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
import hashlib
import uuid
import shutil
import os
import tempfile
import inspect

from glastopf.glastopf import GlastopfHoneypot
from glastopf.modules.handlers.request_handler import RequestHandler
import glastopf.modules.events.attack as attack
from glastopf.modules.HTTP.handler import HTTPHandler
import glastopf.modules.HTTP.method_handler as method_handler

import helpers


class TestEmulatorIntegration(unittest.TestCase):
    """Tests the honeypots request emulation modules.
    General approach is to load the module, pass a request if needed and
    compare the modules return value with an expectation"""

    def setUp(self):
        self.work_dir = tempfile.mkdtemp()
        GlastopfHoneypot.prepare_environment(self.work_dir)
        self.data_dir = os.path.join(self.work_dir, 'data/')
        package_directory = os.path.dirname(os.path.abspath(inspect.getfile(RequestHandler)))
        #original data as stored with new glatopf installations
        self.original_data_dir = os.path.join(package_directory, 'emulators/data/')

    def tearDown(self):
        if os.path.isdir(self.work_dir):
            shutil.rmtree(self.work_dir)

    def test_dummy_emulator(self):
        """Objective: Tests the dummy emulator added to prove extensibility.
        Input: http://localhost:8080/
        Expected Results: Returns a short message for verification.
        Notes: The dummy emulator fulfills minimal emulator requirements."""
        print "Starting Dummy emulator module test"
        event = attack.AttackEvent()
        event.http_request = HTTPHandler('', None)
        event.matched_pattern = "dummy"
        print "Loading module"
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(event.matched_pattern)
        print "Trying to handle an event with the dummy module"
        emulator.handle(event)
        self.assertEqual(event.http_request.get_response_body(), "dummy response")
        print "Return value: '" + event.http_request.get_response_body() + "'",
        print "equates our expectation."

    def test_lfi_emulator(self):
        """Objective: Local File Inclusion module testing.
        Input: http://localhost:8080/test.php?p=../../../../../etc/passwd
        Expected Result: The passwd file from the virtual file system.
        Notes:"""
        print "Starting local file inclusion test"
        event = attack.AttackEvent()
        event.matched_pattern = "lfi"
        event.http_request = HTTPHandler('', None)
        event.http_request.request_url = "/test.php?p=../../../../../etc/passwd"
        print "Sending request:", "http://localhost:8080" + event.http_request.request_url
        print "Loading the emulator and handling the request."
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(event.matched_pattern)
        emulator.handle(event)
        #TODO: Check it contains user names...
        response = event.http_request.get_response()
        self.assertIn('root:x:0:0:root:/root:/bin/bash', response)
        self.assertIn('daemon:x:1:1:daemon:/usr/sbin:/bin/sh', response)

    def test_pma_emulator(self):
        """Objective: Testing an emulator for PHPMyAdmin specific attacks.
        Input: http://localhost:8080/phpmyadmin
        Expected Result: The PHPMyAdmin set-up page.
        Notes: This module is for a specific attack against PHPMyAdmin"""
        with open(os.path.join(self.data_dir, 'phpmyadmin/script_setup.php'), 'r') as setup_php:
            page = setup_php.read()
            local_hash = hashlib.md5(page).hexdigest()
            print "Hash of the local 'script' file:", local_hash
        event = attack.AttackEvent()
        event.matched_pattern = "phpmyadmin"
        event.http_request = HTTPHandler('', None)
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(event.matched_pattern)
        print "Sending request:", "http://localhost:8080/phpmyadmin/setup.php"
        emulator.handle(event)
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
        print "Starting remote file inclusion test using unquoted url"
        event = attack.AttackEvent()
        url = "https://gist.githubusercontent.com/glaslos/02c4c4be39fb03b3bbee5c862cd304c6/raw/adf146469e8eeee4498874164ecd80c70ffb4e7a/test_file.txt"
        event.http_request = HTTPHandler('GET /test.php?p={} HTTP/1.0'.format(url), None)
        event.matched_pattern = "rfi"
        print "Sending request:", "http://localhost:8080" + event.http_request.path
        helpers.create_sandbox(self.data_dir)
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(event.matched_pattern)
        emulator.handle(event)
        self.assertEqual(event.http_request.get_response(), "test successful")
        print "Return value 'test successful', matching our expectation."

    def test_rfi_emulator_quoted_url(self):
        # TODO: Handle return value from sandbox
        """Objective: Remote File Injection test when attacker injects quoted url.
        Input: /test.php?p=http%3A%2F%21durch0.de%2Ftest_file.txt
        Expected Result: The return value from the PHP sandbox.
        Notes: Injected file contains <?php echo("test successful"); ?>"""
        GlastopfHoneypot.prepare_sandbox(self.work_dir)
        print "Starting remote file inclusion test using quoted url."
        event = attack.AttackEvent()
        url = "https%3A%2F%2Fgist.githubusercontent.com%2Fglaslos/02c4c4be39fb03b3bbee5c862cd304c6/raw/adf146469e8eeee4498874164ecd80c70ffb4e7a/test_file.txt"
        event.http_request = HTTPHandler('GET /test.php?p={} HTTP/1.0'.format(url), None)
        event.matched_pattern = "rfi"
        print "Sending request:", "http://localhost:8080" + event.http_request.path
        helpers.create_sandbox(self.data_dir)
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(event.matched_pattern)
        emulator.handle(event)
        self.assertEqual(event.http_request.get_response(), "test successful")
        print "Return value 'test successful', matching our expectation."

        #http%3A%2F%2Fflickr.com.blumenlendlefloral.com%2Fsh.php

    def test_rfi_emulator_with_malformed_uri(self):
        # TODO: Handle return value from sandbox
        """Objective: Remote File Injection test with malformed uri
        Input: http://localhost:8080/test.php?p="http://google.com/index.html
        Expected Result: The return value from the PHP sandbox.
        Notes: Injected file contains <?php echo("test successful"); ?>"""
        GlastopfHoneypot.prepare_sandbox(self.work_dir)
        print "Starting remote file inclusion test"
        event = attack.AttackEvent()
        url = "https://gist.githubusercontent.com/glaslos/02c4c4be39fb03b3bbee5c862cd304c6/raw/adf146469e8eeee4498874164ecd80c70ffb4e7a/test_file.txt"
        event.http_request = HTTPHandler('GET /test.php?p={} HTTP/1.0'.format(url), None)
        event.matched_pattern = "rfi"
        helpers.create_sandbox(self.data_dir)
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(event.matched_pattern)
        print "Sending request:", "http://localhost:8080" + event.http_request.path
        emulator.handle(event)
        self.assertEqual(event.http_request.get_response(), "test successful")
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
        event = attack.AttackEvent()
        event.http_request = HTTPHandler('GET /robots.txt HTTP/1.0', None)
        event.matched_pattern = "robots"
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(event.matched_pattern)
        print "Sending request:", "http://localhost:8080/robots.txt"
        emulator.handle(event)
        remote_hash = hashlib.md5(event.http_request.get_response()).hexdigest()
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
        event = attack.AttackEvent()
        event.http_request = HTTPHandler('', None)
        event.matched_pattern = "style_css"
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(event.matched_pattern)
        print "Sending request:", "http://localhost:8080/style.css"
        emulator.handle(event)
        remote_hash = hashlib.md5(event.http_request.get_response_body()).hexdigest()
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
        event = attack.AttackEvent()
        event.http_request = HTTPHandler('', None)
        event.matched_pattern = "unknown"
        event.http_request.path = "/"
        event.source_addr = ("127.0.0.1", "8080")
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(event.matched_pattern)
        print "Sending request:", "http://localhost:8080/"
        emulator.handle(event)
        remote_hash = hashlib.md5(event.http_request.get_response_body()).hexdigest()
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
        event = attack.AttackEvent()
        event.http_request = HTTPHandler('GET /index.php?-s HTTP/1.0', None)
        event.matched_pattern = "php_cgi_rce"
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(event.matched_pattern)
        emulator.handle(event)
        self.assertEquals(event.http_request.get_response(), """<code><span style="color: #000000">
<span style="color: #0000BB">&lt;?php<br />page&nbsp;</span><span style="color: #007700">=&nbsp;</span><span style="color: #0000BB">$_GET</span><span style="color: #007700">[</span><span style="color: #DD0000">'page'</span><span style="color: #007700">];<br />include(</span><span style="color: #0000BB">page</span><span style="color: #007700">);<br /></span><span style="color: #0000BB">?&gt;<br /></span>
</span>""")

    def test_phpcgi_rce_emulator(self):
        """Objective: Emulator testing for PHP CGI remote code execution CVE-2012-1823
        Input: http://localhost/-d+allow_url_include=on+-d+safe_mode=off+-d+open_basedir=off-d+auto_prepend_file=php://input POST: <?php echo("rce attempt"); ?>
        Expected Result: Remote command execution of a echo command
        Notes:"""
        GlastopfHoneypot.prepare_sandbox(self.work_dir)
        os.mkdir(os.path.join(self.data_dir, 'files/'))
        request = "POST /index.php?-d+allow_url_include=on+-d+safe_mode=off+-d+open_basedir=off-d+auto_prepend_file=php://input HTTP/1.0\r\n\r\n" \
                  '<?php echo "testing"; ?>'
        event = attack.AttackEvent()
        event.http_request = HTTPHandler(request, None)
        event.matched_pattern = "php_cgi_rce"
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(event.matched_pattern)
        emulator.handle(event)
        print "Return value:", event.http_request.get_response()
        self.assertTrue("""testing""" == event.http_request.get_response())

    def test_phpinfo_emulator(self):
        """Objective: Emulator testing for phpinfo.php requests
        Input: http://localhost/phpinfo.php
        Expected Result: Result of the phpinfo() function
        Notes:"""
        event = attack.AttackEvent()
        event.http_request = HTTPHandler('GET /info.php?param1 HTTP/1.0', None)
        event.matched_pattern = "phpinfo"
        #self.event.http_request.method = 'GET'
        #self.event.http_request.url = "/info.php?param1"
        event.matched_pattern = "phpinfo"
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(event.matched_pattern)
        emulator.handle(event)
        self.assertTrue("PHP Version " in event.http_request.get_response())
        self.assertTrue("Zend Extension" in event.http_request.get_response())

    def test_put_method(self):
        """Objective: Test handling of a PUT requests
        Input: curl -XPUT http://localhost/
        Expected Result: request verb is PUT, matcher pattern is put
        Notes:"""
        event = attack.AttackEvent()
        event.http_request = HTTPHandler('PUT / HTTP/1.0', None)
        self.assertTrue(event.http_request.request_verb == "PUT")
        method_handlers = method_handler.HTTPMethods(self.data_dir)
        event.matched_pattern = getattr(
            method_handlers,
            event.http_request.command,
            method_handlers.GET
        )(event.http_request)
        self.assertTrue(event.matched_pattern == 'put')
        request_handler = RequestHandler(self.data_dir)
        emulator = request_handler.get_handler(event.matched_pattern)
        emulator.handle(event)
        self.assertTrue('Created' in event.http_request.get_response())


if __name__ == '__main__':
    unittest.main()
