# Copyright (C) 2011  Jeremy Heng
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

import re

class LFIEmulator(object):
    def __init__(self):
        pass
    
    def getVirtualPath(self, injected_path):
        """
        Sanitises and simulates a file path with a virtual root of the corresponding virtualdocs directory.
        """
        
    def getContents(self, injected_path):
        preg = re.compile(r'/.*\?.*=(.*)&?')
        result = preg.match(injected_path)
        file_path = "virtualdocs/linux/%s" % result.group(1)
        read_data = ""
        try:
            with open(file_path, "r") as f:
                read_data = f.read()
        except IOError:
            # Placeholder file not found error
            read_data = "Warning: include(vars1.php): failed to open stream: No such file or directory in /var/www/html/anonymous/test.php on line 6 Warning: include(): Failed opening 'vars1.php' for inclusion (include_path='.:/usr/share/pear:/usr/share/php') in /var/www/html/anonymous/test.php on line 6" 
        return read_data