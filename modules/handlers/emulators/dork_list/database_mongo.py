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
from pymongo import MongoClient, uri_parser

import cluster
import logging

logger = logging.getLogger(__name__)


class Database(object):
    """
    Responsible for all dork related communication with the main glastopf mongo database.
    """

    def __init__(self, connection_string):

        uri_dict = uri_parser.parse_uri(connection_string)
        if not uri_dict['database']:
            raise Exception("Invalid Mongo URI. Database name must be specified.")

        try:
            self.client = MongoClient(connection_string)
            self.events_coll = client[uri_dict['database']]
        except:
            logger.exception("Unable to connect to MongoDB service.")
            raise

    def select_data(self,):
        url_list = []
        self.full_url_list = []
        data = self.events_coll.find({'pattern': self.pattern})
        self.num_results = data.count()
        data = list(data.distinct('request.url'))

        self.num_distinct_results = len(data)

        for request in data:
            if request != None:
                url = request.split('=', 1)[0]
                url_list.append(url)
        return url_list

    def select_entry(self, starts_with):
        regx = re.compile(starts_with + ".*", re.IGNORECASE)
        data = list(self.events_coll.find({'request.url': regx}))
        return data

    def insert_dorks(self, insert_list):
        if len(insert_list) == 0:
            return

        conn = self.engine.connect()
        trans = conn.begin()
        try:
            for item in insert_list:
                collection = item['table']
                #'firsttime' can be extracted from the _id (ObjectId)
                self.db[collection].update({'content': item['content']},
                                           {'$set': {'lastime': datetime.now()},
                                            '$inc': {'count': 1}})

    def get_dork_list(self, tablename, starts_with=None):
        conn = self.engine.connect()
        table = self.tables[tablename]

        if starts_with == None:
            result = conn.execute(select([table]))
        else:
            result = conn.execute(
                table.select().
                where(table.c.content.like('%{0}'.format(starts_with))))

        return_list = []
        for entry in result:
            return_list.append(entry[0])

        return return_list
