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
from sqlalchemy import exc

from ConfigParser import ConfigParser

import threading
import Queue

from modules.reporting.base_logger import BaseLogger

import time
import logging

logger = logging.getLogger(__name__)


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
            SQL.event_queue = Queue.Queue()
            consumer_thread = threading.Thread(target=self.consumer)
            consumer_thread.daemon = True
            consumer_thread.start()

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
                    entry = attack_event.event_dict()

                    for key, value in entry['request'].items():
                        entry['request_' + key] = value

                    entry['source'] = (entry['source'][0] + ":" + str(entry['source'][1]))
                    entry['request_header'] = json.dumps(entry['request_header'])

                    del entry['request']

                    insert_dicts.append(entry)

            if len(insert_dicts) > 0:
                try:
                    conn = self.engine.connect()
                    conn.execute(self.events_table.insert(), insert_dicts)
                except exc.DBAPIError as err:
                    logger.warning("Error caught while inserting %i events into SQL, will retry in %s seconds. (%s)" %
                                     (len(insert_dicts), self.wait_seconds, err))
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
        Column('time', String),
        Column('source', String),
        Column('request_method', String),
        Column('request_url', String),
        Column('request_parameters', String),
        Column('request_version', String),
        Column('request_header', String),
        Column('request_body', String),
        Column('pattern', String),
        Column('filename', String),
        Column('response', String),
        )

        self.engine = create_engine(self.options['connection_string'])

        #only creates if it cant find the schema
        meta.create_all(self.engine)
