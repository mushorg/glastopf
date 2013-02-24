# Copyright (C) 2013  Johnny Vestergaard
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

import unittest
from datetime import datetime

from glastopf.modules.reporting.main import log_sql
from sqlalchemy import create_engine

import glastopf.modules.events.attack as attack
import glastopf.modules.HTTP.util as util


class TestSQLAlchemy(unittest.TestCase):

    def test_sqla_insert(self):
        #in-memory sqlite database
        sqla_engine = create_engine("sqlite:///")
        maindb = log_sql.Database(sqla_engine)

        #prepare attack event
        attack_event = attack.AttackEvent()
        attack_event.event_time =  self.event_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        attack_event.matched_pattern = "test_test"
        attack_event.source_addr = ("192.168.1.201", 12345)
        attack_event.parsed_request = util.HTTPRequest()
        attack_event.parsed_request.url = "/breadandbytter.php?a=b"
        attack_event.parsed_request.method= "GET"
        attack_event.parsed_request.header = {'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 'Connection': 'keep-alive'}
        attack_event.parsed_request.body = "some stuff"

        #insert attack event
        maindb.insert(attack_event)

        #try to extract event from the database
        sql = "SELECT * FROM events"
        results = sqla_engine.connect().execute(sql).fetchall()
        #Check if database returned the correct amount
        self.assertEqual(len(list(results)), 1)

        entry = results[0]
        #check basic attributes
        #source
        self.assertEqual(entry[2], "192.168.1.201:12345")
        #method
        self.assertEqual(entry[3], "GET")
        #request_url
        self.assertEqual(entry[4], "/breadandbytter.php?a=b")
        #resuest_header
        self.assertEqual(entry[7], '{"Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3", "Connection": "keep-alive"}')
        #request_body
        self.assertEqual(entry[8], "some stuff")
        #pattern
        self.assertEqual(entry[9], "test_test")
