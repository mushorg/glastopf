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
import sys
import Queue
import threading
import string
import random

from ConfigParser import ConfigParser
import logging.handlers

from __init__ import __version__
from modules.HTTP.handler import HTTPHandler
import modules.HTTP.method_handler as method_handler
import modules.events.attack as attack
from modules.handlers.request_handler import RequestHandler
from modules import logging_handler
import shutil
import modules.privileges as privileges
#import modules.processing.profiler as profiler
from modules.handlers.emulators.dork_list import dork_file_processor
from modules.handlers.emulators.dork_list import database_sqla
from modules.handlers.emulators.dork_list import database_mongo
from modules.handlers.emulators.dork_list import dork_page_generator
from modules.handlers.emulators.dork_list import cluster
from modules.handlers.emulators.dork_list import mnem_service
from modules.reporting.main import log_mongodb, log_sql
from subprocess import check_call
from sqlalchemy import create_engine


logger = logging.getLogger(__name__)
package_directory = os.path.dirname(os.path.abspath(__file__))


class GlastopfHoneypot(object):
    def __init__(self, config="glastopf.cfg", work_dir=os.getcwd()):
        """
        :param work_dir: directory used for data storage and various data files, must be writeable by glastopf. Default: os.getcwd()
        :param config: path to the glastopf configuration file. Default: glastopf.cfg
        """
        logger.info('Initializing Glastopf {0} using "{1}" as work directory.'.format(__version__,work_dir))
        self.work_dir = work_dir
        self.data_dir = os.path.join(self.work_dir, 'data')

        conf_parser = ConfigParser()
        conf_parser.read(config)
        self.options = {
            "uid": conf_parser.get("webserver", "uid").encode('latin1'),
            "gid": conf_parser.get("webserver", "gid").encode('latin1'),
            "proxy_enabled": conf_parser.get("webserver", "proxy_enabled").encode('latin1'),
 	        "banner": conf_parser.get("misc", "banner").encode('latin1'),
        }

        (self.maindb, self.dorkdb) = self.setup_main_database(conf_parser)

        self.dork_generator = self.setup_dork_generator(conf_parser, self.work_dir)

        if len(self.dork_generator.get_current_pages()) == 0:
            logger.info("Generating initial dork pages - this can take a while.")
            self.dork_generator.regular_generate_dork(0)

        #profiler disabled until issue #26 is fixed
        self.profiler_available = False
        if self.profiler_available:
            self.profiler = profiler.Profiler(self.maindb)

        #self.HTTP_parser = util.HTTPParser()
        self.MethodHandlers = method_handler.HTTPMethods(self.data_dir)

        #used for post processing (logging and analysis) of attack events
        self.post_queue = Queue.Queue()
        self.workers_enabled = False

    def start_background_workers(self):
        """
        Starts background threads responsible for data processing and logging.
        """
        privileges.drop(self.work_dir, self.options['uid'], self.options['gid'])
        self.workers_enabled = True
        self.loggers = logging_handler.get_aux_loggers(self.data_dir)

        dork_thread = threading.Thread(
            target=self.dork_generator.regular_generate_dork, args=(30,))
        dork_thread.daemon = True
        dork_thread.start()

        self.post_processing = threading.Thread(target=self.post_processer)
        self.post_processing.daemon = True
        self.post_processing.start()
        logger.info('Glastopf started and privileges dropped.')

    def stop_background_workers(self):
        """
        Notifies background threads that they are supposed to stop.
        This method does not guarantee that the threads actually stops.
        """
        logger.info('Stopping Glastopf.')
        self.dork_generator.enabled = False
        self.workers_enabled = False

    def post_processer(self):
        while self.workers_enabled:
            attack_event = self.post_queue.get()

            self.dork_generator.collect_dork(attack_event)

            if self.maindb:
                self.maindb.insert(attack_event)

            for logger in self.loggers:
                logger.insert(attack_event)

    def setup_dork_generator(self, conf_parser, work_dir):
        token_pattern = conf_parser.get('dork-db', 'token_pattern')
        n_clusters = conf_parser.getint('dork-db', 'n_clusters')
        max_iter = conf_parser.getint('dork-db', 'max_iter')
        n_init = conf_parser.getint('dork-db', 'n_init')

        file_processor = dork_file_processor.DorkFileProcessor(self.dorkdb)

        mnemosyne_service = None
        clusterer = cluster.Cluster(token_pattern, n_clusters, max_iter, n_init, min_df=0.0)
        if conf_parser.has_option('dork-db', 'mnem_service'):
            if conf_parser.getboolean('dork-db', 'mnem_service') == True:
                mnemosyne_service = mnem_service.Mnem_Service()

        return dork_page_generator.DorkPageGenerator(self.dorkdb,
                                                     file_processor,
                                                     clusterer,
                                                     data_dir=self.data_dir,
                                                     mnem_service_instance=mnemosyne_service)

    def setup_main_database(self, conf_parser):

        if conf_parser.getboolean("main-database", "enabled"):
            connection_string = conf_parser.get("main-database", "connection_string")
            logger.info("Connecting to main database with: {0}".format(connection_string))
            if connection_string.startswith("mongodb://"):
                maindb = log_mongodb.Database(connection_string)
                dorkdb = database_mongo.Database(connection_string)
                return (maindb, dorkdb)
            elif connection_string.startswith(("sqlite", "mysql",
                                               "oracle", "postgresql")):
                sqla_engine = create_engine(connection_string)
                maindb = log_sql.Database(sqla_engine)
                dorkdb = database_sqla.Database(sqla_engine)
                return (maindb, dorkdb)
            else:
                logger.error("Invalid connection string.")
                sys.exit(1)
        else:
            default_db = "sqlite://db/glastopf.db"
            logger.info("Main datbase has been disabled, dorks will be stored in: {0}".format(default_db))
            #db will only be used for dorks
            sqla_engine = create_engine("sqlite://db/glastopf.db")
            maindb = log_sql.Database(sqla_engine)
            dorkdb = database_sqla.Database(sqla_engine)
            #disable usage of main logging datbase
            return (None, dorkdb)

    @staticmethod
    def _get_entry(user_id):
        # Random username of 3 characters
        name = "".join([random.choice(string.letters[:26]) for i in xrange(3)])
        gid = user_id
        uid = user_id
        g = "\n" + name + ":x:" + str(gid) + ":"
        p = "\n" + name + ":x:" + str(uid) + ":" + str(gid) + "::" + "/home/" + name + \
            "/:/bin/sh"
        # If we want to, we could also give a password hash in place of '*'
        s = "\n" + name + ":*:6723:0:99999:7:::"
        return p, s, g

    @staticmethod
    def randomize_vdocs(vpath):
        # For now, we'll only change the passwd, shadow and group files.
        pwd_path = os.path.join(vpath, 'linux/etc/passwd')
        shd_path = os.path.join(vpath, 'linux/etc/shadow')
        grp_path = os.path.join(vpath, 'linux/etc/group')

        num_entries = random.randint(1, 10) # number of random entries

        pwd = open(pwd_path, "a")
        shd = open(shd_path, "a")
        grp = open(grp_path, "a")
        for i in xrange(num_entries):
            # Possible duplication of user id, but very low probability
            user_id = random.randint(1000, 1500)
            pwd_entry, shd_entry, grp_entry = GlastopfHoneypot._get_entry(user_id)

            pwd.write(pwd_entry)
            shd.write(shd_entry)
            grp.write(grp_entry)
        pwd.close()
        shd.close()
        grp.close()

    @staticmethod
    def prepare_sandbox(work_dir):
        logger.info('Creating PHP sandbox')
        #create sandbox
        sandbox_dir = os.path.join(package_directory, 'sandbox')
        #preserve old working dir
        old_cwd = os.getcwd()
        os.chdir(sandbox_dir)
        #execute makefile and output to self.workdir/data/apd_sandbox.php
        sandbox_out = os.path.join(work_dir, 'data', 'sandbox.php')
        check_call(['make', '-B', '-s', 'out={0}'.format(sandbox_out)])
        #restore state of original working dir
        os.chdir(old_cwd)

    @staticmethod
    def prepare_environment(work_dir):
        """
        Configures the Glastopf work environment.

        If this methods completes without exceptions, the environment will look something like:
        (self.workdir)/
                      glastopf.cfg
                      db/
                      log/
                      data/
                          sandbox.php
                          dork_pages/
                          virtual_docs/
                          (and various other module data directories)
        """
        logger.info('Preparing work environment.')
        if not os.path.isfile(os.path.join(work_dir, 'glastopf.cfg')):
            logger.info('Copying glastopf.cfg to work work_dir.')
            shutil.copyfile(os.path.join(package_directory, 'glastopf.cfg.dist'),
                            os.path.join(work_dir, 'glastopf.cfg'))

        #copy emulator level data
        emulator_data_dir = os.path.join(package_directory, 'modules/handlers/emulators/data/')

        shutil.copytree(emulator_data_dir, os.path.join(work_dir, 'data/'),
                        ignore=GlastopfHoneypot._ignore_copy_files)

        dirs = ('log', 'db', 'data')
        for entry in dirs:
            dir_path = os.path.join(work_dir, entry)
            if not os.path.isdir(dir_path):
                os.mkdir(dir_path)
            # Randomize the files in virtualdocs folder
        GlastopfHoneypot.randomize_vdocs(os.path.join(work_dir, 'data/virtualdocs/'))
        GlastopfHoneypot.prepare_sandbox(work_dir)

    @staticmethod
    def _ignore_copy_files(path, content):
        to_ignore = []
        for file in content:
            if file in ('.placeholder', '.git'):
                to_ignore.append(file)
        return to_ignore

    def _handle_proxy(self, attack_event, addr):
        client_ip = attack_event.http_request.header['X-Forwarded-For']
        client_ip = client_ip.split(',')[-1]
        if client_ip == 'unknown':
            client_ip = '0.0.0.0'
            # Note: the port number is not relevant in this case
        attack_event.source_addr = (client_ip, addr[1])

    def handle_request(self, raw_request, addr, connection):

        attack_event = attack.AttackEvent()
        attack_event.raw_request = raw_request

        attack_event.http_request = HTTPHandler(raw_request, addr, self.options['banner'], sys_version=' ')

        if self.options["proxy_enabled"] == "True":
            self._handle_proxy(attack_event)
        else:
            attack_event.source_addr = addr
        logger.info("{0} requested {1} {2} on {3}".format(
            attack_event.source_addr[0],
            attack_event.http_request.command,
            attack_event.http_request.path,
            attack_event.http_request.headers.get('Host', "None")
        )
        )
        # Handle the HTTP request method
        attack_event.matched_pattern = getattr(
            self.MethodHandlers,
            attack_event.http_request.command,
            self.MethodHandlers.GET
        )(attack_event.http_request)
        # Handle the request with the specific vulnerability module
        request_handler = RequestHandler(os.path.join(self.work_dir, 'data/'))
        emulator = request_handler.get_handler(attack_event.matched_pattern)
        emulator.handle(attack_event)
        # Logging the event
        if self.profiler_available:
            self.profiler.handle_event(attack_event)
        self.post_queue.put(attack_event)

        header = attack_event.http_request.get_response_header()
        body = attack_event.http_request.get_response_body()
        return header, body
