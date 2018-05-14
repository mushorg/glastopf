# Copyright (C) 2015 Johnny Vestergaard <jkv@unixcluster.dk>
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

#import json
import logging

from sqlalchemy import Table, Column, Integer, String, MetaData, TEXT, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc
import glastopf.modules.processing.ip_profile as ipp

logger = logging.getLogger(__name__)


class Database(object):
    def __init__(self, engine):
        self.engine = engine
        ipp.Base.metadata.create_all(self.engine)
        self.setup_mapping()
        self.session = sessionmaker(bind=self.engine)()

    def insert(self, attack_event):
        entry = attack_event.event_dict()

        entry['source'] = (entry['source'][0] + ":" + str(entry['source'][1]))

        try:
            conn = self.engine.connect()
            conn.execute(self.events_table.insert(entry))
        except exc.OperationalError as e:
            logger.error("Error inserting attack event into main database: {0}".format(e))

    def insert_profile(self, ip_profile):
        # print "last_event_time for ip %s:%s"%(
        #             ip_profile.ip, ip_profile.last_event_time)
        # .split()[0] is added to deal with multiple ASNs
        self.session.add(ip_profile)
        try:
            self.session.commit()
        except exc.OperationalError as e:
            self.session.rollback()
            logger.error("Error inserting profile into main database: {0}".format(e))

    def update_db(self):
        try:
            self.session.commit()
        except exc.OperationalError as e:
            self.session.rollback()
            logger.error("Error updating profile in main database: {0}".format(e))

    def get_profile(self, source_ip):
        ip_profile = self.session.query(ipp.IPProfile).filter(
            ipp.IPProfile.ip == source_ip).first()
        return ip_profile

    def setup_mapping(self):
        meta = MetaData()
        self.events_table = Table(
            'events', meta,
            Column('id', Integer, primary_key=True, ),
            Column('time', String(30)),
            Column('source', String(30)),
            Column('request_url', String(500)),
            Column('request_raw', TEXT),
            Column('pattern', String(20)),
            Column('filename', String(500)),
            Column('file_sha256', String(500)),
            Column('version', String(10)),
            Column('sensorid', String(36)),
            Column('known_file', Boolean())
        )
        #only creates if it cant find the schema
        meta.create_all(self.engine)
