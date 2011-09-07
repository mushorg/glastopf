from datetime import datetime

class AttackEvent(object):
	def __init__(self):
		self.parsed_request = None
		self.event_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		self.source_addr = None