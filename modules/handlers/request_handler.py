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

from modules.handlers.base_emulator import BaseEmulator
import logging

logger = logging.getLogger(__name__)


def get_handler(name):
    try:
        BaseEmulator()
        module_name = "modules.handlers.emulators." + name
        __import__(module_name, globals(), locals(), [], -1)
        emulators = BaseEmulator.__subclasses__()
    except ImportError as e:
        logging.exception("Error while importing emulator: {0}", e)
        return get_handler("unknown")
    else:
        for emulator in emulators:
            if emulator.__module__.rsplit(".", 1)[1].strip() == name:
                return emulator()
        return get_handler("unknown")
