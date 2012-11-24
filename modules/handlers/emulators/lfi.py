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
# Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import re
import os

from modules.handlers import base_emulator


class LFIEmulator(base_emulator.BaseEmulator):

    def __init__(self):
        pass

    def virtualdocs_whitelist(self):
        whitelist = []
        for root, subFolders, files in os.walk('virtualdocs/'):
            if ".git" in root:
                continue
            for dir_file in files:
                whitelist.append(os.path.join(root, dir_file))
        return whitelist

    def clean_path(self, attack_event):
        return attack_event.parsed_request.url.split('\0', 1)[0]

    def file_path(self, cleaned_path):
        try:
            pattern = re.compile(r'(\.\./)*')
            result = pattern.split(cleaned_path, maxsplit=1)
            path = "virtualdocs/linux/%s" % result[2]
        except:
            path = None
        return path

    def handle(self, attack_event):
        path = self.file_path(self.clean_path(attack_event))
        try:
            if path in self.virtualdocs_whitelist():
                with open(path, "r") as f:
                    attack_event.response += f.read()
            else:
                raise IOError
        except IOError:
            # TODO: Make it not finger printable
            # Place holder file not found error
            attack_event.response += "Warning: include(vars1.php): failed to open stream: No such file or directory in /var/www/html/anonymous/test.php on line 6 Warning: include(): Failed opening 'vars1.php' for inclusion (include_path='.:/usr/share/pear:/usr/share/php') in /var/www/html/anonymous/test.php on line 6" 
