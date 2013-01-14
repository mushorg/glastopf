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

from sqlalchemy import create_engine

import re

from ConfigParser import ConfigParser

import cluster
import logging

logger = logging.getLogger(__name__)


class Database(object):
    """
    Responsible for all dork related communication with the main glastopf database.
    """

    def __init__(self, config="glastopf.cfg"):
        self.config = config
        conf_parser = ConfigParser()
        self.conf_parser = conf_parser
        conf_parser.read(config)
        self.pattern = self.conf_parser.get('dork-db', 'pattern')
        if conf_parser.get("mongodb", "enabled") != "True":
            if conf_parser.get("sql", "enabled") == "True":

                connectionstring = conf_parser.get("sql", "connection_string")
                self.engine = create_engine(connectionstring, echo=False)
                self.dbtype = 'sql'
            else:
                self.connection = None
        else:
            self.options = {
                "enabled": conf_parser.get("dork-db", "enabled"),
                "host": conf_parser.get("mongodb", "host"),
                "port": conf_parser.getint("mongodb", "port"),
                "user": conf_parser.get("mongodb", "user"),
                "password": conf_parser.get("mongodb", "password"),
                "database": conf_parser.get("mongodb", "database"),
                "collection": conf_parser.get("mongodb", "collection"),
            }
            self.dbtype = 'mongodb'
            try:
                from pymongo import Connection
                self.connection = Connection(self.options['host'],
                                             self.options['port'])
            except Exception as e:
                logger.exception("Unable to connect to MongoDB service: {0}".format(e))
                self.connection = None
            else:
                self.db = self.connection[self.options['database']]
                #self.db.authenticate(self.options['user'],
                #                self.options['password'])
                self.collection = self.db[self.options['collection']]

    def select_data(self,):
        url_list = []
        self.full_url_list = []
        if self.dbtype == 'mongodb':
            data = self.collection.find({'pattern': self.pattern})
            self.num_results = data.count()
            data = list(data.distinct('request.url'))
        else:
            data = self.get_pattern_requests_sql()
            self.num_results = len(data)
            data = list(set(data))
        self.num_distinct_results = len(data)
        #seed with static data if we got too few hits in events db
        #if len(data) < 100:
        #    dork_seeds = random.sample(self.dorkdb.get_dork_list('inurl'), 100)
        #    data = dork_seeds
        for request in data:
            if request != None:
                url = request.split('=', 1)[0]
                url_list.append(url)
        return url_list

    def get_pattern_requests_sql(self):
        return_list = []
        sql = "SELECT request_url FROM events WHERE pattern = :x"
        results = self.engine.connect().execute(sql, x=self.pattern).fetchall()
        for row in results:
            return_list.append(row[0])
        return return_list

    def select_entry(self, starts_with):
        if self.dbtype == 'mongodb':
            regx = re.compile(starts_with + ".*", re.IGNORECASE)
            data = list(self.collection.find({'request.url': regx}))
        else:
            data = []
            sql = "SELECT request_url FROM events WHERE request_url LIKE :x"
            results = self.engine.connect().execute(sql, x=starts_with + "%").fetchall()
            logger.debug("Searching for: {0}".format(starts_with))
            for row in results:
                data.append(row[0])
        return data

    def process(self):
        url_list = self.select_data()
        self.clusterer = cluster.Cluster()
        self.clusterer.cluster(url_list, self.config)


if __name__ == "__main__":
    d = Database(config="../../../../glastopf.cfg")
    url_list = d.select_data()
    c = cluster.Cluster()
    c.cluster(url_list, d.config)
