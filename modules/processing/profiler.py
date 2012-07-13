import collections
import thread
import time
import datetime

from scans_table import ScansTable
from scan import Scan


class Profiler(object):
    def __init__(self):
        self.scans_table = ScansTable()
        self.events_deque = collections.deque()
        self.deque_read_interval = 30
        self.scan_threshold = 3600
        thread.start_new_thread(self.run)

    def handle_event(self, event):
        self.events_deque.appendleft()

    def update_scans(self, event):
        source_ip = event.source_addr[0].split(',')[0]
        if source_ip is None:
            return
        scan = self.scans_table.get_current_scan(source_ip)
        event_time = datetime.strptime(event.event_time, "%Y-%m-%d %H:%M:%S")
        if scan is None:
            scan = Scan(source_ip, start_time=event_time)
            self.scans_table.insert_scan(scan)
            return

        time_diff = (scan.last_event_time - event_time).total_seconds
        if time_diff > self.scan_threshold:
            self.scans_table.close_scan(source_ip)
            scan = Scan(source_ip, start_time=event_time)
            self.scans_table.insert_scan(scan)
        else:
            scan.requests += 1
            scan.last_event_time = event.event_time

    def run(self):
        while True:
            if len(self.events_deque) == 0:
                time.sleep(self.deque_read_interval)
                continue
            self.update_scans(self.events_deque.pop())
