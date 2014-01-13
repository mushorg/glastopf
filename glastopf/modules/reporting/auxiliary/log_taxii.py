# Copyright (C) 2014  Johnny Vestergaard <jkv@unixcluster.dk>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import logging

import libtaxii
import libtaxii.clients as tc
from libtaxii.messages import ContentBlock, InboxMessage, generate_message_id
from libtaxii.clients import HttpClient

from glastopf.modules.reporting.auxiliary.stix.stix_transform import StixTransformer
from glastopf.modules.reporting.auxiliary.base_logger import BaseLogger


logger = logging.getLogger(__name__)


class TaxiiLogger(BaseLogger):
    def __init__(self, data_dir, config='glastopf.cfg'):
        BaseLogger.__init__(self, config)
        self.options = {'enabled': self.config.getboolean('taxii', 'enabled')}
        self.host = self.config.get('taxii', 'host')
        self.port = self.config.getint('taxii', 'port')
        self.inbox_path = self.config.get('taxii', 'inbox_path')
        self.use_https = self.config.getboolean('taxii', 'use_https')
        self.client = HttpClient()
        self.client.setProxy('noproxy')

        auth_credentials = {'username': self.config.get('taxii', 'auth_basic_username'),
                            'password': self.config.get('taxii', 'auth_basic_password'),
                            'key_file': self.config.get('taxii', 'auth_certificate_keyfile'),
                            'cert_file': self.config.get('taxii', 'auth_certificate_certfile')}
        self.client.setAuthCredentials(auth_credentials)

        if self.config.getboolean('taxii', 'use_auth_basic'):
            self.client.setAuthType(tc.HttpClient.AUTH_BASIC)
        elif self.config.getboolean('taxii', 'use_auth_certificate'):
            self.client.setAuthType(tc.HttpClient.AUTH_CERT)
        elif self.config.getboolean('taxii', 'use_auth_basic') and self.config.getboolean('taxii', 'use_auth_certificate'):
            self.client.setAuthType(tc.HttpClient.AUTH_CERT_BASIC)
        else:
            self.client.setAuthType(tc.HttpClient.AUTH_NONE)

        self.stix_transformer = StixTransformer(self.config, data_dir)

    def insert(self, event):
        # converts from conpot log format to STIX compatible xml
        stix_package = self.stix_transformer.transform(event)

        # wrapping the stix message in a TAXII envelope
        content_block = ContentBlock(libtaxii.CB_STIX_XML_10, stix_package)

        inbox_message = InboxMessage(message_id=generate_message_id(), content_blocks=[content_block])
        inbox_xml = inbox_message.to_xml()

        # the actual call to the TAXII web service
        response = self.client.callTaxiiService2(self.host, self.inbox_path, libtaxii.VID_TAXII_XML_10, inbox_xml, self.port)
        response_message = libtaxii.get_message_from_http_response(response, '0')

        if response_message.status_type != libtaxii.messages.ST_SUCCESS:
            logger.error('Error while transmitting message to TAXII server: {0}'.format(response_message.status_detail))
            return False
        else:
            return True
