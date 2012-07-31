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

from modules.reporting.base_logger import BaseLogger


class LogMongoDB(BaseLogger):

    def __init__(self, config="glastopf.cfg", create_tables=True):
        conf_parser = ConfigParser()
        conf_parser.read(config)
        self.options = {
            "enabled": conf_parser.get("mongodb", "enabled"),
            "host": conf_parser.get("mongodb", "host"),
            "port": conf_parser.getint("mongodb", "port"),
            "user": conf_parser.get("mongodb", "user"),
            "password": conf_parser.get("mongodb", "password"),
            "database": conf_parser.get("mongodb", "database"),
            "collection": conf_parser.get("mongodb", "collection"),
            }
        if self.options['enabled'] == 'True':
            try:
                from pymongo import Connection
                self.connection = Connection(self.options['host'],
                                     self.options['port'])
            except:
                print "Unable to connect to MongoDB service"
                self.options['enabled'] = 'False'
            else:
                self.db = self.connection[self.options['database']]
                self.db.authenticate(self.options['user'],
                                 self.options['password'])
                self.collection = self.db[self.options['collection']]
        else:
            return None

    def insert(self, attack_event):
        self.collection.insert(attack_event.event_dict())
        self.connection.end_request()
