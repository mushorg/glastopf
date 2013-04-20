# Copyright (C) 2012  Phani Vadrevu
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


class FileServer(base_emulator.BaseEmulator):
    def __init__(self, data_dir):
        super(FileServer, self).__init__(data_dir)

    def handle(self, attack_event):
        server_path = os.path.join(self.data_dir, 'server_files')
        request_file = attack_event.http_request.request_path.lstrip('/')
        if request_file == "":
            request_file = "index.html"
        response = ''
        if os.path.isfile(os.path.join(server_path, request_file)):
            with open(os.path.join(server_path, request_file), 'r') as f:
                response += f.read()
        #response with no content-type header
        attack_event.http_request.set_response(response, headers=())
