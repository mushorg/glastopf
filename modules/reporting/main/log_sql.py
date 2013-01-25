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
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc

import threading
import Queue

import time
import logging

import modules.processing.ip_profile as ipp

logger = logging.getLogger(__name__)


class Database(object):

    def __init__(self, engine):
        self.engine = engine
        self.setup_mapping()
        self.session = sessionmaker(bind=self.engine)()

    def insert(self, attack_event):
        entry = attack_event.event_dict()

        for key, value in entry['request'].items():
            entry['request_' + key] = value

        entry['source'] = (entry['source'][0] + ":" + str(entry['source'][1]))
        entry['request_header'] = json.dumps(entry['request_header'])

        del entry['request']

        try:
            conn = self.engine.connect()
            conn.execute(self.events_table.insert(entry))
        except exc.OperationalError as e:
            message = str(e)[:35]
            logger.error("Error inserting attack event into main database: {0}".format(message))
            
    def insert_profile(self, ip_profile):
        self.session.add(ip_profile)
        self.session.commit()
        
    def update_profile(self, ip_profile):
        self.session.commit()
    
    def get_profile(self, source_ip):
        ip_profile = self.session.query(ipp.IPProfile).filter(
                                 ipp.IPProfile.ip==source_ip).first()
        return ip_profile

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

        #only creates if it cant find the schema
        meta.create_all(self.engine)
        
    
