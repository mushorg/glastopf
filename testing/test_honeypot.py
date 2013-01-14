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
import tempfile
import os
import uuid
from pymongo import MongoClient
import bson


class FakeCon(object):

    def __init__(self):
        self.sock = None


class TestHoneypotFunctionality(unittest.TestCase):
    """Tests the basic honeypot functionality
    Test set-up instantiates the honeypot.
    The main Test sends a request and checks the response."""

    @classmethod
    def setUpClass(cls):
        if not os.path.isdir('db'):
            os.mkdir('db')

        #name for temporary mongo db
        cls.db_name = 'glastopf-test-{0}'.format(str(uuid.uuid4())[0:10])
        c = MongoClient('localhost', 27017)

        #read and insert test data into mongodb instance
        data = open('testing/data/events_500.bson', 'r').read()
        for item in bson.decode_all(data):
            del item['_id']
            c[cls.db_name].events.insert(item)

        #Write a isolated glastopf configuration file
        cls.fake_config_mongo = tempfile.mkstemp()[1]
        with open(cls.fake_config_mongo, 'w') as f:
            f.writelines(cls.gen_config(mongodb=cls.db_name))

    #TODO: Move this functionality to helper class
    @classmethod
    def gen_config(cls, mongodb=None, sql_connectionstring=None):
        """
        Generates config string.
        """
        return ["[sql]\n",
                "enabled = {0}\n".format(True if sql_connectionstring else False),
                "connection_string = {0}\n".format(sql_connectionstring),
                "[dork-db]\n",
                "enabled = True\n",
                "pattern = rfi\n",
                "token_pattern = /\w+\n",
                "n_clusters = 10\n",
                "max_iter = 10\n",
                "n_init = 2\n",
                "[mongodb]\n",
                "enabled = {0}\n".format(True if mongodb else False),
                "host = localhost\n",
                "port = 27017\n",
                "user = a\n",
                "password = b\n",
                "database = {0}\n".format(mongodb),
                "collection = events\n",
                "[surfcertids]\n",
                "enabled = False\n",
                "host = localhost\n",
                "port = 5432\n",
                "user =\n",
                "password =\n",
                "database = idsserver\n",
                "[syslog]\n",
                "enabled = False\n",
                "socket = /dev/log\n",
                "[mail]\n",
                "enabled = False\n",
                "patterns = rfi,lfi\n",
                "user =\n",
                "pwd =\n",
                "mail_from =\n",
                "mail_to =\n",
                "smtp_host = smtp.gmail.com\n",
                "smtp_port = 587\n",
                "[hpfeed]\n",
                "enabled = True\n",
                "host = hpfeeds.honeycloud.net\n",
                "port = 10000\n",
                "secret = 3wis3l2u5l7r3cew\n",
                "chan = glastopf.events,glastopf.files\n",
                "ident = x8yer@hp1\n",
                "[webserver]\n",
                "host = 0.0.0.0\n",
                "port = 8080\n",
                "uid = nobody\n",
                "gid = nogroup\n",
                "proxy_enabled = False\n",
                ]

    def test_honeypot(self):
        """Objective: Testing overall Honeypot integration.
        Input: Loads the honeypot module.
        Expected Response: Honeypot responses with a non-empty HTTP response.
        Note: This test verifies the overall functionality."""
        raw_request = "GET /honeypot_test HTTP/1.1\r\nHost: honeypot\r\n\r\n"
        source_address = ["127.0.0.1", "12345"]
        self.glastopf = glastopf.GlastopfHoneypot(test=True, config=TestHoneypotFunctionality.fake_config_mongo)
        self.glastopf.options["enabled"] = "False"
        print "Sending request: http://localhost:8080/"
        connection = FakeCon()
        connection.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        response = self.glastopf.handle_request(raw_request,
                                                source_address,
                                                connection)
        connection.sock.close()
        self.assertIsNot(response, None)
        #print "Non-empty return value equates our expectation."
