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
import hashlib
import uuid
import shutil
import os
import tempfile
import inspect
import helpers

from glastopf.modules.handlers.request_handler import RequestHandler
from glastopf.glastopf import GlastopfHoneypot
import glastopf.modules.events.attack as attack
import glastopf.modules.HTTP.util as util


class TestEmulatorIntegration(unittest.TestCase):
    """Tests the honeypots request emulation modules.
    General approach is to load the module, pass a request if needed and
    compare the modules return value with an expectation"""

    def setUp(self):
        self.event = attack.AttackEvent()
        self.event.parsed_request = util.HTTPRequest()
        self.work_dir = tempfile.mkdtemp()
        self.data_dir = os.path.join(self.work_dir, 'data/')
        package_directory = os.path.dirname(os.path.abspath(inspect.getfile(RequestHandler)))
        #original data as stored with new glatopf installations
        self.original_data_dir = os.path.join(package_directory, 'emulators/data/')
        #copy the data to a isolated data directory
        shutil.copytree(self.original_data_dir, self.data_dir)

    def tearDown(self):
        del self.event
        if os.path.isdir(self.work_dir):
            shutil.rmtree(self.work_dir)


    def test_dummy_emulator(self):
        """Objective: Tests the dummy emulator added to prove extensibility.
        Input: http://localhost:8080/
        Expected Results: Returns a short message for verification.
        Notes: The dummy emulator fulfills minimal emulator requirements."""
        print "Starting Dummy emulator module test"
        self.event.matched_pattern = "dummy"
        print "Loading module"
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(self.event.matched_pattern)
        print "Trying to handle an event with the dummy module"
        emulator.handle(self.event)
        self.assertEqual(self.event.response, "dummy response")
        print "Return value: '" + self.event.response + "'",
        print "equates our expectation."

    def test_favicon_emulator(self):
        # TODO: Handle existing favicon
        """Objective: Test the favicon.ico handling module.
        Input: http://localhost:8080/favicon.ico
        Expected Result: Returns a favicon for the browser if available.
        Notes: Providing a unique favicon could improve the deception."""
        print "Starting favicon module test"
        self.event.matched_pattern = "favicon_ico"
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(self.event.matched_pattern)
        print "Sending request to the module: http://localhost:8080/favicon.ico"
        self.event.parsed_request.url = "/favicon.ico"
        emulator.handle(self.event)
        with open(os.path.join(self.original_data_dir, 'favicon/favicon.ico'), 'r') as favicon:
            data = favicon.read()
            local_hash = hashlib.md5(data).hexdigest()
            print "Calculate md5 hash from local favicon file:", local_hash
            remote_hash = hashlib.md5(
                self.event.response.split('\r\n\r\n')[1]).hexdigest()
        self.assertEqual(remote_hash, local_hash)
        print "Return value", remote_hash,
        print "matched expectation."

    def test_lfi_emulator(self):
        """Objective: Local File Inclusion module testing.
        Input: http://localhost:8080/test.php?p=../../../../../etc/passwd
        Expected Result: The passwd file from the virtual file system.
        Notes:"""
        print "Starting local file inclusion test"
        with open(os.path.join(self.data_dir, "virtualdocs/linux/etc/passwd"), 'r') as passwd_file:
            passwd = passwd_file.read()
            local_hash = hashlib.md5(passwd).hexdigest()
            print "Hash of the local 'passwd' file:", local_hash
        self.event.parsed_request = util.HTTPRequest()
        self.event.parsed_request.url = "/test.php?p=../../../../../etc/passwd"
        print "Sending request:", "http://localhost:8080" + self.event.parsed_request.url
        self.event.matched_pattern = "lfi"
        self.event.response = ""
        print "Loading the emulator and handling the request."
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(self.event.matched_pattern)
        emulator.handle(self.event)
        remote_hash = hashlib.md5(self.event.response).hexdigest()
        self.assertEqual(remote_hash, local_hash)
        print "Return value:", remote_hash
        print "matched the hash of the local file."

    def test_pma_emulator(self):
        """Objective: Testing an emulator for PHPMyAdmin specific attacks.
        Input: http://localhost:8080/phpmyadmin
        Expected Result: The PHPMyAdmin set-up page.
        Notes: This module is for a specific attack against PHPMyAdmin"""
        with open(os.path.join(self.data_dir, 'phpmyadmin/script_setup.php'), 'r') as setup_php:
            page = setup_php.read()
            local_hash = hashlib.md5(page).hexdigest()
            print "Hash of the local 'script' file:", local_hash
        self.event.matched_pattern = "phpmyadmin"
        self.event.response = ""
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(self.event.matched_pattern)
        print "Sending request:", "http://localhost:8080/phpmyadmin/setup.php"
        emulator.handle(self.event)
        remote_hash = hashlib.md5(emulator.page).hexdigest()
        self.assertEqual(remote_hash, local_hash)
        print "Return value:", remote_hash
        print "matched the hash of the local file."

    def test_rfi_emulator(self):
        # TODO: Handle return value from sandbox
        """Objective: Remote File Injection test.
        Input: http://localhost:8080/test.php?p=http://google.com/index.html
        Expected Result: The return value from the PHP sandbox.
        Notes: Injected file contains <?php echo("test successful"); ?>"""
        GlastopfHoneypot.prepare_sandbox(self.work_dir)
        print "Starting remote file inclusion test"
        self.event.parsed_request = util.HTTPRequest()
        self.event.parsed_request.url = "/test.php?p=http://1durch0.de/test_file.txt"
        print "Sending request:", "http://localhost:8080" + self.event.parsed_request.url
        self.event.matched_pattern = "rfi"
        self.event.response = ""
        helpers.create_sandbox(self.data_dir)
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(self.event.matched_pattern)
        emulator.handle(self.event)
        self.assertEqual(self.event.response, "test successful")
        print "Return value 'test successful', matching our expectation."

    def test_rfi_emulator_with_malformed_uri(self):
        # TODO: Handle return value from sandbox
        """Objective: Remote File Injection test with malformed uri
        Input: http://localhost:8080/test.php?p="http://google.com/index.html
        Expected Result: The return value from the PHP sandbox.
        Notes: Injected file contains <?php echo("test successful"); ?>"""
        GlastopfHoneypot.prepare_sandbox(self.work_dir)
        print "Starting remote file inclusion test"
        self.event.parsed_request = util.HTTPRequest()
        self.event.parsed_request.url = "/test.php?p=%22http://1durch0.de/test_file.txt"
        print "Sending request:", "http://localhost:8080" + self.event.parsed_request.url
        self.event.matched_pattern = "rfi"
        self.event.response = ""
        helpers.create_sandbox(self.data_dir)
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(self.event.matched_pattern)
        emulator.handle(self.event)
        self.assertEqual(self.event.response, "test successful")
        print "Return value 'test successful', matching our expectation."
        
    def test_robots_emulator(self):
        """Objective: Test the robots.txt emulator.
        Input: http://localhost:8080/robots.txt
        Expected Response: The robots.txt page.
        Notes: The robots.txt is provided by the honeypot"""
        print "Starting robot.txt request handling module"
        with open(os.path.join(self.data_dir, 'robots/robots.txt'), 'r') as robots_file:
            robots = robots_file.read()
            local_hash = hashlib.md5(robots).hexdigest()
            print "Hash of the local 'robots' file:", local_hash
        self.event.matched_pattern = "robots"
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(self.event.matched_pattern)
        print "Sending request:", "http://localhost:8080/robots.txt"
        emulator.handle(self.event)
        remote_hash = hashlib.md5(self.event.response).hexdigest()
        self.assertEqual(remote_hash, local_hash)
        print "Return value:", remote_hash
        print "matched content of robots.txt."

    def test_style_css_emulator(self):
        """Objective: Test the style.css emulator.
        Input: http://localhost:8080/styles.css
        Expected Result: The styles.css file.
        Notes: Definitions used for the attacks surface style parameters."""
        print "Starting style.css emulator test"
        with open(os.path.join(self.data_dir, 'style/style.css'), 'r') as style_file:
            style = style_file.read()
            local_hash = hashlib.md5(style).hexdigest()
            print "Hash of the local 'style' file:", local_hash
        self.event.matched_pattern = "style_css"
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(self.event.matched_pattern)
        print "Sending request:", "http://localhost:8080/style.css"
        emulator.handle(self.event)
        remote_hash = hashlib.md5(self.event.response).hexdigest()
        self.assertEqual(remote_hash, local_hash)
        print "Return value:", remote_hash
        print "matched content of style.css."

    def test_unknown_emulator(self):
        """Objective: Emulator testing for non-malicious requests.
        Input: http://localhost:8080/
        Expected Result: One of the generated attack surfaces.
        Notes:"""

        tmp_file = os.path.join(self.data_dir, 'dork_pages', format(str(uuid.uuid4())))

        with open(tmp_file, 'w+') as f:
            f.write("tmpfile")
        print "Starting 'unknown' request emulation module"
        self.event.parsed_request = util.HTTPRequest()
        self.event.parsed_request.url = "/"
        self.event.matched_pattern = "unknown"
        self.event.response = ""
        self.event.source_addr = ("127.0.0.1", "8080")
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(self.event.matched_pattern)
        print "Sending request:", "http://localhost:8080/"
        emulator.handle(self.event)
        remote_hash = hashlib.md5(self.event.response).hexdigest()
        local_hash = hashlib.md5(emulator.template).hexdigest()
        print "Hash of the local 'response' file:", local_hash
        self.assertEqual(remote_hash, local_hash)
        print "Return value:", remote_hash
        print "matched a generated attack surface item."


    def test_phpcgi_source_code_disclosure_emulator(self):
        """Objective: Emulator testing for PHP CGI source code disclosure CVE-2012-1823
        Input: http://localhost:8080/index.php?-s
        Expected Result: Source code disclosure
        Notes:"""
        self.event.parsed_request = util.HTTPRequest()
        self.event.parsed_request.url = "/index.php"
        self.event.parsed_request.parameters = "-s"
        self.event.matched_pattern = "php_cgi_rce"
        self.event.response = ""
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(self.event.matched_pattern)
        emulator.handle(self.event)
        self.assertEquals(self.event.response, """<code><span style="color: #000000">
<span style="color: #0000BB">&lt;?php<br />page&nbsp;</span><span style="color: #007700">=&nbsp;</span><span style="color: #0000BB">$_GET</span><span style="color: #007700">[</span><span style="color: #DD0000">'page'</span><span style="color: #007700">];<br />include(</span><span style="color: #0000BB">page</span><span style="color: #007700">);<br /></span><span style="color: #0000BB">?&gt;<br /></span>
</span>""")

    def test_phpcgi_rce_emulator(self):
        """Objective: Emulator testing for PHP CGI remote code execution CVE-2012-1823
        Input: http://localhost/-d+allow_url_include=on+-d+safe_mode=off+-d+open_basedir=off-d+auto_prepend_file=php://input POST: <?php echo("rce attempt"); ?>
        Expected Result: Remote command execution of a echo command
        Notes:"""
        GlastopfHoneypot.prepare_sandbox(self.work_dir)
        os.mkdir(os.path.join(self.data_dir, 'files/'))
        self.event.parsed_request = util.HTTPRequest()
        self.event.parsed_request.method = 'POST'
        self.event.parsed_request.url = "/index.php"
        self.event.parsed_request.parameters = "-d+allow_url_include=on+-d+safe_mode=off+-d+open_basedir=off-d+auto_prepend_file=php://input"
        self.event.matched_pattern = "php_cgi_rce"
        self.event.parsed_request.body = '<?php echo "testing"; ?>'
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(self.event.matched_pattern)
        emulator.handle(self.event)
        print "Return value:", self.event.response
        self.assertTrue("""testing""" == self.event.response)


    def test_phpinfo_emulator(self):
        """Objective: Emulator testing for phpinfo.php requests
        Input: http://localhost/phpinfo.php
        Expected Result: Result of the phpinfo() function
        Notes:"""
        self.event.parsed_request = util.HTTPRequest()
        self.event.parsed_request.method = 'GET'
        self.event.parsed_request.url = "/info.php?param1"
        self.event.matched_pattern = "phpinfo"
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(self.event.matched_pattern)
        emulator.handle(self.event)
        self.assertTrue("PHP Version " in self.event.response)
        self.assertTrue("Zend Extension" in self.event.response)
        
    def test_files(self):
        v_files=('shadow', 'passwd', 'group' )
	    f_dir1	= "/tmp/test1/"
	    f_dir2	= "/tmp/test2/"
	    os.makedirs(f_dir1)
	    os.makedirs(f_dir2)

	    GlastopfHoneypot.randomize_vdocs(f_dir1)
        GlastopfHoneypot.randomize_vdocs(f_dir2)
	    for v_file in v_files:
        	    dat_1 = open(os.path.join(f_dir1, "linux/etc/shadow"), 'r').read()
        	    dat_2 = open(os.path.join(f_dir2, "linux/etc/passwd"), 'r').read()
		        md5_1 = hashlib.md5(dat_1).hexdigest()
		        md5_2 = hashlib.md5(dat_2).hexdigest()
		        self.assertNotEqual(md5_1,md5_2)
	    shutil.rmtree(f_dir1)
	    shutil.rmtree(f_dir2)
