from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class IPProfile(Base):
    __tablename__ = 'ip_profiles'
    
    ip = Column(String, primary_key=True)
    as_number = Column(String)
    as_name = Column(String)
    country_code = Column(String)
    total_requests = Column(Integer)
    total_scans = Column(Integer)
    bgp_prefix = Column(String)
    requests_per_scan = Column(Float)
    avg_scan_duration = Column(Float)
    scan_time_period = Column(Float)
    last_event_time = Column(String) 
       
    def __init__(
            self, ip=None, as_number=None, as_name=None,
            country_code=None, total_requests=0,
            total_scans=0, bgp_prefix=None,
            requests_per_scan=None, avg_scan_duration=1, 
            scan_time_period=1, last_event_time=None):
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
