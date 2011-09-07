import modules.HTTP.util as util
import modules.HTTP.method_handler as method_handler
import modules.events.attack as attack

def handle_request(raw_request, addr):
	HTTP_parser = util.HTTPParser()
	attack_event = attack.AttackEvent()
	parsed_request = HTTP_parser.parse_request(raw_request)
	attack_event.parsed_request = parsed_request
	attack_event.source_addr = addr
	print addr[0] + ": " + parsed_request.method, parsed_request.url, parsed_request.header["Host"]
	MethodHandlers = method_handler.HTTPMethods()
	response = util.HTTPServerResponse.response_header
	response += getattr(MethodHandlers, parsed_request.method, "GET")(parsed_request)
	return response