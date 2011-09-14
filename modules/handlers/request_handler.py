import sandbox.apd_sandbox as sandbox
import modules.handlers.emulators.rfi as rfi_emulator

def unknown(attack_event):
	response = "unknown handled"
	return response

def rfi(attack_event):
	emulator = rfi_emulator.RFIEmulator()
	file_name = emulator.download_file(attack_event.parsed_request.url)
	response = sandbox.run(file_name)
	return response