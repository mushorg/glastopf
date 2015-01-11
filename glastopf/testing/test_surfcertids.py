# Copyright (C) 2015 Johnny Vestergaard <jkv@unixcluster.dk>
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

from glastopf.testing import helpers
from glastopf.modules.events.attack import AttackEvent
from glastopf.modules.HTTP.handler import HTTPHandler
from glastopf.modules.reporting.auxiliary.log_surfcertids import LogSURFcertIDS


class Test_Loggers(unittest.TestCase):

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()

    def tearDown(self):
        if os.path.isdir(self.tmpdir):
            shutil.rmtree(self.tmpdir)

    def test_surfcertids(self):
        """Objective: Testing if a basic event can be transmitted using hpfriends."""

        config_file = tempfile.mkstemp()[1]
        with open(config_file, 'w') as f:
            f.writelines(helpers.gen_config(''))

        try:
            attack_event = AttackEvent()
            request = "GET /pub/WWW/TheProject.html HTTP/1.1\r\n" \
            "Host: www.evil.org\r\n" \
            "Referer: http://www.honeynet.org\r\n" \
            "User-Agent:  Mozilla 5\r\n" \
            "\r\n\r\n" \
            "GET /beer\r\n"

            attack_event.http_request = HTTPHandler(request, "1.2.3.4")
            attack_event.source_addr = ('4.3.2.1', 41022)
            logSURFcertIDS = LogSURFcertIDS(None, os.getcwd(), config_file)
            logSURFcertIDS.connection = connectionMock()
        finally:
            if os.path.isfile(config_file):
                os.remove(config_file)


class connectionMock(object):
    class cursorMock(object):
        def execute(self, sql_statement, something):
            pass

        def fetchall(self):
            return [1, 2, 3, 4]

        def close(self):
            pass

    def commit(self):
        pass

    def cursor(self):
        return self.cursorMock()


if __name__ == '__main__':
    unittest.main()
