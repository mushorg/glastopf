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


import hashlib
import os
from glastopf.modules.handlers import base_emulator

import glastopf.sandbox.sandbox as sandbox


class PHPCGIRCE(base_emulator.BaseEmulator):
    """
    Emulator for the PHP Remote code execution CVE-2012-1823

    Source disclosure:
    "GET /?-s HTTP/1.1"
    "GET /?-w HTTP/1.1"
    "GET /?-s+%3d HTTP/1.1"
    "GET /?-w+%3d HTTP/1.1"

    Code Execution
    "GET /?-d+auto_prepend_file=http://REMOTE_INCLUDE HTTP/1.1"
    "POST /-d+allow_url_include=on+-d+safe_mode=off+-d+open_basedir=off-d+auto_prepend_file=php://input HTTP/1.0

    <?php payload ?>
    "

    """

    def __init__(self, data_dir):
        super(PHPCGIRCE, self).__init__(data_dir)
        self.files_dir = os.path.join(self.data_dir, 'files/')
        if not os.path.exists(self.files_dir):
            os.mkdir(self.files_dir)

    # TODO duplicate code from rfi.py, refactor it
    def get_filename(self, php_code):
        file_name = hashlib.md5(php_code).hexdigest()
        return file_name

    def store_file(self, php_code):
        file_name = self.get_filename(php_code)
        if not os.path.exists(os.path.join(self.files_dir, file_name)):
            with open(os.path.join(self.files_dir, file_name), 'w+') as local_file:
                local_file.write(php_code)
        return file_name

    def handle(self, attack_event):

        php_source_code_s = """<code><span style="color: #000000">
<span style="color: #0000BB">&lt;?php<br />page&nbsp;</span><span style="color: #007700">=&nbsp;</span><span style="color: #0000BB">$_GET</span><span style="color: #007700">[</span><span style="color: #DD0000">'page'</span><span style="color: #007700">];<br />include(</span><span style="color: #0000BB">page</span><span style="color: #007700">);<br /></span><span style="color: #0000BB">?&gt;<br /></span>
</span>"""

        php_source_code_w = """<?php
page = $_GET['page']; include(page); ?>"""

        query_dict = attack_event.http_request.request_query
        url = attack_event.http_request.request_url

        # php -h
        #   -s   Output HTML syntax highlighted source.
        #   -w   Output source with stripped comments and whitespace.
        if '-s' in query_dict or '-s+%3d' in query_dict:
            attack_event.http_request.set_raw_response(php_source_code_s)
            return attack_event

        if '-w' in query_dict or '-w+%3d' in query_dict:
            attack_event.http_request.set_raw_response(php_source_code_w)
            return attack_event

        # Handle remote code execution
        if attack_event.http_request.request_verb == "POST" and \
           "auto_prepend_file=php://input" in url and \
           '-d' in url:
            print 'good stuff'
            # Read the PHP POST payload calculate the md5 checksum and save the file
            # Then call the PHP sandbox and return the expected results
            # TODO verify if it's a valid PHP code?
            php_file_name = self.store_file(attack_event.http_request.request_body)
            response = sandbox.run(php_file_name, self.data_dir)
            print '---'
            print response
            attack_event.http_request.set_raw_response(response)
            print '---'
            return attack_event

        # fallback to display vulnerable source code
        attack_event.http_request.set_raw_response(php_source_code_w)
        return attack_event
