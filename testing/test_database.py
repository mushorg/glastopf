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

import unittest

from datetime import datetime

from modules.reporting import log_sqlite
from modules.reporting import log_mongodb
from modules.reporting import log_mysql
from modules.reporting import log_postgresql


class AttackEvent(object):
    class ParsedRequest():
        def __init__(self):
            self.method = "GET"
            self.url = "/test"
            self.parameters = ""
            self.version = "HTTP/1.1"
            self.header = {"Host": "None", "User-Agent": "Test"}
            self.body = ""

    def __init__(self):
        self.parsed_request = self.ParsedRequest()
        self.event_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.source_addr = ("1.2.3.4", "1234")
        self.matched_pattern = 0
        self.file_name = "12345678901234567890123456789011"


class TestDatabaseReporting(unittest.TestCase):
    """Description"""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sqlite_reporter(self):
        """Objective:
        Expected Results:
        Notes:"""
        sqlite = log_sqlite.LogSQLite()
        # TODO: Finish test

    def test_mongodb_reporter(self):
        """Objective:
        Expected Results:
        Notes:"""
        mdb = log_mongodb.LogMongoDB()
        mdb.insert(AttackEvent())
        res = mdb.collection.find_one()['file_name']
        mdb.connection.drop_database('test')
        self.assertEqual(res, "12345678901234567890123456789011")

    def test_mysql_reporter(self):
        """Objective:
        Expected Results:
        Notes:"""
        mysql = log_mysql.LogMySQL()
        mysql.insert(AttackEvent())
        # TODO: Fix file name
        file_name = mysql.select()[6]
        mysql.drop()
        mysql.close()
        self.assertEqual(file_name, "12345678901234567890123456789011")

    def test_postgresql_reporter(self):
        """Objective:
        Expected Results:
        Notes:"""
        postgresql = log_postgresql.LogPostgreSQL()
        postgresql.insert(AttackEvent())
        file_name = postgresql.select()[6]
        postgresql.drop()
        postgresql.close()
        self.assertEqual(file_name, "12345678901234567890123456789011")
