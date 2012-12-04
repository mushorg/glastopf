# Copyright (C) 2012 Johnny Vestergaard <jkv@unixcluster.dk>
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

from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine
import logging

from ConfigParser import ConfigParser

# from multiprocessing import Process, Queue
import multiprocessing
# for the exception
import Queue

from modules.reporting.base_logger import BaseLogger

import time


class SQL(BaseLogger):

    def __init__(self, config="glastopf.cfg", create_tables=True):
        conf_parser = ConfigParser()
        conf_parser.read(config)
        self.options = {
            "enabled": conf_parser.get("sql", "enabled"),
            "connection_string": conf_parser.get("sql", "connection_string"),
            }
        self.setup_mapping()
        self.wait_seconds = 1
        try:
            SQL.event_queue
        except AttributeError:
            SQL.event_queue = multiprocessing.Queue()
            consumer_process = multiprocessing.Process(target=self.consumer)
            consumer_process.start()

    def consumer(self):
        while True:
            insert_dicts = []
            event_backup = []
            #fetch as many events at possible before inserting
            while not SQL.event_queue.empty():
                try:
                    attack_event = SQL.event_queue.get(True, 1)
                    event_backup.append(attack_event)
                except Queue.Empty:
                    break
                else:
                    entry = {
                    'timestamp': attack_event.event_time,
                    'source_addr': (attack_event.source_addr[0] + ":" + str(attack_event.source_addr[1])),
                    'method': attack_event.parsed_request.method,
                    'request': attack_event.parsed_request.url,
                    'request_body': attack_event.parsed_request.body,
                    'request_header': json.dumps(attack_event.parsed_request.header),
                    'module': attack_event.matched_pattern,
                    'filename': attack_event.file_name,
                    'response': attack_event.response,
                    'host': attack_event.parsed_request.header.get('Host', "None")
                    }

                    insert_dicts.append(entry)
            if len(insert_dicts) > 0:
                try:
                    conn = self.engine.connect()
                    conn.execute(self.events_table.insert(), insert_dicts)
                except sqlalchemy.exc.DBAPIError as err:
                    logging.warning("Error caught while inserting %i events into SQL, will retry in %s seconds.i (%s)" %
                                     (len(insert_dicts), self.wait_seconds), err)
                    for item in event_backup:
                        SQL.event_queue.put(item)
            time.sleep(self.wait_seconds)

    #called by multiple producers
    def insert(self, attack_event):
        SQL.event_queue.put(attack_event)

    def setup_mapping(self):
        meta = MetaData()

        self.events_table = Table('events', meta,
        Column('id', Integer, primary_key=True, ),
        Column('timestamp', String),
        Column('source_addr', String),
        Column('method', String),
        Column('request', String),
        Column('request_body', String),
        Column('request_header', String),
        Column('module', String),
        Column('filename', String),
        Column('response', String),
        Column('host', String),
        )

        self.engine = create_engine(self.options['connection_string'],
                                    echo=False)
        #only creates if it cant find the schema
        meta.create_all(self.engine)
