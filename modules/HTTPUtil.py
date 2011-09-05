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
	
	def parse_request(self, request):
		"""GET /test.php HTTP/1.1\r\nHost: localhost\r\nConnection: keep-alive\r\nUser-Agent: Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.814.0 Safari/535.1\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: gzip,deflate,sdch\r\nAccept-Language: en-US,en;q=0.8\r\nAccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3\r\n\r\n"""
		request, body = request.split("\r\n\r\n")
		request = request.split("\r\n")
		request_line = request[0].split()
		request_method = request_line[0]
		request_url = request_line[1]
		request_version = request_line[2]
		request_header = request[1:] 
		parsed_request = HTTPRequest(request_method, request_url, request_version, request_header, body)
		return parsed_request
	
class HTTPServerResponse():
	response_header = "HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html; charset=UTF-8\n\n"