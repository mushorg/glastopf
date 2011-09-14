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
        filename = self.get_filename(file)
        if not os.path.exists("files/" + filename):
            local_file = open("files/" + filename, 'w+')
            for line in file.split("\n"):
                print "line", line
                local_file.write(line)
            local_file.close()
    
    def get_filename(self, file):
        filename = hashlib.md5(file).hexdigest()
        return filename
    
    def download_file(self, url):
        injectd_url = self.extract_url(url)
        print injectd_url
        try:
            req = urllib2.Request(injectd_url)
            file = urllib2.urlopen(req).read()
            print file
        except IOError, e:
            print e
            f = open("sandbox/samples/id.txt")
            file = f.read()
            f.close()
            file = None
        else:
            self.store_file(file)
        return file