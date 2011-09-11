import sandbox.sandbox as sandbox

def unknown(attack_event):
	response = "unknown handled"
	return response

def rfi(attack_event):
	attack_event.parsed_request.url
	response = sandbox.run("sandbox/samples/id.txt")
	return response