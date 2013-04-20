# Copyright (C) 2012  Louis Liu
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

from string import Template
import hashlib
import time

from glastopf.modules.handlers import base_emulator
import os


class PMAEmulator(base_emulator.BaseEmulator):
    def __init__(self, data_dir):
        super(PMAEmulator, self).__init__(data_dir)

    def handle(self, attack_event, time_stamp=time.time()):
        path = os.path.join(self.data_dir, 'phpmyadmin/script_setup.php')
        with open(path, 'r') as setup_php:
            self.page = setup_php.read()
        m = hashlib.md5()
        m.update("%d" % time_stamp)
        page_template = Template(self.page)
        response = page_template.substitute(
            token_value=m.hexdigest() )
        attack_event.http_request.set_response(response)
        return attack_event
