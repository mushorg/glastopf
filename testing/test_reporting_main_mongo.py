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
import datetime

from modules.reporting.main import log_mongodb
from sqlalchemy import create_engine

from modules.handlers import request_handler
from datetime import datetime
import modules.events.attack as attack
import modules.HTTP.util as util
from pymongo import MongoClient
import uuid



class TestSQLAlchemy(unittest.TestCase):

    def test_mongodb_insert(self):

        db_name = 'glastopf-test-{0}'.format(str(uuid.uuid4())[0:10])
        conn_string = "mongodb://localhost:27017/{0}".format(db_name)

        try:
            maindb = log_mongodb.Database(conn_string)

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

            maindb.insert(attack_event)


            collection = MongoClient(conn_string)[db_name]['events']
            results = list(collection.find())
            
            #Check if database returned the correct amount
            self.assertEqual(len(list(results)), 1)

            entry = results[0]
            self.assertEqual(entry["pattern"], "test_test")
            self.assertEqual(entry["request"]["body"], "some stuff")
            self.assertEqual(entry["request"]["parameters"], "")
            self.assertEqual(entry["request"]["url"], "/breadandbytter.php?a=b")
            self.assertEqual(entry["request"]["header"]['Accept-Charset'], "ISO-8859-1,utf-8;q=0.7,*;q=0.3")
            self.assertEqual(entry["request"]["header"]['Connection'], "keep-alive")
            self.assertEqual(entry["request"]["method"], "GET")
            self.assertEqual(entry["source"][0], "192.168.1.201")
            self.assertEqual(entry["source"][1], 12345)

        finally:
            client = MongoClient(conn_string)
            client.drop_database(db_name)
