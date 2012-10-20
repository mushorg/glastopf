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

from ConfigParser import ConfigParser

import cluster
import dork_db
import random


class DorkDB():

    def __init__(self, config="glastopf.cfg"):
        self.config = config
        conf_parser = ConfigParser()
        self.conf_parser = conf_parser
        conf_parser.read(config)
        if conf_parser.get("mongodb", "enabled") != "True":
            if conf_parser.get("sqlite", "enabled") == "True":
                import sqlite3
                self.connection = sqlite3.connect("db/%s" %
                                conf_parser.get("sqlite", "database"))
                self.cursor = self.connection.cursor()
                self.dbtype = 'sqlite'
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
                print "Unable to connect to MongoDB service:", e
                self.connection = None
            else:
                self.db = self.connection[self.options['database']]
                #self.db.authenticate(self.options['user'],
                #                self.options['password'])
                self.collection = self.db[self.options['collection']]

    def insert_data(self, data):
        self.collection.insert(data)

    def count_data(self):
        if self.dbtype == 'mongodb':
            self.num_entries = self.collection.count()
        else:
            sql = "SELECT COUNT(*) FROM events"
            self.cursor.execute(sql)
            self.num_entries = self.cursor.fetchone()[0]

    def select_data(self,):
        url_list = []
        self.full_url_list = []
        self.pattern = self.conf_parser.get('dork-db', 'pattern')
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
        if len(data) < 100:
            data = data + self.get_dorks_from_dorkdb()
        for request in data:
            url = request.split('=', 1)[0]
            url_list.append(url)
        return url_list

    def get_pattern_requests_sql(self):
        return_list = []
        sql = "SELECT request FROM events WHERE module = (?)"
        self.cursor.execute(sql, (self.pattern,))
        for row in self.cursor.fetchall():
            return_list.append(row[0])
        return return_list

    def get_dorks_from_dorkdb(self):
        return_list = []
        dorkdb = dork_db.DorkDB()
        entries = random.sample(dorkdb.get_dork_list('inurl'), 100)
        for entry in entries:
            return_list.append(entry[0])
        return return_list

    def select_data_old(self,):
        url_list = []
        self.full_url_list = []
        self.pattern = self.conf_parser.get('dork-db', 'pattern')
        data = self.collection.find({'pattern': self.pattern})
        self.num_results = data.count()
        data = data.distinct('request.url')
        for request in data:
            url = request.split('=', 1)[0]
            url_list.append(url)
        self.num_distinct_results = len(url_list)
        return url_list

    def select_entry(self, starts_with):
        if self.dbtype == 'mongodb':
            regx = re.compile(starts_with + ".*", re.IGNORECASE)
            data = list(self.collection.find({'request.url': regx}))
        else:
            data = []
            sql = "SELECT request FROM events WHERE request LIKE (?)"
            self.cursor.execute(sql, (starts_with + '%',))
            for row in self.cursor.fetchall():
                data.append(row[0])
        return data

    def process(self):
        url_list = self.select_data()
        self.clusterer = cluster.Cluster()
        self.clusterer.cluster(url_list, self.config)

    def conn_info(self):
        if self.dbtype == 'mongodb':
            return ('mongodb', self.db.name, self.collection.name)
        else:
            return ('sqlite',
                    self.conf_parser.get("sqlite", "database"),
                    'events'
                    )


if __name__ == "__main__":
    d = DorkDB(config="../../../../glastopf.cfg")
    url_list = d.select_data()
    c = cluster.Cluster()
    c.cluster(url_list, d.config)
