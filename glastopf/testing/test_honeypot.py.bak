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
import tempfile
import shutil
import os

from glastopf.glastopf import GlastopfHoneypot
from glastopf.testing import helpers
from sqlalchemy import create_engine


class TestHoneypotFunctionality(unittest.TestCase):
    """Tests the basic honeypot functionality
    Test set-up instantiates the honeypot.
    The main Test sends a request and checks the response."""

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()

    def tearDown(self):
        if os.path.isdir(self.tmpdir):
            shutil.rmtree(self.tmpdir)

    @unittest.skip('disabled until mongodb is a real database')
    def test_honeypot_mongo(self):
        """Objective: Testing overall Honeypot integration.
        Input: Loads the honeypot module with mongodb as main database.
        Expected Response: Honeypot responses with a non-empty HTTP response.
        Note: This test verifies the overall functionality."""

        conn_string = helpers.create_mongo_database(fill=True)
        config_file = tempfile.mkstemp()[1]

        with open(config_file, 'w') as f:
            f.writelines(helpers.gen_config(conn_string))

        try:
            raw_request = "GET /honeypot_test HTTP/1.1\r\nHost: honeypot\r\n\r\n"
            source_address = ["127.0.0.1", "12345"]
            sensor_address = ["1.2.3.4", "8080"]
            GlastopfHoneypot.prepare_environment(self.tmpdir)
            self.glastopf = GlastopfHoneypot(work_dir=self.tmpdir, config=config_file)
            self.glastopf.options["enabled"] = "False"
            print "Sending request: http://localhost:8080/"

            response = self.glastopf.handle_request(raw_request,
                                                    source_address,
                                                    sensor_address)
            self.assertIsNot(response, None)
        finally:
            helpers.delete_mongo_testdata(conn_string)
            if os.path.isfile(config_file):
                os.remove(config_file)

    def test_honeypot_sql(self):
        """Objective: Testing overall Honeypot integration.
        Input: Loads the honeypot module with mongodb as main database.
        Expected Response: Honeypot responses with a non-empty HTTP response.
        Note: This test verifies the overall functionality."""

        db_file = tempfile.mkstemp()[1]
        conn_string = "sqlite:///{0}".format(db_file)
        sql_engine = create_engine(conn_string)
        helpers.populate_main_sql_testdatabase(sql_engine)

        config_file = tempfile.mkstemp()[1]

        with open(config_file, 'w') as f:
            f.writelines(helpers.gen_config(conn_string))

        try:
            raw_request = "GET /honeypot_test HTTP/1.1\r\nHost: honeypot\r\n\r\n"
            source_address = ["127.0.0.1", "12345"]
            sensor_address = ["1.2.3.4", "8080"]
            GlastopfHoneypot.prepare_environment(self.tmpdir)
            self.glastopf = GlastopfHoneypot(work_dir=self.tmpdir, config=config_file)
            self.glastopf.options["enabled"] = "False"
            print "Sending request: http://localhost:8080/"
            response = self.glastopf.handle_request(raw_request,
                                                    source_address,
                                                    sensor_address)
            self.assertIsNot(response, None)
        finally:
            if os.path.isfile(config_file):
                os.remove(config_file)
            if os.path.isfile(db_file):
                os.remove(db_file)


if __name__ == '__main__':
    unittest.main()
