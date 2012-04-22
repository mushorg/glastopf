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

from ConfigParser import ConfigParser

from pymongo import Connection


class LogMongoDB(object):

    def __init__(self, config="glastopf.cfg"):
        conf_parser = ConfigParser()
        conf_parser.read(config)
        self.options = {
            "host": conf_parser.get("mongodb", "host"),
            "port": conf_parser.getint("mongodb", "port"),
            "user": conf_parser.get("mongodb", "user"),
            "password": conf_parser.get("mongodb", "password"),
            "database": conf_parser.get("mongodb", "database"),
            "collection": conf_parser.get("mongodb", "collection"),
            }
        self.connection = Connection(self.options['host'],
                                     self.options['port'])
        self.db = self.connection[self.options['database']]
        self.db.authenticate(self.options['user'],
                             self.options['password'])
        self.collection = self.db[self.options['collection']]

    def insert(self, attack_event):
        self.collection.insert(attack_event.event_dict())
        self.connection.end_request()
