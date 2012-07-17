import collections
import thread
import time
import subprocess
from datetime import datetime, timedelta
import re

from modules.processing.scans_table import ScansTable
from modules.processing.scan import Scan
from modules import logging_handler
from modules.processing.ip_profile import IPProfile


class Profiler(object):
    def __init__(self):
        self.scans_table = ScansTable()
        self.events_deque = collections.deque()
        self.deque_read_interval = 15
        self.scan_threshold = 3600
        #self.scan_threshold = 60
        self.cymru_min_timeout = 2
        self.cymru_timeout = 3
        self.profile_update_time = datetime.now() + timedelta(hours=24)
        #self.profile_update_time = datetime.now() + timedelta(minutes=1)
        self.loggers = logging_handler.get_loggers()
        thread.start_new_thread(self.run, ())

    # Reverse the IP address for querying origin.asn.cymru.com
    def reverse_ip(self, ip):
        ipreg = re.compile("([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})"
                                    "\.([0-9]{1,3})$")
        m = ipreg.match(ip)
        if m is not None:
            return (m.group(4) + "." + m.group(3) + "." + m.group(2) +
                    "." + m.group(1))

    def handle_event(self, event):
        self.events_deque.appendleft(event)

    def update_scan(self, event):
        source_ip = event.source_addr[0].split(',')[0]
        if source_ip is None:
            return
        scan = self.scans_table.get_current_scan(source_ip)
        event_time = datetime.strptime(event.event_time, "%Y-%m-%d %H:%M:%S")
        if scan is None:
            scan = Scan(source_ip, start_time=event_time)
            self.scans_table.insert_scan(scan)
            return

        time_diff = (scan.last_event_time - event_time).total_seconds()
        if time_diff > self.scan_threshold:
            self.scans_table.close_scan(source_ip)
            scan = Scan(source_ip, start_time=event_time)
            self.scans_table.insert_scan(scan)
        else:
            scan.requests += 1
            scan.last_event_time = event_time

    def fetch_as_number(self, ip_profile):
        cmd = subprocess.Popen(
                    ['dig', '+short', self.reverse_ip(ip_profile.ip) +
                    '.origin.asn.cymru.com', 'TXT'], stdout=subprocess.PIPE)
        time.sleep(self.cymru_min_timeout)
        if cmd.poll() is None:
            time.sleep(self.cymru_timeout)
            if cmd.poll() is None:
                try:
                    cmd.kill()
                except:
                    pass
                else:
                    return False
        as_info = cmd.stdout.readline()
        as_info = as_info.strip().strip('"').split('|')
        # .split()[0] is added to deal with multiple ASNs
        as_info = [word.strip().split()[0] for word in as_info]
        try:
            ip_profile.as_number = as_info[0]
            ip_profile.bgp_prefix = as_info[1]
            ip_profile.country_code = as_info[2]
        except IndexError:
            return False
        else:
            return True

    def fetch_as_name(self, ip_profile):
        cmd = subprocess.Popen(
                    ['dig', '+short', ('AS' + ip_profile.as_number +
                     '.asn.cymru.com'), 'TXT'], stdout=subprocess.PIPE)
        as_info = cmd.stdout.readline()
        time.sleep(self.cymru_min_timeout)
        if cmd.poll() is None:
            time.sleep(self.cymru_timeout)
            if cmd.poll() is None:
            try:
                cmd.kill()
            except:
                pass
            else:
                return
        as_name_info = cmd.stdout.readline()
        as_name_info = as_info.strip().strip('"').split('|')
        try:
            ip_profile.as_name = as_name_info[4].strip()
        except IndexError:
            pass

    def create_new_profile(self, source_ip):
        ip_profile = IPProfile()
        ip_profile.ip = source_ip
        if self.fetch_as_number(ip_profile):
            self.fetch_as_name(ip_profile)
        return ip_profile

    def update_profile_with_scan(self, profile, scan):
        profile.total_requests += scan.requests
        profile.total_scans += 1
        profile.requests_per_scan = (profile.total_requests /
                                     profile.total_scans)
        profile.avg_scan_duration = (
                ((profile.avg_scan_duration * (profile.total_scans - 1)) +
                 (scan.last_event_time - scan.start_time)) /
                (profile.total_scans))
        if profile.total_scans > 1:
            profile.scan_time_period = (
                ((profile.scan_time_period * (profile.total_scans - 2)) +
                (scan.start_time - profile.last_event_time)) /
                (profile.total_scans - 1))
        profile.last_event_time = scan.last_event_time

    def update_profiles(self, loggers):
        self.scans_table.close_old_scans(self.scan_threshold)
        for source_ip in self.scans_table.scans:
            ip_profile = loggers[0].get_profile(source_ip)
            if ip_profile is None:
                for logger in loggers:
                    logger.insert_profile(source_ip)
                ip_profile = self.create_new_profile(source_ip)
            for scan in self.scans_table.scans[source_ip]['closed']:
                self.update_profile_with_scan(ip_profile, scan)
            for logger in loggers:
                logger.update_profile(ip_profile)
        self.scans_table.delete_closed_scans()

    def run(self):
        while True:
            if len(self.events_deque) == 0:
                if datetime.now() > self.profile_update_time:
                    # Should change this after adding ip_profile code to other
                    # reporting modules
                    supported_loggers = []
                    for logger in self.loggers:
                        if logger.__class__.__name__ in ('LogPostgreSQL',):
                            supported_loggers.append(logger)
                    self.update_profiles(supported_loggers)
                    #self.profile_update_time += timedelta(hours=24)
                    self.profile_update_time += timedelta(minutes=2)
                time.sleep(self.deque_read_interval)
                continue
            self.update_scan(self.events_deque.pop())
