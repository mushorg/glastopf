import modules.HTTP.util as util
import modules.HTTP.method_handler as method_handler
import modules.events.attack as attack
from modules.handlers import request_handler
import modules.reporting.log_sqlite as log_sqlite

def print_info(attack_event):
	print attack_event.event_time,
	print attack_event.source_addr[0] + " requested",
	print attack_event.parsed_request.method, 
	print attack_event.parsed_request.url, "on", 
	print attack_event.parsed_request.header["Host"]

def handle_request(raw_request, addr):
	HTTP_parser = util.HTTPParser()
	attack_event = attack.AttackEvent()
	# Parse the request
	attack_event.parsed_request = HTTP_parser.parse_request(raw_request)
	attack_event.source_addr = addr
	print_info(attack_event)
	# Start response with the server header
	# TODO: Add msg length header
	response = util.HTTPServerResponse.response_header
	MethodHandlers = method_handler.HTTPMethods()
	# Handle the HTTP request method
	matched_pattern = getattr(MethodHandlers, attack_event.parsed_request.method, "GET")(attack_event.parsed_request)
	# Handle the request with the specific vulnerability module
	response += getattr(request_handler, matched_pattern, request_handler.unknown)(attack_event)
	return response

if __name__ == "__main__":
	pass
else:
	pass