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
import uuid


class AttackEvent(object):
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.sensor_addr = ("", "")
        self.http_request = None
        self.raw_request = None
        self.event_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.source_addr = None
        self.matched_pattern = "unknown"
        self.file_name = None

    def event_dict(self):
        event_dict = {
            "time": self.event_time,
            "source": self.source_addr,
            "request_url": self.http_request.request_url,
            "request_raw": self.http_request.request_raw,
            "pattern": self.matched_pattern,
            "filename": self.file_name,
        }
        return event_dict
