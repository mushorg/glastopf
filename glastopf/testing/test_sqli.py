# Copyright (C) 2015 Lukas Rist
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
import os
import shutil
import tempfile

from glastopf.modules.handlers.request_handler import RequestHandler
import glastopf.modules.events.attack as attack
from glastopf.modules.HTTP.handler import HTTPHandler


class TestSQLiEmulation(unittest.TestCase):
    """Tests the honeypots SQL injection emulation module.
    We first start with the integration test and continue with unit test"""
    def setUp(self):
        self.event = attack.AttackEvent()
        self.event.http_request = HTTPHandler('GET /test.php?q=SELECT%20A%20FROM%20B', None)
        self.data_dir = tempfile.mkdtemp()

    def tearDown(self):
        del self.event
        if os.path.isdir(self.data_dir):
            shutil.rmtree(self.data_dir)

    def _get_test_request(self, attack_event):
        self.test_request = "haha"

    def test_sqli_lexer(self):
        """Objective: Tests the SQL injection lexer.
        Input: SELECT A FROM B
        Expected Results:
        Notes:
        """
        self.event.matched_pattern = "sqli"
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(self.event.matched_pattern)
        self._get_test_request(self.event)
        emulator.handle(self.event)
        self.assertEqual(emulator.ret["fingerprint"], "Enkn")

    def test_sqli_emulator(self):
        """Objective: Assure that the SQL injection module is integrated.
        Input: Inject SELECT a FROM b in parameter q.
        Expected Results: MySQL error message.
        Notes: As there is no table b, the honeypot returns an error message."""
        self.event.matched_pattern = "sqli"
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(self.event.matched_pattern)
        self._get_test_request(self.event)
        emulator.handle(self.event)
        response = "Invalid query: You have an error in your SQL syntax; check the manual that corresponds to your " \
                   "MySQL server version for the right syntax to use near 'SELECT A FROM B' at line 1"
        self.assertEqual(self.event.http_request.get_response(), response)

    def test_sqli_error_based(self):
        """Objective: A simple query provoking an error message from the database.
        Input: Inject a single quotation mark in parameter q.
        Expected Results: MySQL syntax error message.
        Notes: The query is included in the error message."""
        self.event.matched_pattern = "sqli"
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(self.event.matched_pattern)
        self.event.http_request.request_query = {
            "q": ["'"],
        }
        self._get_test_request(self.event)
        emulator.handle(self.event)
        response = "Invalid query: You have an error in your SQL syntax; check the manual that corresponds to your " \
                   "MySQL server version for the right syntax to use near ''' at line 1"
        self.assertEqual(self.event.http_request.get_response(), response)

    def test_sqli_select_user(self):
        """Objective: A query with the goal to disclosure the current user.
        Input: SELECT user().
        Expected Results: Current SQL user name.
        Notes: This query is MySQL specific."""
        self.event.matched_pattern = "sqli"
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(self.event.matched_pattern)
        self.event.http_request.request_query = {
            "q": ["SELECT user()"],
        }
        self._get_test_request(self.event)
        emulator.handle(self.event)
        response = "root@localhost"
        self.assertEqual(self.event.http_request.get_response().strip(), response)

    def test_sqli_mysqld_version(self):
        """Objective: A query with the goal to disclose the MySQL server version.
        Input: SELECT @@version.
        Expected Results: The MySQL server version number.
        Notes: The query is MySQL specific."""
        self.event.matched_pattern = "sqli"
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(self.event.matched_pattern)
        self.event.http_request.request_query = {
            "q": ["SELECT @@version"],
        }
        self._get_test_request(self.event)
        emulator.handle(self.event)
        response = "5.1.49-3"
        self.assertEqual(self.event.http_request.get_response().strip(), response)

    def test_sqli_xss(self):
        """Objective: Injecting JavaScript.
        Input: '&lt;script&gt;alert("XSS");&lt;/script&gt;'
        Expected Results: MySQL syntax error message containing '&lt;script&gt;alert("XSS");&lt;/script&gt;'
        Notes: The query and identifying string is included in the error message."""
        self.event.matched_pattern = "sqli"
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(self.event.matched_pattern)
        self.event.http_request.request_query = {
            'q': ['<script>alert("XSS");</script>'],
        }
        self._get_test_request(self.event)
        emulator.handle(self.event)
        self.assertTrue('<script>alert("XSS");</script>' in self.event.http_request.get_response())


if __name__ == '__main__':
    unittest.main()
