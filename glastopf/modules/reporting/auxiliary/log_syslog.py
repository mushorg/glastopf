# Copyright (C) 2012 Johnny Vestergaard <jkv@unixcluster.dk>
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

from ConfigParser import ConfigParser

from glastopf.modules.reporting.auxiliary.base_logger import BaseLogger


class LogSyslog(BaseLogger):
    def __init__(self, data_dir, config="glastopf.cfg"):
        conf_parser = ConfigParser()
        conf_parser.read(config)
        self.options = {
            "enabled": conf_parser.getboolean("syslog", "enabled"),
            "socket": conf_parser.get("syslog", "socket"),
        }

        if self.options['enabled']:
        #Make sure we only have one logger
            try:
                LogSyslog.logger
            except AttributeError:
                LogSyslog.logger = logging.getLogger('glaspot_attack')
                LogSyslog.logger.propagate = False
                LogSyslog.log_handler = logging.handlers.SysLogHandler(address=self.options['socket'])
                LogSyslog.logger.addHandler(self.log_handler)
                LogSyslog.logger.setLevel(logging.INFO)

    def insert(self, attack_event):
        message = "Glaspot: %(pattern)s attack method from %(source)s against %(host)s. [%(method)s %(url)s]" % {
            'pattern': attack_event.matched_pattern,
            'source': ':'.join((attack_event.source_addr[0], str(attack_event.source_addr[1]))),
            'host': attack_event.http_request.header.get('Host', "None"),
            'method': attack_event.http_request.method,
            'url': attack_event.http_request.url,
        }
        LogSyslog.logger.info(message)
