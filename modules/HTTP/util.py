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
