import urllib2
import hashlib
import os
import re

class RFIEmulator(object):
    def __init__(self):
        pass
    
    def extract_url(self, url):
        protocol_pattern = re.compile("=(ht|f)tps?", re.IGNORECASE)
        matched_protocol = protocol_pattern.search(url).group(0)
        injected_url = matched_protocol + url.partition(matched_protocol)[2].split("?")[0]
        return injected_url.strip("=")
    
    def store_file(self, file):
        file_name = self.get_filename(file)
        if not os.path.exists("files/" + file_name):
            local_file = open("files/" + file_name, 'w+')
            for line in file.split("\n"):
                local_file.write(line)
            local_file.close()
        return file_name
    
    def get_filename(self, file):
        file_name = hashlib.md5(file).hexdigest()
        return file_name
    
    def download_file(self, url):
        injectd_url = self.extract_url(url)
        try:
            req = urllib2.Request(injectd_url)
            file = urllib2.urlopen(req).read()
        except IOError, error:
            print "Failed to fetch injected file, I/O error: %s" % error.reason
            file_name = "sandbox/samples/id.txt"
        else:
            file_name = self.store_file(file)
        return file_name