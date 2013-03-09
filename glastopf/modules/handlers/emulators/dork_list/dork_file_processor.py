# Copyright (C) 2013  Lukas Rist <glaslos@gmail.com>
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

import codecs
import re
import os
import unicodedata

package_directory = os.path.dirname(os.path.abspath(__file__))


class DorkFileProcessor(object):
    def __init__(self, dorkdb=None, dorks_file=os.path.join(package_directory, 'data/dorks.txt')):
        self.dorkdb = dorkdb
        self.dorks_file = dorks_file

    def get_lines(self):
        dork_lines = []
        with codecs.open(self.dorks_file, "r", "utf-8") as dork_list:
            for dork_line in dork_list.readlines():
                dork_line = dork_line.strip()
                if dork_line != "":
                    dork_lines.append(unicodedata.normalize('NFKD', dork_line).encode('ascii', 'ignore'))
        return dork_lines

    def extract_term(self, dork_line):
        if dork_line.startswith('"'):
            term = re.match('"([^"]+)"', dork_line)
            if term:
                term = term.group(1)
        elif dork_line.startswith("'"):
            term = re.match("'([^']+)'", dork_line)
            if term:
                term = term.group(1)
        else:
            term = dork_line.split(" ")[0]
        if term:
            term = term.strip()
        return term

    def parse_lines(self, dork_lines, ignores):
        search_opers = ('intitle:', 'inurl:', 'intext:', 'filetype:', 'ext:', 'allinurl:')
        inserts = []
        for dork_line in dork_lines:
            operator = next((oper for oper in search_opers if oper in dork_line), None)
            if operator != None:
                dork_line_split = dork_line.partition(operator)[2]
                table = operator[:-1]
                if table not in ignores:
                    inserts.append({'table': table, 'content': self.extract_term(dork_line_split)})
        return inserts

    def process_dorks(self, ignore=()):
        dork_lines = self.get_lines()
        return self.parse_lines(dork_lines, ignore)
