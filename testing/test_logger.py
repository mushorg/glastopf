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
import os

import modules.reporting.file_logger as file_logger


class TestFileLogger(unittest.TestCase):
    """Tests the file loggers functionality.
    Test set-up takes care of log file handling and instantiating."""
    def setUp(self):
        self.file_path = "log/test.log"
        if os.path.isfile(self.file_path):
            os.remove(self.file_path)
        else:
            with open(self.file_path, 'w') as log_file:
                pass
        self.log = file_logger.FileLogger(name="test_logger",
                                          log_format='%(message)s',
                                          logfile_name=self.file_path).log()
        print "Test log file generated."

    def tearDown(self):
        if os.path.isfile(self.file_path):
            os.remove(self.file_path)
        print "Test log file deleted."

    def test_file_logging(self):
        """Objective: Tests the file logging feature.
        Input: Write 'test' into the log file.
        Expected Event: Entry 'test' in the temporary log file.
        Notes: We create a special test file so we don't interfere with productive logs."""
        print "Starting log file test"
        print "Writing test log entry"
        self.log.info("test")
        with open(self.file_path) as log_file:
            self.assertEqual(log_file.read(), "test\n")
        print "Expected log entry 'test\\n' found in test log file."

    def test_syslog_logging(self):
        # TODO: Implement
        pass
