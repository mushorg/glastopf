from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class IPProfile(Base):
    __tablename__ = 'ip_profiles'
    
    ip = Column(String, primary_key=True)
    as_number = Column(String)
    as_name = Column(String)
    country_code = Column(String)
    total_requests = Column(String)
    total_scans = Column(String)
    bgp_prefix = Column(String)
    requests_per_scan = Column(String)
    avg_scan_duration = Column(String)
    scan_time_period = Column(String)
    last_event_time = Column(String) 
       
    def __init__(
            self, ip, as_number, as_name, country_code,
            total_requests, total_scans, bgp_prefix, 
            requests_per_scan, avg_scan_duration, 
            scan_time_period, last_event_time ):
        self.ip = ip
        self.as_number = as_number
        self.as_name = as_name
        self.country_code = country_code
        self.total_requests = total_requests
        self.total_scans = total_scans
        self.bgp_prefix = bgp_prefix
        self.requests_per_scan = requests_per_scan
        self.avg_scan_duration = avg_scan_duration
        self.scan_time_period = scan_time_period
        self.last_event_time = last_event_time