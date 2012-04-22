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

import json
from ConfigParser import ConfigParser

import psycopg2


class LogPostgreSQL(object):

    def __init__(self, config="glastopf.cfg"):
        conf_parser = ConfigParser()
        conf_parser.read(config)
        self.options = {
            "host": conf_parser.get("postgresql", "host"),
            "port": conf_parser.getint("postgresql", "port"),
            "user": conf_parser.get("postgresql", "user"),
            "password": conf_parser.get("postgresql", "password"),
            "database": conf_parser.get("postgresql", "database"),
            }
        self.connection = psycopg2.connect("dbname=%s user=%s" %
                                           (
                                            self.options['database'],
                                            self.options['user'],
                                            )
                                           )
        self.create()

    def create(self):
        cursor = self.connection.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS events(
                       id serial PRIMARY KEY,
                       timestamp VARCHAR(19),
                       source_addr VARCHAR(15),
                       request VARCHAR(255),
                       header VARCHAR(255),
                       module INT,
                       filename VARCHAR(32),
                       host VARCHAR(255))
                       """)
        self.connection.commit()

    def insert(self, attack_event):
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO events(timestamp, source_addr, request,
            header, module, filename, host)
            VALUES(%s, %s, %s, %s, %s, %s, %s)
            """,
            (
            attack_event.event_time,
            ":".join((attack_event.source_addr[0],
                      str(attack_event.source_addr[1]))),
            attack_event.parsed_request.url,
            json.dumps(attack_event.parsed_request.header),
            attack_event.matched_pattern,
            attack_event.file_name,
            attack_event.parsed_request.header.get('Host', "None")
            )
                       )
        self.connection.commit()
        cursor.close()

    def select(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM events")
        res = cursor.fetchone()
        cursor.close()
        return res

    def drop(self, table="events"):
        cursor = self.connection.cursor()
        cursor.execute("DROP TABLE %s" % table)
        self.connection.commit()
        cursor.close()

    def close(self):
        if self.connection:
            self.connection.close()
