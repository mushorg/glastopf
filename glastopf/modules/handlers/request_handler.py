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

import logging

from glastopf.modules.handlers.base_emulator import BaseEmulator
import os


logger = logging.getLogger(__name__)


class RequestHandler:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def get_handler(self, name):
        try:
            BaseEmulator(self.data_dir)
            module_name = "glastopf.modules.handlers.emulators." + name
            __import__(module_name, globals(), locals(), [], -1)
            emulators = BaseEmulator.__subclasses__()
        except ImportError as e:
            logging.exception("Error while importing emulator: {0}: {1}".format(name, e))
            return self.get_handler("unknown")
        else:
            for emulator in emulators:
                if emulator.__module__.rsplit(".", 1)[1].strip() == name:
                    return emulator(data_dir=self.data_dir)
            return self.get_handler("unknown")
