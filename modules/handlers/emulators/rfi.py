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
        # FIXME: Check if the extracted url is actually a url
        injected_url = matched_protocol + url.partition(matched_protocol)[2].split("?")[0]
        return injected_url.strip("=")
    
    def store_file(self, injected_file):
        cleaned_injected_file = ""
        for line in injected_file.split("\n"):
            line = re.sub(r'(\r\n)|\r', r'\r\n', line)
            cleaned_injected_file = cleaned_injected_file + line + '\r\n'
        file_name = self.get_filename(cleaned_injected_file)
        if not os.path.exists("files/" + file_name):
            with open("files/" + file_name, 'w+') as local_file:
                for line in cleaned_injected_file:
                    local_file.write(line)
        return file_name
    
    def get_filename(self, injected_file):
        file_name = hashlib.md5(injected_file).hexdigest()
        return file_name
    
    def download_file(self, url):
        injectd_url = self.extract_url(url)
        try:
            req = urllib2.Request(injectd_url)
            # FIXME: We need a timeout on read here
            injected_file = unicode(urllib2.urlopen(req).read()).encode('utf-8')
        except IOError, error:
            print "Failed to fetch injected file, I/O error:", error
            file_name = "id.txt"
        else:
            file_name = self.store_file(injected_file)
        return file_name