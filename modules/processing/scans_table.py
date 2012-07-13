class ScansTable():
    def __init__(self):
        self.scans = {}

    def insert_scan(self, scan):
        if scan.source_ip not in self.scans:
            self.scan[scan.source_ip] = {}
            self.scan[scan.source_ip]['closed'] = []
        self.scans[scan.source_ip]['current'] = scan

    def get_current_scan(self, source_ip):
        if source_ip in self.scans:
            if 'current' in self.scans[source_ip]:
                return self.scans[source_ip]['current']
        return None

    def close_scan(self, source_ip):
        if source_ip in self.scans:
            if 'current' in self.scans[source_ip]:
                current = self.scans[source_ip]['current']
                self.scans[source_ip]['current'].current = False
                self.scans[source_ip]['closed'].append(current)
                del self.scans[source_ip]['current']

    def delete_closed_scans(self):
        for source_ip in self.scans:
            del self.scans[source_ip]['closed'][:]
