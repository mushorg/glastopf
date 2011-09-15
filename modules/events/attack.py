from datetime import datetime

class AttackEvent(object):
	def __init__(self):
		self.parsed_request = "/"
		self.event_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		self.source_addr = None
		self.matched_pattern = "unknown"
		self.file_name = None
		self.response = None