import modules.HTTPUtil as HTTPUtil
import modules.HTTPMethodHandler as HTTPMethodHandler

class Glastopf(object):
	def __init__(self):
		pass
	
	def HandleRequest(self, d):
		Server = HTTPUtil.HTTPParser()
		parsed_request = Server.parse_request(d)
		print parsed_request.method, parsed_request.url, parsed_request.header["Host"]
		MethodHandlers = HTTPMethodHandler.HTTPMethods()
		response =HTTPUtil.HTTPServerResponse.response_header
		response += getattr(MethodHandlers, parsed_request.method, "GET")()
		return response