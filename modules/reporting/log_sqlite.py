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

import sqlite3
import time
from multiprocessing import Process, Queue

from ConfigParser import ConfigParser

from modules.reporting.base_logger import BaseLogger


class LogSQLite(BaseLogger):
    # TODO: Add SQLite error handling

    def __init__(self, config="glastopf.cfg", create_tables=True):
        conf_parser = ConfigParser()
        conf_parser.read(config)
        self.options = {
            "enabled": conf_parser.get("sqlite", "enabled"),
            "database": conf_parser.get("sqlite", "database"),
            }
        if self.options['enabled'] == "True":
            try:
                self.connection = sqlite3.connect("db/%s" %
                                    self.options['database'])
            except:
                print "Unable to connect to MySQL service"
                self.options['enabled'] = 'False'
            else:
                if create_tables:
                    self.create()
        else:
            return None

        #create message_queue and start worker thread
        try:
            LogSQLite.message_queue
        except AttributeError:
            LogSQLite.message_queue = Queue()
            consumer_process = Process(target=self.consumer)
            consumer_process.start()

    def consumer(self):
        while True:
            self.write_insert(LogSQLite.message_queue.get())
            time.sleep(0.1)

    def create(self):
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS events(
                id INTEGER PRIMARY KEY,
                timestamp TEXT,
                source_addr TEXT,
                method TEXT,
                request TEXT,
                request_body TEXT,
                module TEXT,
                filename TEXT,
                response TEXT,
                host TEXT)
                """)
        self.connection.commit()
        self.cursor.close()

    #called by multiple producers
    def insert(self, attack_event):
        LogSQLite.message_queue.put(attack_event)

    #called by single consumer
    def write_insert(self, attack_event):
        self.cursor = self.connection.cursor()
        if attack_event.matched_pattern.strip() == "unknown":
            response = attack_event.response.split('\r\n\r\n')[0]
        else:
            response = attack_event.response
        self.cursor.execute("""
                INSERT INTO events VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (None, attack_event.event_time,
                 (attack_event.source_addr[0] + ":" +
                 str(attack_event.source_addr[1])),
                 attack_event.parsed_request.method,
                 attack_event.parsed_request.url,
                 attack_event.parsed_request.body,
                 attack_event.matched_pattern,
                 attack_event.file_name, response,
                 attack_event.parsed_request.header.get('Host', "None")))
        self.connection.commit()
        self.cursor.close()
