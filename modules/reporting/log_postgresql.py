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

import json

from ConfigParser import ConfigParser

from modules.reporting.base_logger import BaseLogger
from modules.processing.ip_profile import IPProfile

try:
    import psycopg2
    import psycopg2.extras

except ImportError as e:
    import_error = e
else:
    import_error = None


class LogPostgreSQL(BaseLogger):

    def __init__(self, config="glastopf.cfg"):
        conf_parser = ConfigParser()
        conf_parser.read(config)
        self.options = {
            "enabled": conf_parser.get("postgresql", "enabled"),
            "host": conf_parser.get("postgresql", "host"),
            "port": conf_parser.getint("postgresql", "port"),
            "user": conf_parser.get("postgresql", "user"),
            "password": conf_parser.get("postgresql", "password"),
            "database": conf_parser.get("postgresql", "database"),
            }
        if self.options['enabled'] == 'True' and import_error:
            print "Unable to connect to PostgreSQL service:", import_error
            self.options['enabled'] = 'False'
        if self.options['enabled'] == 'True':
            try:
                self.connection = psycopg2.connect("dbname=%s user=%s "
                                           "password =%s" %
                                           (
                                            self.options['database'],
                                            self.options['user'],
                                            self.options['password']
                                            )
                                           )
            except Exception as e:
                print "Unable to connect to PostgreSQL service:", e
                self.options['enabled'] = 'False'
            else:
                self.create()
                self.create_profiles_table()
        else:
            return None

    def create(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                       CREATE TABLE events(
                       id serial PRIMARY KEY,
                       timestamp TIMESTAMP,
                       source_ip INET,
                       source_port INT,
                       method VARCHAR(7),
                       request VARCHAR,
                       request_body VARCHAR,
                       header VARCHAR,
                       module VARCHAR(23),
                       filename VARCHAR(32),
                       host VARCHAR(255))
                       """)
        except psycopg2.ProgrammingError as e:
            print "Exception in creating events table:", e
        self.connection.commit()

    def create_profiles_table(self):
        cursor = self.connection.cursor()
        try:
                cursor.execute("""
                        CREATE TABLE ip_profiles(
                        ip VARCHAR(15) PRIMARY KEY,
                        as_number INT,
                        as_name VARCHAR,
                        country_code VARCHAR(2),
                        bgp_prefix INET,
                        total_scans INT DEFAULT 0,
                        total_requests INT DEFAULT 0,
                        requests_per_scan FLOAT,
                        avg_scan_duration INTERVAL DEFAULT '0',
                        scan_time_period INTERVAL DEFAULT '0',
                        last_event_time TIMESTAMP)
                    """)
        except psycopg2.ProgrammingError as e:
            print "Exception in creating ip_profiles table:", e
        self.connection.commit()

    def insert(self, attack_event):
        cursor = self.connection.cursor()
        # Use the first IP as there could be multiple IP addresses
        attack_event.source_addr = (attack_event.source_addr[0].split(',')[0],
                                    attack_event.source_addr[1])
        cursor.execute("""
            INSERT INTO events(timestamp, source_ip, source_port, method,
            request, request_body, header, module, filename, host)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
            attack_event.event_time,
            attack_event.source_addr[0],
            attack_event.source_addr[1],
            attack_event.parsed_request.method,
            attack_event.parsed_request.url,
            attack_event.parsed_request.body,
            json.dumps(attack_event.parsed_request.header),
            attack_event.matched_pattern,
            attack_event.file_name,
            attack_event.parsed_request.header.get('Host', "None")
            )
                       )
        self.connection.commit()
        cursor.close()

    def select(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM events")
        res = cursor.fetchone()
        cursor.close()
        return res

    def drop(self, table="events"):
        cursor = self.connection.cursor()
        cursor.execute("DROP TABLE %s" % table)
        self.connection.commit()
        cursor.close()

    def insert_profile(self, ip_address):
        cursor = self.connection.cursor()
        cursor.execute("""
                INSERT INTO ip_profiles(ip) VALUES (%s)""", (ip_address,))
        self.connection.commit()
        cursor.close()

    def update_profile(self, ip_profile):
        cursor = self.connection.cursor()
        cursor.execute("""
                UPDATE ip_profiles SET
                as_number = %s,
                as_name = %s,
                country_code = %s,
                total_requests = %s,
                total_scans = %s,
                bgp_prefix = %s,
                requests_per_scan = %s,
                avg_scan_duration = %s,
                scan_time_period = %s,
                last_event_time = %s
                where ip = %s""",
                (ip_profile.as_number, ip_profile.as_name,
                ip_profile.country_code, ip_profile.total_requests,
                ip_profile.total_scans, ip_profile.bgp_prefix,
                ip_profile.requests_per_scan, ip_profile.avg_scan_duration,
                ip_profile.scan_time_period, ip_profile.last_event_time,
                ip_profile.ip))
        self.connection.commit()
        cursor.close()

    def get_profile(self, source_ip):
        dict_cur = self.connection.cursor(
                        cursor_factory=psycopg2.extras.DictCursor)
        dict_cur.execute("""SELECT * from  ip_profiles
                        WHERE ip = %s""", (source_ip,))
        if dict_cur.rowcount == 0:
            return None
        else:
            ip_profile = IPProfile()
            profile_dict = dict_cur.fetchone()
            for key, value in profile_dict.items():
                setattr(ip_profile, key, value)
            return ip_profile

    def close(self):
        if self.connection:
            self.connection.close()
