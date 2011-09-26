# Copyright (C) 2011  Lukas Rist
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

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
            print "Failed to fetch injected file, I/O error:", error
            file_name = "sandbox/samples/id.txt"
        else:
            file_name = self.store_file(file)
        return file_name