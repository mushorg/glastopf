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

class HTTPRequest(object):

	def __init__(self, method, url, version, header, body):
		self.method = method
		self.url = url
		self.version = version
		self.header = header
		self.body = body

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
	
	def parse_request(self, request):
		request, body = request.split("\r\n\r\n")
		request = request.split("\r\n")
		request_line = request[0].split()
		request_method = request_line[0]
		request_url = request_line[1]
		request_version = request_line[2]
		request_header = self.parse_header(request[1:]) 
		parsed_request = HTTPRequest(request_method, request_url, request_version, request_header, body)
		return parsed_request
	
class HTTPServerResponse():
	response_header = "HTTP/1.1 200 OK\r\nConnection: close\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n"
