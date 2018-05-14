# Copyright (C) 2018 Andre Vorbach @vorband
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging
import os
import gevent

import botocore.session, botocore.client
from botocore.exceptions import ClientError

from glastopf.modules.reporting.auxiliary.base_logger import BaseLogger


logger = logging.getLogger(__name__)


class S3Logger(BaseLogger):

    def __init__(self, data_dir, work_dir, config="glastopf.cfg", reconnect=True):
        config = os.path.join(work_dir, config)
        BaseLogger.__init__(self, config)
        self.files_dir = os.path.join(data_dir, 'files/')
        self.enabled = self.config.getboolean("s3storage", "enabled")
        self._initial_connection_happend = False
        self.options = {'enabled': self.enabled}
        if self.enabled:
            self.endpoint = self.config.get("s3storage", "endpoint")
            self.accesskey = self.config.get("s3storage", "aws_access_key_id")
            self.secretkey = self.config.get("s3storage", "aws_secret_access_key")
            self.version = self.config.get("s3storage", "signature_version")
            self.region = self.config.get("s3storage", "region")
            self.bucket = self.config.get("s3storage", "bucket")
            self.enabled = True
            self.s3client = None
            self.s3session = None
            gevent.spawn(self._start_connection)

    def _start_connection(self):
        self.s3session = botocore.session.get_session()
        self.s3session.set_credentials(self.accesskey, self.secretkey)
        self.s3client = self.s3session.create_client(
            's3',
            endpoint_url=self.endpoint,
            region_name=self.region,
            config=botocore.config.Config(signature_version=self.version)
        )
        try:
            self.s3client.head_bucket(Bucket=self.bucket)
            self._initial_connection_happend = True
        except ClientError as e:
            logger.error("Could not establish s3 connection to bucket '%s' on %s. Received error: %s" % (self.bucket, self.endpoint, e.response['Error']['Message']))

    def insert(self, attack_event):
        if self._initial_connection_happend:
            if attack_event.file_sha256 is not None:
                if attack_event.known_file:
                    logger.debug('sha256:{0} / md5:{1} is a known file, it will not be uploaded.'.format(attack_event.file_sha256, attack_event.file_name))
                    return
                with file(os.path.join(self.files_dir, attack_event.file_name), 'r') as file_handler:
                    try:
                        # check if file exists in bucket
                        searchFile = self.s3client.list_objects_v2(Bucket=self.bucket, Prefix=attack_event.file_sha256)
                        if (len(searchFile.get('Contents', []))) == 1 and str(searchFile.get('Contents', [])[0]['Key']) == attack_event.file_sha256:
                            logger.debug('Not storing file (sha256:{0}) to s3 bucket "{1}" on {2} as it already exists in the bucket.'.format(attack_event.file_sha256, self.bucket, self.endpoint))
                            return
                        # upload file to s3
                        self.s3client.put_object(Bucket=self.bucket, Body=file_handler, Key=attack_event.file_sha256)
                        logger.debug('Storing file (sha256:{0}) using s3 bucket "{1}" on {2}'.format(attack_event.file_sha256, self.bucket, self.endpoint))
                    except ClientError as e:
                        logger.warning("Received error: %s", e.response['Error']['Message'])
        else:
            logger.warning('Not storing attack file because initial s3 connection test did not succeeded')

