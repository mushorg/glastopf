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

from glastopf.modules.handlers import base_emulator
import os


class TomcatManagerStatusHandler(base_emulator.BaseEmulator):
    def __init__(self, data_dir):
        super(TomcatManagerStatusHandler, self).__init__(data_dir)

    def handle(self, attack_event):
        tomcat_manager_path = os.path.join(self.data_dir, 'tomcat/manager_status.html')
        with open(tomcat_manager_path, 'r') as tomcat_manager_file:
            attack_event.http_request.set_response(tomcat_manager_file.read())
        return attack_event
