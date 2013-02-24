# Copyright (C) 2012  Lukas Rist
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

from pymongo import MongoClient, uri_parser

import logging

logger = logging.getLogger(__name__)


class Database(object):

    def __init__(self, connection_string):

    	uri_dict = uri_parser.parse_uri(connection_string)
    	if not uri_dict['database']:
    		raise Exception("Invalid Mongo URI. Database name must be specified.")

        try:
            client = MongoClient(connection_string)
            self.db = client[uri_dict['database']]
        except:
            logger.exception("Unable to connect to MongoDB service.")
            raise

    def insert(self, attack_event):
        self.db["events"].insert(attack_event.event_dict())
