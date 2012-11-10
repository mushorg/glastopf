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

import urllib
import unicodedata
import chardet
from urlparse import urlparse
import re


class HTTPRequest(object):

    def __init__(self):
        self.method = "GET"
        self.url = "/"
        self.parameters = ""
        self.version = "HTTP/1.1"
        self.header = ""
        self.body = ""

    def request_dict(self):
        request_dict = {
                        "method": self.method,
                        "url": self.url,
                        "parameters": self.parameters,
                        "version": self.version,
                        "header": self.header,
                        "body": self.body
                        }
        return request_dict


class HTTPParser(object):

    def __init__(self, ):
        pass

    def parse_header(self, header_list):
        header_dict = {}
        for header_item in header_list:
            item_parts = header_item.split(":", 1)
            if len(item_parts) > 1 and item_parts[0].strip() != "":
                key, value = item_parts
                header_dict[key] = value.strip()
            else:
                continue
        return header_dict
    # TODO: add body parser function

    def parse_request(self, request):        
        # FIXME: Error handling for mal formed HTTP requests
        request = urllib.unquote(request)
        encoding = chardet.detect(request)
        try:
            request = unicodedata.normalize('NFKD',
                        request.decode(encoding['encoding'])).encode('ascii')
        except:
            print "request.decode(%s) failed, fall back to decode with latin1.\n" % encoding['encoding']   
            request = unicodedata.normalize('NFKD',
                        request.decode('latin1')).encode('ascii', 'ignore')
        parsed_request = HTTPRequest()
        try:
            request, parsed_request.body = request.split("\r\n\r\n", 1)
        except ValueError:
            # TODO: Maybe this is too powerful
            pass
        request = request.split("\r\n")

        # Parse the first line
        HTTP_REQ_RE = re.compile("([A-Z0-9$-_.]{3,10})\s+(.*)\s+(HTTP/\d+.\d+)")
        re_grp = HTTP_REQ_RE.match(request[0])

        # TODO Handle invalid requests. 
        # Improve a better error handling
        parsed_request.method = re_grp.group(1)
        parsed_request.url = urlparse(re_grp.group(2)).path
        parsed_request.parameters = urlparse(re_grp.group(2)).query
        parsed_request.version = re_grp.group(3)
        parsed_request.header = self.parse_header(request[1:])
        return parsed_request


class HTTPServerResponse():
    # TODO: Make header customizable
    def __init__(self):
        self.response_header = {
                                "status_line": "HTTP/1.1 200 OK\r\n",
                                "connection": "Connection: close\r\n",
                                "content_length": "Content-Length: ",
                                "content_type": "Content-Type: text/html; charset=UTF-8\r\n\r\n",
                            }
        self.trace_header = (
                         "HTTP/1.1 200 OK \r\n"
                         "Connection: close\r\n"
                         "Content-Type: message/http\r\n\r\n")

    def get_header(self, attack_event):
        if attack_event.parsed_request.method.lower() == 'trace':
            return self.trace_header
        else:
            header = self.response_header["status_line"]
            header += self.response_header["connection"]
            header += self.response_header["content_length"]
            header += str(len(attack_event.response)) + "\r\n"
            header += self.response_header["content_type"]
        return header
