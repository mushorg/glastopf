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

import re
import warnings
from datetime import datetime

import logging
logger = logging.getLogger(__name__)

try:
    from pymongo import MongoClient, uri_parser
except ImportError:
    logger.warn('Unable to import module pymongo')

class Database(object):
    """
    Responsible for all dork related communication with the glastopf mongo database.
    """

    def __init__(self, connection_string):

        uri_dict = uri_parser.parse_uri(connection_string)
        if not uri_dict['database']:
            raise Exception("Invalid Mongo URI. Database name must be specified.")

        try:
            with warnings.catch_warnings(record=True):
                self.client = MongoClient(connection_string)
            self.db = self.client[uri_dict['database']]
        except:
            logger.exception("Unable to connect to MongoDB service.")
            raise

    def select_data(self, pattern="rfi"):
        """
        Selects URLs from the events database filtered by attack module.
        """
        url_list = []

        data = self.db.events.find({'pattern': pattern})
        data = list(data.distinct('request_url'))

        self.num_distinct_results = len(data)

        for request in data:
            if request != None:
                url = request.split('=', 1)[0]
                url_list.append(url)
        return url_list

    def select_entry(self, starts_with):
        """
        Selects URL from main database filterned by name.
        """
        regx = re.compile(starts_with + ".*", re.IGNORECASE)
        urls = list(self.db.events.find({'request_url': regx}))
        return urls

    def insert_dorks(self, insert_list):
        if len(insert_list) == 0:
            return

        for item in insert_list:
            collection = item['table']
            self.db[collection].update({'content': item['content']},
                                       {'$set': {'lastime': datetime.now()},
                                        '$inc': {'count': 1}}, upsert=True)

    def get_dork_list(self, collection, starts_with=None):
        """
        Selects dork from dork collection.
        """
        if starts_with != None:
            regx = re.compile(starts_with + "^{0}".format(starts_with), re.IGNORECASE)
            dorks = list(self.db[collection].find({'content': regx},
                                                  {'content': 1, '_id': 0}))
        else:
            dorks = list(self.db[collection].find({}, {'content': 1, '_id': 0}))

        return_list = []
        for item in dorks:
            return_list.append(item['content'])

        return return_list
