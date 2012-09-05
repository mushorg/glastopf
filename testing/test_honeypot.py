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

import socket
import glastopf


class FakeCon(object):

    def __init__(self):
        self.sock = None


class TestHoneypotFunctionality(unittest.TestCase):
    """Tests the basic honeypot functionality
    Test set-up instantiates the honeypot.
    The main Test sends a request and checks the response."""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_honeypot(self):
        """Objective: Testing overall Honeypot integration.
        Input: Loads the honeypot module.
        Expected Response: Honeypot responses with a non-empty HTTP response.
        Note: This test verifies the overall functionality."""
        raw_request = "GET /honeypot_test HTTP/1.1\r\nHost: honeypot\r\n\r\n"
        source_address = ["127.0.0.1", "12345"]
        self.glastopf = glastopf.GlastopfHoneypot()
        self.glastopf.options["enabled"] = "False"
        print "Sending request: http://localhost:8080/"
        connection = FakeCon()
        connection.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        response = self.glastopf.handle_request(raw_request,
                                                source_address,
                                                connection)
        self.assertIsNot(response, None)
        #print "Non-empty return value equates our expectation."
