# Author: Sooky Peter <xsooky00@stud.fit.vutbr.cz>
# Brno University of Technology, Faculty of Information Technology

import logging
import os

# import pyodbc
import sqlite3

from ConfigParser import NoSectionError, NoOptionError
from glastopf.modules.reporting.auxiliary.base_logger import BaseLogger


class LogProfiler(BaseLogger):
    def __init__(self, data_dir, work_dir, config="glastopf.cfg"):
        config = os.path.join(work_dir, config)
        BaseLogger.__init__(self, config)
        self.options = {'enabled': False}
        try:
            self.options = {
                "enabled": self.config.getboolean("profiler", "enabled"),
                "database": self.config.get("main-database", "connection_string")
            }
        except (NoSectionError, NoOptionError):
            return
        self.logger = logging.getLogger(__name__)

    def insert(self, ip_profile):
        # insertion into the database is handled by the regular updates; logging the changes seems irrelevant
        pass

    # retrieve all comments for a specific IP address stored in the database
    def get_comments(self, ip_address):
        if not self.options['enabled']:
            self.logger.error('Glastopf LogProfiler is inactive.')
            return

        driver, data_source_name = self.options['database'].split(':///')
        # for now use conditional statements; a more transparent implementation
        # might be using pyodbc in the future
        if driver == 'sqlite':
            # sqlite
            try:
                connection = sqlite3.connect(data_source_name)
                c = connection.cursor()
                c.execute("""SELECT comments FROM ip_profiles WHERE ip==?""", (ip_address,))
                comments_list = c.fetchall()
                c.close()
            except sqlite3.DatabaseError as e:
               self.logger.error('Comment retrieval failed due to ({0})'.format(e))
        else:
            # not supported databse type
            return ''
        return comments_list

    # add a comment for a specific IP address stored in the database
    def add_comment(self, ip_address, comment):
        if not self.options['enabled']:
            self.logger.error('Glastopf LogProfiler is inactive.')
            return

        driver, data_source_name = self.options['database'].split(':///')
        # for now use conditional statements; a more transparent implementation
        # might be using pyodbc in the future
        if driver == 'sqlite':
            # sqlite
            try:
                connection = sqlite3.connect(data_source_name)
                c = connection.cursor()
                c.execute("""SELECT comments FROM ip_profiles WHERE ip==?""", (ip_address,))
                comments_list = c.fetchall()
                if len(comments_list) == 0:
                    c.execute("""INSERT INTO ip_profiles(ip, total_requests, total_scans, avg_scan_duration, scan_time_period, comments) VALUES (?, ?, ?, ?, ?, ?)""", (ip_address, 0, 0, 1, 1, comment))
                else:
                    comments_list.append((comment, ))
                    comments = ""
                    for i in range(len(comments_list)):
                        comments += str(comments_list[i][0])
                        c.execute("""UPDATE ip_profiles SET comments=(?) WHERE ip==?""", (comments, ip_address))
                connection.commit()
                c.close()
                self.logger.info('Comment added to database for ip address {0}'.format(ip_address))
            except sqlite3.DatabaseError as e:
                self.logger.error('Comment insertion failed due to ({0})'.format(e))
        else:
            # not supported database type
            return ''

