import sandbox.apd_sandbox as sandbox
import modules.handlers.emulators.rfi as rfi_emulator

def unknown(attack_event):
	attack_event.response += "unknown handled"
	return attack_event

def rfi(attack_event):
	emulator = rfi_emulator.RFIEmulator()
	attack_event.file_name = emulator.download_file(attack_event.parsed_request.url)
	attack_event.response += sandbox.run(attack_event.file_name)
	return attack_event

def lfil (attack_event):
	attack_event.response += "lfi-linux handled"
	return attack_event

def lfiw (attack_event):
	attack_event.response += "lfi-windows handled"
	return attack_event