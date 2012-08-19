class Scan(object):
    def __init__(self, source_ip, start_time):
        self.source_ip = source_ip
        self.start_time = start_time
        self.last_event_time = start_time
        self.requests = 1
        self.requests_posted = 0
        self.current = True
