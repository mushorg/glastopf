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

from datetime import datetime
import uuid
from ConfigParser import ConfigParser
import logging

import libtaxii
from libtaxii.messages import ContentBlock, InboxMessage, generate_message_id
from libtaxii.clients import HttpClient
from glastopf.modules.reporting.auxiliary.stix.stix_transform import StixTransformer
from glastopf.modules.reporting.auxiliary.base_logger import BaseLogger


logger = logging.getLogger(__name__)


class TaxiiLogger(BaseLogger):
    def __init__(self, data_dir, config_file='glastopf.cfg'):
        config = ConfigParser()
        config.read(config_file)
        self.options = {'enabled': config.getboolean('taxii', 'enabled')}
        self.host = config.get('taxii', 'host')
        self.port = config.getint('taxii', 'port')
        self.inbox_path = config.get('taxii', 'inbox_path')
        self.use_https = config.getboolean('taxii', 'use_https')
        self.client = HttpClient()
        self.client.setProxy('noproxy')
        self.stix_transformer = StixTransformer(config, data_dir)

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
