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
from ConfigParser import ConfigParser
import logging.handlers

from modules.HTTP import util
import modules.HTTP.method_handler as method_handler
import modules.events.attack as attack
from modules.handlers.request_handler import RequestHandler
from modules import logging_handler
import shutil
import modules.privileges as privileges
import modules.processing.profiler as profiler
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
        logger.info('Initializing Glastopf using "{0}" as work directory.'.format(work_dir))
        self.work_dir = work_dir
        self.data_dir = os.path.join(self.work_dir, 'data')

        self.prepare_environment(self.work_dir)

        conf_parser = ConfigParser()
        conf_parser.read(config)
        self.options = {
            "uid": conf_parser.get("webserver", "uid").encode('latin1'),
            "gid": conf_parser.get("webserver", "gid").encode('latin1'),
            "proxy_enabled": conf_parser.get("webserver", "proxy_enabled").encode('latin1'),
        }

        (self.maindb, self.dorkdb) = self.setup_main_database(conf_parser)

        self.dork_generator = self.setup_dork_generator(conf_parser, self.work_dir)

        if len(self.dork_generator.get_current_pages()) == 0:
            logger.info("Generating initial dork pages - this can take a while.")
            self.dork_generator.regular_generate_dork(0)

        #hmm?
        self.profiler_available = False
        if self.profiler_available:
            self.profiler = profiler.Profiler(self.maindb)

        self.HTTP_parser = util.HTTPParser()
        self.MethodHandlers = method_handler.HTTPMethods()

        #used for post processing (logging and analysis) of attack events
        self.post_queue = Queue.Queue()
        self.workers_enabled = False

    def start_background_workers(self):
        self.workers_enabled = True
        self.loggers = logging_handler.get_aux_loggers()

        dork_thread = threading.Thread(
            target=self.dork_generator.regular_generate_dork, args=(30,))
        dork_thread.daemon = True
        dork_thread.start()

        self.post_processing = threading.Thread(target=self.post_processer)
        self.post_processing.daemon = True
        self.post_processing.start()
        privileges.drop(self.options['uid'], self.options['gid'])
        logger.info('Glastopf started and privileges dropped.')

    def stop_bakground_workers(self):
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
                self.profiler_available = True
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
            self.profiler_available = True
            #disable usage of main logging datbase
            return (None, dorkdb)

    def prepare_environment(self, directory):
        """
        Configures the Glastopf work environment.

        If this methods completes without exceptions, the environment will look something like:
        (self.workdir)/
                      glastopf.cfg
                      db/
                      log/
                      files/
                      data/
                          apd_sandbox.php
                          dork_pages/
                          virtual_docs/
                          (and various other module data directories)
        """

        if not os.path.isfile(os.path.join(directory, 'glastopf.cfg')):
            logger.info('Copying glastopf.cfg to work directory.')
            shutil.copyfile(os.path.join(package_directory, 'glastopf.cfg.dist'),
                            os.path.join(directory, 'glastopf.cfg'))

        #copy emulator level data
        emulator_data_dir = os.path.join(package_directory, 'modules/handlers/emulators/data/')
        shutil.copytree(emulator_data_dir, os.path.join(directory, 'data/'))

        dirs = ('log', 'db', 'files', 'data')
        for entry in dirs:
            if not os.path.isdir(entry):
                os.mkdir(entry)

        GlastopfHoneypot.prepare_sandbox(directory)

    @staticmethod
    def prepare_sandbox(directory):
        #create sandbox
        sandbox_dir = os.path.join(package_directory, 'sandbox')
        #preserve old working dir
        old_cwd = os.getcwd()
        os.chdir(sandbox_dir)
        #execute makefile and output to self.workdir/data/apd_sandbox.php
        sandbox_out = os.path.join(directory, 'data', 'apd_sandbox.php')
        check_call(['make', '-B', 'out={0}'.format(sandbox_out)])
        #restore state of original working dir
        os.chdir(old_cwd)

    def _handle_proxy(self, attack_event, addr):
        client_ip = attack_event.parsed_request.header['X-Forwarded-For']
        client_ip = client_ip.split(',')[-1]
        if client_ip == 'unknown':
            client_ip = '0.0.0.0'
            # Note: the port number is not relevant in this case
        attack_event.source_addr = (client_ip, addr[1])

    def handle_request(self, raw_request, addr, connection):
        response_code = "200 OK"
        attack_event = attack.AttackEvent()
        attack_event.sensor_addr = connection.sock.getsockname()
        attack_event.raw_request = raw_request
        # Parse the request
        try:
            attack_event.parsed_request = self.HTTP_parser.parse_request(
                raw_request)
        except util.ParsingError as e:
            response_code = e.response_code
        else:
            if self.options["proxy_enabled"] == "True":
                self._handle_proxy(attack_event)
            else:
                attack_event.source_addr = addr
            logger.info("{0} requested {1} {2} on {3}".format(
                attack_event.source_addr[0],
                attack_event.parsed_request.method,
                attack_event.parsed_request.url,
                attack_event.parsed_request.header.get('Host', "None")
            )
            )
            # Handle the HTTP request method
            attack_event.matched_pattern = getattr(
                self.MethodHandlers,
                attack_event.parsed_request.method,
                self.MethodHandlers.GET
            )(attack_event.parsed_request)
            # Handle the request with the specific vulnerability module
            request_handler = RequestHandler(os.path.join(self.work_dir, 'data/'))
            emulator = request_handler.get_handler(attack_event.matched_pattern)
            emulator.handle(attack_event)
            # Logging the event
            if self.profiler_available:
                self.profiler.handle_event(attack_event)
            self.post_queue.put(attack_event)
            response_code = "200 OK"
        response_util = util.HTTPServerResponse(response_code)
        attack_event.response = response_util.get_header(attack_event) + attack_event.response
        return attack_event.response

