import modules.HTTP.util as util
import modules.HTTP.method_handler as method_handler

def handle_request(raw_request):
	Server = util.HTTPParser()
	parsed_request = Server.parse_request(raw_request)
	print parsed_request.method, parsed_request.url, parsed_request.header["Host"]
	MethodHandlers = method_handler.HTTPMethods()
	response = util.HTTPServerResponse.response_header
	response += getattr(MethodHandlers, parsed_request.method, "GET")(parsed_request)
	return response