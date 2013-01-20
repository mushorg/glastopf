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

import urllib
import unicodedata
import chardet
from urlparse import urlparse
import re
import logging

logger = logging.getLogger(__name__)


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
        # FIXME: Error handling for malformed HTTP requests
        #request = urllib.unquote(request)
        encoding = chardet.detect(request)
        try:
            request = unicodedata.normalize('NFKD', request.decode(encoding['encoding'])).encode('ascii')
        except:
            logger.exception("request.decode({0}) failed, fall back to decode with latin1.".format(encoding['encoding']))
            request = unicodedata.normalize('NFKD', request.decode('latin1')).encode('ascii', 'ignore')
        parsed_request = HTTPRequest()
        try:
            request, parsed_request.body = request.split("\r\n\r\n", 1)
        except ValueError:
            # TODO: Maybe this is too powerful
            pass
        request = request.split("\r\n")

        # Parse the first line
        try:
            HTTP_REQ_METHOD_RE = re.compile("^([A-Z]{3,7})")
            parsed_request.method = HTTP_REQ_METHOD_RE.match(request[0]).group(1)
        except:
            # Should return a 501 Not implemented error
            # We might want to use a default method (finger printable?)
            raise
        else:
            try:
                HTTP_REQ_PATH_RE = re.compile("^([A-Z]{3,7})\s+(.*)\s+")
                parsed_request.url = urlparse(HTTP_REQ_PATH_RE.match(request[0]).group(2)).path
                parsed_request.parameters = urlparse(HTTP_REQ_PATH_RE.match(request[0]).group(2)).query
            except:
                # Should no path be redirected to the root dir?
                raise
            else:
                try:
                    HTTP_REQ_VERSION_RE = re.compile("^([A-Z]{3,7})\s+(.*)\s+(HTTP/\d\.\d)")
                    parsed_request.version = HTTP_REQ_VERSION_RE.match(request[0]).group(3)
                except:
                    # Default to HTTP/1.1?
                    # Should return a 505  HTTP Version Not Supported
                    raise
        parsed_request.header = self.parse_header(request[1:])
        # If the request contains parameters append to url.
        # Some detection rules need to parse the whole url,
        # not only the request path
        if parsed_request.parameters:
            parsed_request.url += '?%s' % parsed_request.parameters
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
