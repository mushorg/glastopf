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
import datetime

from glastopf.modules.handlers.request_handler import RequestHandler
import glastopf.modules.events.attack as attack
import glastopf.modules.HTTP.util as util


class TestSQLiEmulation(unittest.TestCase):
    """Tests the honeypots SQL injection emulation module.
    We first start with the integration test and continue with unit test"""
    def setUp(self):
        self.event = attack.AttackEvent()
        self.event.parsed_request = util.HTTPRequest()
        self.event.parsed_request.url = "/test.php"
        self.event.parsed_request.parameters_dict = {
                                                     "q": "SELECT A FROM B",
                                                     }

    def tearDown(self):
        del self.event

    def _get_test_request(self, attack_event):
        params = '&'.join(
                          ['='.join(param) for param in
                           self.event.parsed_request.parameters_dict.items()
                           ]
                          )
        self.test_request = "http://localhost:8080/test.php?" + params

    def test_sqli_lexer(self):
        """Objective: Tests the SQL injection lexer.
        Input: 'SELECT A FROM B'
        Expected Results: Query tokens 121, 237, 80, 237, 122, 237, 80
        Notes: 121 matches the SELECT, 237 the three white spaces, 80 the column and table alias and 122 the FROM"""
        print "Starting SQL injection Lexer test..."
        self.event.matched_pattern = "sqli"
        request_handler = RequestHandler()
        emulator = request_handler.get_handler(self.event.matched_pattern)
        self._get_test_request(self.event)
        print "Sending request:", self.test_request
        emulator.handle(self.event)
        #print self.event.response
        self.assertEqual(emulator.query_parser.tokens,
                         [121, 237, 80, 237, 122, 237, 80])
        print "Return value: Query tokens:",
        print "'" + ', '.join([str(t) for t in emulator.query_parser.tokens]) + "'",
        print "equates our expectation."

    def test_sqli_parser(self):
        """Objective: Tests the SQL injection parser.
        Input: 'SELECT A FROM B'
        Expected Results: Parsed tokens (SELECT (SELECT_CORE (COLUMNS (ALIAS (COLUMN_EXPRESSION A))) (FROM (ALIAS B))))
        Notes: The Parser turns the tokens into a query"""
        print "Starting SQL injection Parser test..."
        self.event.matched_pattern = "sqli"
        request_handler = RequestHandler()
        emulator = request_handler.get_handler(self.event.matched_pattern)
        self._get_test_request(self.event)
        print "Sending request:", self.test_request
        emulator.handle(self.event)
        self.assertEqual(emulator.query_parser.tree,
                         '(SELECT (SELECT_CORE (COLUMNS (ALIAS (COLUMN_EXPRESSION A))) (FROM (ALIAS B))))')
        print "Return value: Parsed tokens:",
        print '(SELECT (SELECT_CORE (COLUMNS (ALIAS (COLUMN_EXPRESSION A))) (FROM (ALIAS B))))',
        print "equates our expectation."

    def test_sqli_emulator(self):
        """Objective: Assure that the SQL injection module is integrated.
        Input: Inject 'SELECT a FROM b' in parameter q.
        Expected Results: MySQL error message.
        Notes: As there is no table b, the honeypot returns an error message."""
        print "Starting SQL injection module integration test..."
        self.event.matched_pattern = "sqli"
        request_handler = RequestHandler()
        emulator = request_handler.get_handler(self.event.matched_pattern)
        self._get_test_request(self.event)
        print "Sending request:", self.test_request
        emulator.handle(self.event)
        #print self.event.response
        response = "Invalid query: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'SELECT A FROM B' at line 1"
        self.assertEqual(self.event.response, response)
        print "Return value: Invalid query: You have an error in your SQL syntax; (truncated)",
        print "equates our expectation."

    def test_sqli_error_based(self):
        """Objective: A simple query provoking an error message from the database.
        Input: Inject a single quotation mark in parameter q.
        Expected Results: MySQL syntax error message.
        Notes: The query is included in the error message."""
        print "Starting error based SQL injection test"
        self.event.matched_pattern = "sqli"
        request_handler = RequestHandler()
        emulator = request_handler.get_handler(self.event.matched_pattern)
        self.event.parsed_request.parameters_dict = {
                                                     "q": "'",
                                                     }
        self._get_test_request(self.event)
        print "Sending request:", self.test_request
        emulator.handle(self.event)
        #print self.event.response
        response = "Invalid query: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''' at line 1"
        self.assertEqual(self.event.response, response)
        print "Return value: ", response,
        print "equates our expectation."

    def test_sqli_select_user(self):
        """Objective: A query with the goal to disclosure the current user.
        Input: SELECT user().
        Expected Results: Current SQL user name.
        Notes: This query is MySQL specific."""
        print "Starting SQL user disclosure test"
        self.event.matched_pattern = "sqli"
        request_handler = RequestHandler()
        emulator = request_handler.get_handler(self.event.matched_pattern)
        self.event.parsed_request.parameters_dict = {
                                                     "q": "SELECT user()",
                                                     }
        self._get_test_request(self.event)
        print "Sending request:", self.test_request
        emulator.handle(self.event)
        #print self.event.response
        response = "root@localhost"
        self.assertEqual(self.event.response.strip(), response)
        print "Return value: ", response,
        print "equates our expectation."

    def test_sqli_mysqld_version(self):
        """Objective: A query with the goal to disclose the MySQL server version.
        Input: SELECT @@version.
        Expected Results: The MySQL server version number.
        Notes: The query is MySQL specific."""
        print "Starting mysqld version disclosure test"
        self.event.matched_pattern = "sqli"
        request_handler = RequestHandler()
        emulator = request_handler.get_handler(self.event.matched_pattern)
        self.event.parsed_request.parameters_dict = {
                                                     "q": "SELECT @@version",
                                                     }
        self._get_test_request(self.event)
        print "Sending request:", self.test_request
        emulator.handle(self.event)
        #print self.event.response
        response = "5.1.49-3"
        self.assertEqual(self.event.response.strip(), response)
        print "Return value: ", response,
        print "equates our expectation."

    def test_error_based_concatenated(self):
        """Objective: Complex error based vulnerability probing request containing CONCAT.
        Input: ') AND (SELECT 8957 FROM(SELECT COUNT(*),CONCAT(0x3a6e676a3a,(SELECT (CASE WHEN (8957=8957) THEN 1 ELSE 0 END)),0x3a6f74633a,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a) AND (4673=4673'
        Expected Results: MySQL syntax error message containing ':ngj:1:otc:0' (the result from the CONCAT call)
        Notes: The query and identifying string is included in the error message."""
        print "Starting error based SQLMap injection test"
        self.event.matched_pattern = "sqli"
        request_handler = RequestHandler()
        emulator = request_handler.get_handler(self.event.matched_pattern)
        self.event.parsed_request.parameters_dict = {
                                                     "q": ") AND (SELECT 8957 FROM(SELECT COUNT(*),CONCAT(0x3a6e676a3a,(SELECT (CASE WHEN (8957=8957) THEN 1 ELSE 0 END)),0x3a6f74633a,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a) AND (4673=4673",
                                                     }
        self._get_test_request(self.event)
        print "Sending request:", self.test_request
        emulator.handle(self.event)
        #print self.event.response
        self.assertTrue(':ngj:1:otc:0' in self.event.response)
        print "Return value: ", self.event.response,
        print "equates our expectation."

    def test_blind_sqli(self):
        """Objective: Injecting a response delaying SQL query.
        Input: ') AND SLEEP(1) AND (4673=4673'
        Expected Results: Response is delayed by 1 second
        Notes: """
        print "Starting time based injection test"
        self.event.matched_pattern = "sqli"
        request_handler = RequestHandler()
        emulator = request_handler.get_handler(self.event.matched_pattern)
        self.event.parsed_request.parameters_dict = {
                                                     "q": ") AND SLEEP(1) AND (4673=4673",
                                                     }
        self._get_test_request(self.event)
        print "Noting time and sending request:", self.test_request
        start = datetime.datetime.now()
        emulator.handle(self.event)
        #print self.event.response
        end = datetime.datetime.now()
        duration = end - start
        self.assertTrue(duration.seconds >= 1)
        print "Response duration: ", duration,
        print "equates our expectation."

    def test_obfuscated_blind_sqli(self):
        """Objective: Injecting an obfuscated response delaying SQL query.
        Input: ')%20aND%20SLeeP(1)%20And%20(4673%3D4673'
        Expected Results: Response is delayed by 1 second
        Notes: """
        print "Starting obfuscated time based injection test"
        self.event.matched_pattern = "sqli"
        request_handler = RequestHandler()
        emulator = request_handler.get_handler(self.event.matched_pattern)
        self.event.parsed_request.parameters_dict = {
                                                     "q": ")%20aND%20SLeeP(1)%20And%20(4673%3D4673",
                                                     }
        self._get_test_request(self.event)
        print "Noting time and sending request:", self.test_request
        start = datetime.datetime.now()
        emulator.handle(self.event)
        #print self.event.response
        end = datetime.datetime.now()
        duration = end - start
        self.assertTrue(duration.seconds >= 1)
        print "Response duration: ", duration,
        print "equates our expectation."

    def test_sqli_xss(self):
        """Objective: Injecting JavaScript.
        Input: '&lt;script&gt;alert("XSS");&lt;/script&gt;'
        Expected Results: MySQL syntax error message containing '&lt;script&gt;alert("XSS");&lt;/script&gt;'
        Notes: The query and identifying string is included in the error message."""
        print "Starting error based JavaScript injection test"
        self.event.matched_pattern = "sqli"
        request_handler = RequestHandler()
        emulator = request_handler.get_handler(self.event.matched_pattern)
        self.event.parsed_request.parameters_dict = {
                                                     'q': '<script>alert("XSS");</script>',
                                                     }
        self._get_test_request(self.event)
        print "Sending request:", self.test_request
        emulator.handle(self.event)
        #print self.event.response
        self.assertTrue('<script>alert("XSS");</script>' in self.event.response)
        print "Return value: ", self.event.response,
        print "equates our expectation."
