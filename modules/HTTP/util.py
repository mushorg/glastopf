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
                        "method" : self.method,
                        "url" : self.url,
                        "parameters" : self.parameters,
                        "version" : self.version,
                        "header" : self.header,
                        "body" : self.body
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
            request = unicodedata.normalize('NFKD', request.decode(encoding['encoding'])).encode('ascii')
        except:
            print "request.decode(%s) failed, fall back to decode with latin1.\n" % encoding['encoding']   
            request = unicodedata.normalize('NFKD', request.decode('latin1')).encode('ascii', 'ignore')
        parsed_request = HTTPRequest()
        try:
            request, parsed_request.body = request.split("\r\n\r\n", 1)
        except ValueError:
            # TODO: Maybe this is to powerful
            request = request
        request = request.split("\r\n")
        request_line = request[0].split()
        parsed_request.method = request_line[0]
        parsed_request.url = request_line[1]
        parsed_request.parameters = parsed_request.url.split("?") 
        parsed_request.version = request_line[2]
        parsed_request.header = self.parse_header(request[1:]) 
        return parsed_request
    
class HTTPServerResponse():
    # TODO: Make header customizable
    response_header = "HTTP/1.1 200 OK\r\nConnection: close\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n"