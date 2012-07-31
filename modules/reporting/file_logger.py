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

import logging.handlers


class FileLogger(object):

    def __init__(self, name,
                 log_format='%(asctime)s %(levelname)s %(message)s',
                 logfile_name="log/glastopf.log"):
        if not os.path.isfile(logfile_name):
            pass
        self.name = name
        self.logfile_name = logfile_name
        self.log_format = log_format

    def set_handler(self):
        self.log_handler = logging.handlers.TimedRotatingFileHandler(
                                                    self.logfile_name,
                                                    when="midnight",
                                                    backupCount=31)

    def set_format(self):
        # TODO: change format
        self.log_handler.setFormatter(logging.Formatter(self.log_format))

    def set_channel(self):
        self.logger = logging.getLogger(self.name)

    def set_level(self):
        self.logger.setLevel(logging.INFO)

    def log(self):
        self.set_channel()
        self.set_handler()
        self.set_format()
        self.set_level()
        self.logger.addHandler(self.log_handler)
        return self.logger
