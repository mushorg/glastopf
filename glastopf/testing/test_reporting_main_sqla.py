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
from datetime import datetime

from glastopf.modules.reporting.main import log_sql
from sqlalchemy import create_engine

import glastopf.modules.events.attack as attack
from glastopf.modules.HTTP.handler import HTTPHandler


class TestSQLAlchemy(unittest.TestCase):
    def test_sqla_insert(self):
        #in-memory sqlite database
        sqla_engine = create_engine("sqlite:///")
        maindb = log_sql.Database(sqla_engine)

        #prepare attack event
        attack_event = attack.AttackEvent()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        attack_event.event_time = timestamp
        attack_event.matched_pattern = "test_test"
        attack_event.source_addr = ("192.168.1.201", 12345)
        request = (
            'GET /breadandbytter.php?a=b HTTP/1.0\r\n'
            'Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3\r\n'
            'ISO-8859-1,utf-8;q=0.7,*;q=0.3r\n'
            'Connection: keep-alive\r\n\r\n'
            'some stuff'
        )
        attack_event.http_request = HTTPHandler(request, None)

        #insert attack event
        maindb.insert(attack_event)

        #try to extract event from the database
        sql = "SELECT * FROM events"
        results = sqla_engine.connect().execute(sql).fetchall()
        #Check if database returned the correct amount
        self.assertEqual(len(list(results)), 1)
        print results[0]
        entry = results[0]
        #check basic attributes
        #time
        self.assertEqual(entry[1], timestamp)
        #source
        self.assertEqual(entry[2], "192.168.1.201:12345")
        #request_url
        self.assertEqual(entry[3], "/breadandbytter.php?a=b")
        #request_body
        self.assertEqual(entry[4], request)
        #pattern
        self.assertEqual(entry[5], "test_test")


if __name__ == '__main__':
    unittest.main()
