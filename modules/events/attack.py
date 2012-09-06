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
# Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
from datetime import datetime


class AttackEvent(object):

    def __init__(self):
        self.sensor_add = ("127.0.0.1", "8080")
        self.parsed_request = None
        self.raw_request = None
        self.event_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.source_addr = None
        self.matched_pattern = "unknown"
        self.file_name = None
        self.response = None

    def event_dict(self):
        event_dict = {
                    "time": self.event_time,
                    "source": self.source_addr,
                    "request": self.parsed_request.request_dict(),
                    "pattern": self.matched_pattern,
                    "filename": self.file_name,
                    "response": self.response
                    }
        return event_dict
