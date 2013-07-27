# Copyright (C) 2011  Lukas Rist
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
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import re
import os
import urlparse
import urllib2

from xml.dom.minidom import parse

import glastopf.modules.classification.sql as sql


package_directory = os.path.dirname(os.path.abspath(__file__))


class RequestPattern(object):
    def __init__(self, pattern_id, string, description, module):
        self.id = pattern_id
        self.string = string
        self.description = description
        self.module = module


class Classifier(object):
    # FIXME: Error handling for errors in the xml file

    def __init__(self, data_dir=os.path.join(os.getcwd(), 'data')):
        # TODO: check if file exists
        #ugly but it works...
        requests_file = os.path.join(package_directory, '../../requests.xml')
        self.tree = parse(requests_file)
        self.server_files_path = os.path.join(data_dir, 'server_files')
        if not os.path.isdir(self.server_files_path):
            os.mkdir(self.server_files_path, 0770)
        self.sqli_c = sql.SQLiClassifier()

    def get_patterns(self):
        patterns = self.tree.getElementsByTagName("request")
        return patterns

    def getText(self, nodelist):
        rc = []
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE or node.nodeType == node.CDATA_SECTION_NODE:
                rc.append(node.data)
                break
        return ''.join(rc)

    def parse_pattern(self, pattern):
        pattern_id = self.getText(pattern.getElementsByTagName("id")[0].childNodes)
        pattern_string = self.getText(pattern.getElementsByTagName("patternString")[0].childNodes)
        pattern_description = pattern.getElementsByTagName("patternDescription")[0].childNodes[0].data
        pattern_module = pattern.getElementsByTagName("module")[0].childNodes[0].data
        parsed_pattern = RequestPattern(pattern_id, pattern_string,
                                        pattern_description, pattern_module)
        return parsed_pattern

    def select_pattern(self, matched_patterns):
        # TODO: add some logic
        matched_pattern = matched_patterns[0]
        if len(matched_patterns) > 1:
            if matched_patterns[0] == "unknown":
                matched_pattern = matched_patterns[1]
        else:
            matched_pattern = matched_patterns[0]
        return matched_pattern

    def file_exists(self, http_request):
        request_path = urlparse.urlparse(http_request.path).path
        requested_file = request_path.lstrip('/')
        if os.path.isfile(os.path.join(self.server_files_path, requested_file)):
            return True
        return False

    def classify_request(self, http_request):
        if self.file_exists(http_request):
            return "file_server"
        patterns = self.get_patterns()
        matched_patterns = []
        unquoted_url = urllib2.unquote(http_request.request_url)
        # SQLi early exit
        ret = self.sqli_c.classify(unquoted_url)
        if ret['sqli']:
            return "sqli"
        for pattern in patterns:
            match = None
            parsed_pattern = self.parse_pattern(pattern)
            re_pattern = re.compile(parsed_pattern.string, re.I)
            #TODO: Rules for specific method. We should add a tag in the
            # rule to identify which rule it applies.
            # And some forms would send data in GET and POST methods.
            if http_request.command == "GET":
                match = re_pattern.search(unquoted_url)
            elif http_request.command == "POST":
                match = re_pattern.search(unquoted_url)
                if match == 'unknown':
                    match = re_pattern.search(http_request.request_body)
            elif http_request.command == "HEAD":
                parsed_pattern.module = 'head'
                match = True
            elif http_request.command == "TRACE":
                parsed_pattern.module = 'trace'
                match = True
            else:
                parsed_pattern.module = 'unknown'
                match = True
            if match != None:
                matched_patterns.append(parsed_pattern.module)
        matched_pattern = self.select_pattern(matched_patterns)
        return matched_pattern
