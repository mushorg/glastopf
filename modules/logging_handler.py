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

from modules.reporting.aux.base_logger import BaseLogger
import logging

logger = logging.getLogger(__name__)


def _get_logger_names(path='modules/reporting/aux'):
    names = os.listdir(path)
    for name in reversed(names):
        if (name == 'base_logger.py' or name == 'file_logger.py'
                or name == 'hp_feed.py' or name == '.git'
                or ".pyc" in name or name == '__init__.py'):
            names.remove(name)
    return names


def get_aux_loggers(create_tables=True):
    loggers = []
    try:
        BaseLogger()
        for name in _get_logger_names():
            module_name = "modules.reporting.aux." + name.split('.', 1)[0]
            __import__(module_name, globals(), locals(), [], -1)
        logger_classes = BaseLogger.__subclasses__()
    except ImportError as e:
        logger.exception("Error while importing logger: {0}".format(e))
        return None
    else:
        for logger_class in logger_classes:
            logger_instance = logger_class(create_tables=create_tables)
            if logger_instance.options['enabled'] == 'True':
                loggers.append(logger_instance)
        return loggers
