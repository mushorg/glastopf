# Copyright (C) 2015 Johnny Vestergaard
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
import warnings
from datetime import datetime

from glastopf.modules.reporting.main import log_mongodb
from pymongo import MongoClient, uri_parser
import glastopf.modules.events.attack as attack
from glastopf.modules.HTTP.handler import HTTPHandler
from glastopf.testing import helpers


class TestMongoMainDatbase(unittest.TestCase):
    @unittest.skip('disabled until mongodb is a real database')
    def test_mongodb_insert(self):

        conn_string = helpers.create_mongo_database(fill=False)

        db_name = uri_parser.parse_uri(conn_string)["database"]

        try:
            maindb = log_mongodb.Database(conn_string)

            attack_event = attack.AttackEvent()
            attack_event.event_time = self.event_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            attack_event.matched_pattern = "test_test"
            attack_event.source_addr = ("192.168.1.201", 12345)
            request = ("GET /breadandbytter.php?a=b HTTP/1.0\r\n"
            "Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3\r\n"
            "ISO-8859-1,utf-8;q=0.7,*;q=0.3r\n"
            "Connection: keep-alive\r\n\r\n"
            "some stuff")
            attack_event.http_request = HTTPHandler(request, None)

            maindb.insert(attack_event)

            with warnings.catch_warnings(record=True):
                collection = MongoClient(conn_string)[db_name]["events"]
            results = list(collection.find())

            #Check if database returned the correct amount
            self.assertEqual(len(list(results)), 1)

            entry = results[0]

            self.assertEqual(entry["source"][0], "192.168.1.201")
            self.assertEqual(entry["source"][1], 12345)
            self.assertEqual(entry["pattern"], "test_test")
            self.assertEqual(entry["request_raw"], request)
            self.assertEqual(entry["request_url"], "/breadandbytter.php?a=b")

        finally:
            helpers.delete_mongo_testdata(conn_string)


if __name__ == '__main__':
    unittest.main()
