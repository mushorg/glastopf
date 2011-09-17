import sandbox.apd_sandbox as sandbox
import modules.handlers.emulators.rfi as rfi_emulator
import modules.handlers.emulators.lfi as lfi_emulator

def unknown(attack_event):
	attack_event.response += "unknown handled"
	return attack_event

def rfi(attack_event):
	emulator = rfi_emulator.RFIEmulator()
	attack_event.file_name = emulator.download_file(attack_event.parsed_request.url)
	attack_event.response += sandbox.run(attack_event.file_name)
	return attack_event

def lfil(attack_event):
	emulator = lfi_emulator.LFIEmulator()
	file_contents = emulator.getContents(attack_event.parsed_request.url)
	attack_event.response += file_contents
	#attack_event.response += "lfi-linux handled"
	return attack_event

def lfiw(attack_event):
	attack_event.response += "lfi-windows handled"
	return attack_event

def sql(attack_event):
	attack_event.response += "sql handled"
	return attack_event
