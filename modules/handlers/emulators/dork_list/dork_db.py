# Copyright (C) 2013 Johnny Vestergaard <jkv@unixcluster.dk>
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

from datetime import datetime
import threading
import logging
import os
import json

logger = logging.getLogger(__name__)


class DorkDB(object):
    """
    Responsible for management and persistence of dorks.
    """

    def __init__(self, dorks_file="db/dorks.json", auto_save=True):
        self.lock = threading.Lock()
        self.dorks_file = dorks_file
        self.auto_save = auto_save

        self.activity_count = 0

        with self.lock:
            if os.path.isfile(dorks_file):
                #Note: stored datedatime does not get converted back to datetime
                #as they are not used by glastopf.
                with open(dorks_file) as f:
                    self.dorks = json.load(f)
            else:
                self.dorks = {}

    def save(self):
        with self.lock:
            with open(self.dorks_file, 'w') as f:
                f.write(json.dumps(self.dorks, default=self.json_default, sort_keys=True))

    def insert(self, insert_list):
        if len(insert_list) == 0:
            return
        with self.lock:
            for item in insert_list:
                operator = item['table']
                content = item['content']

                #skip empty
                if not content:
                    continue

                if not operator in self.dorks:
                    self.dorks[operator] = {}

                if not content in self.dorks[operator]:
                    self.dorks[operator][content] = {'count': 0,
                                                     'firsttime': datetime.now(),
                                                     'lasttime': datetime.now()}

                self.dorks[operator][content]['count'] += 1
                self.dorks[operator][content]['lasttime'] = datetime.now()
                self.activity_count += 1

        #dump to file
        if self.activity_count > 10 and self.auto_save:
            self.save()
            self.activity_count = 0

    def get_dork_list(self, tablename, starts_with=None):
        return_list = []
        with self.lock:
            if tablename in self.dorks:
                for content in self.dorks[tablename].keys():
                    if starts_with == None:
                            return_list.append(content)
                    else:
                        if content.startswith(starts_with):
                            return_list.append(content)

        return return_list

    def json_default(slef, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()

    def o_hook(self, what):
        print type(what)
        print what

