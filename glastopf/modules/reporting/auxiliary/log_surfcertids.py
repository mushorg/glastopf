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

from glastopf.modules.reporting.auxiliary.base_logger import BaseLogger


logger = logging.getLogger(__name__)


class LogSURFcertIDS(BaseLogger):
    """
    This is the SURFcert IDS reporting class for Glastopf v3.
    This class allows your Glastopf honeypot to log attacks to a
    SURFcert IDS logserver. For more information on SURFcert IDS
    visit http://ids.surfnet.nl/ or join the #surfnetids IRC
    channel at Freenode.

    To use this module, put this file (log_surcertids.py) in the
    modules/reporting directory of your Glastopf instance. Then
    add the following part to glastopf.cfg (customize the values
    to your own needs):

    [surfcertids]
    enabled = True
    host = 10.1.2.3
    port = 5432
    user = my_db_user
    password = my_db_password
    database = idsserver

    If you haven't done yet, you need to load the file
    dionaea.sql (shipped with the SURFcert IDS logserver) into
    your database first. This file contains all required tables
    and stored procedures for Dionaea, Kippo, Glastopf, etc...

    Finally, (re)start Glastopf and enjoy.

    ernestje

    """

    def __init__(self, data_dir, config="glastopf.cfg"):
        BaseLogger.__init__(self, config)
        self.options = {
            "enabled": self.config.getboolean("surfcertids", "enabled"),
            "host": self.config.get("surfcertids", "host"),
            "port": self.config.getint("surfcertids", "port"),
            "user": self.config.get("surfcertids", "user"),
            "password": self.config.get("surfcertids", "password"),
            "database": self.config.get("surfcertids", "database"),
            "atype": 3,
            "ptype_request": 60,
            "ptype_referer": 61,
            "ptype_useragent": 62,
            "ptype_host": 63,
            "ptype_pattern": 64,
        }
        if self.options['enabled']:
            try:
                import psycopg2

                self.connection = psycopg2.connect(
                    "host=%s port=%s user=%s password=%s dbname=%s" % (
                        self.options['host'],
                        self.options['port'],
                        self.options['user'],
                        self.options['password'],
                        self.options['database'],
                    )
                )
                logger.info("Connected to the SURFcert IDS logserver.")
            except Exception as e:
                logger.exception("Unable to connect to the SURFcert IDS logserver: {0}".format(e))
                self.options['enabled'] = False

    def insert(self, attack_event):
        """
        Inserts an attack into the SURFcert IDS database, using the
        stored procedures originally made for Dionaea.
        """
        if attack_event.matched_pattern == 'unknown':
            severity = 0
        elif attack_event.matched_pattern == 'robots_txt':
            severity = 0
        elif attack_event.matched_pattern == 'style_css':
            severity = 0
        else:
            severity = 1
        try:
            cursor = self.connection.cursor()
        # TODO: reconnect if there is no connection
        except Exception as e:
            logger.error("Connection error : {0}".format(e))
            return
        cursor.execute("""
            SELECT surfids3_attack_add(%s, %s, %s, %s, %s, NULL, %s);
            """,
                       (
                           severity,
                           str(attack_event.source_addr[0]),
                           str(attack_event.source_addr[1]),
                           str(attack_event.sensor_addr[0]),
                           str(attack_event.sensor_addr[1]),
                           self.options["atype"]
                       )
        )
        attackid = cursor.fetchall()[0]
        if attackid > 0:
            cursor.execute("""
                SELECT surfids3_detail_add(%s, %s, %s, %s);
                """,
                           (
                               attackid,
                               str(attack_event.sensor_addr[0]),
                               self.options["ptype_request"],
                               attack_event.http_request.request_url
                           )
            )
            cursor.execute("""
                SELECT surfids3_detail_add(%s, %s, %s, %s);
                """,
                           (
                               attackid,
                               str(attack_event.sensor_addr[0]),
                               self.options["ptype_referer"],
                               attack_event.http_request.request_headers.get('Referer', 'None')
                           )
            )
            cursor.execute("""
                SELECT surfids3_detail_add(%s, %s, %s, %s);
                """,
                           (
                               attackid,
                               str(attack_event.sensor_addr[0]),
                               self.options["ptype_useragent"],
                               attack_event.http_request.request_headers.get('User-Agent', 'None')
                           )
            )
            cursor.execute("""
                SELECT surfids3_detail_add(%s, %s, %s, %s);
                """,
                           (
                               attackid,
                               str(attack_event.sensor_addr[0]),
                               self.options["ptype_host"],
                               attack_event.http_request.request_headers.get('Host', 'None')
                           )
            )
            cursor.execute("""
                SELECT surfids3_detail_add(%s, %s, %s, %s);
                """,
                           (
                               attackid,
                               str(attack_event.sensor_addr[0]),
                               self.options["ptype_pattern"],
                               attack_event.matched_pattern
                           )
            )
        self.connection.commit()
        cursor.close()

    def close(self):
        if self.connection:
            self.connection.close()
