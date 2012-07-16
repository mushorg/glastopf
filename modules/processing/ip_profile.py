class IPProfile(object):
    def __init__(self):
        self.ip = None
        self.as_number = None
        self.as_name = None
        self.country_code = None
        self.total_requests = 0
        self.total_scans = 0
        self.bgp_prefix = None
        self.requests_per_scan = None
        self.avg_scan_duration = 0
        self.scan_time_period = 0
        self.last_event_time = None
