# Copyright (C) 2012  Lukas Rist
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

import os
from glastopf.modules.handlers import base_emulator
from glastopf.modules.handlers.base_emulator import package_directory


class StyleHandler(base_emulator.BaseEmulator):
    def __init__(self, data_dir):
        super(StyleHandler, self).__init__(data_dir)

    def handle(self, attack_event):
        css_file = os.path.join(self.data_dir, 'style/style.css')
        with open(css_file, 'r') as style_file:
            #attack_event.response = style_file.read()
            attack_event.http_request.set_response(style_file.read(),  headers=(('Content-type', 'text/css'),))
        return attack_event
