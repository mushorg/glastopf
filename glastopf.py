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
import base64
import threading
from ConfigParser import ConfigParser

import Queue

from modules.HTTP import util
import modules.HTTP.method_handler as method_handler
import modules.events.attack as attack
from modules.handlers import request_handler
import modules.reporting.aux.hp_feed as hpfeeds
from modules.handlers.emulators.dork_list import dork_file_processor
from modules.handlers.emulators.dork_list import database_sqla
from modules.handlers.emulators.dork_list import database_mongo
from modules.handlers.emulators.dork_list import dork_page_generator
from modules.handlers.emulators.dork_list import cluster
from modules.reporting.main import log_mongodb, log_sql
from sqlalchemy import create_engine

import os
import sys
from modules import logging_handler
import modules.privileges as privileges
import modules.processing.profiler as profiler
import logging.handlers

logger = logging.getLogger(__name__)


class GlastopfHoneypot(object):

    def __init__(self, test=False, config="glastopf.cfg"):
        self.create_empty_dirs()
        self.test = test
        logger.info('Starting Glastopf')

        conf_parser = ConfigParser()
        conf_parser.read(config)
        self.options = {
            "hpfeeds": conf_parser.get("hpfeed", "enabled").encode('latin1'),
            "uid": conf_parser.get("webserver", "uid").encode('latin1'),
            "gid": conf_parser.get("webserver", "gid").encode('latin1'),
            "proxy_enabled": conf_parser.get("webserver", "proxy_enabled").encode('latin1'),
        }

        if self.options["hpfeeds"] == "True":
            self.hpfeeds_logger = hpfeeds.HPFeedClient(config=config)
            logger.info("HPFeeds started")

        (self.maindb, self.dorkdb) = self.setup_main_database(conf_parser)

        self.dork_generator = self.setup_dork_generator(conf_parser)

        if not self.test:
            self.loggers = logging_handler.get_aux_loggers()

        if len(self.dork_generator.get_current_pages()) == 0:
            logger.info("Generating initial dork pages - this can take a while.")
            self.dork_generator.regular_generate_dork(0)

        if not test:
            regular_gen_dork = threading.Thread(
                target=self.dork_generator.regular_generate_dork, args=(30,))
            regular_gen_dork.daemon = True
            regular_gen_dork.start()
        self.profiler = profiler.Profiler()

        self.HTTP_parser = util.HTTPParser()
        self.MethodHandlers = method_handler.HTTPMethods()

        self.post_queue = Queue.Queue()
        self.post_processing = threading.Thread(target=self.post_processer)
        self.post_processing.daemon = True
        self.post_processing.start()

        privileges.drop(self.options['uid'], self.options['gid'])
        logger.info('Glastopf instantiated and privileges dropped')

    def setup_dork_generator(self, conf_parser):
        token_pattern = conf_parser.get('dork-db', 'token_pattern')
        n_clusters = conf_parser.getint('dork-db', 'n_clusters')
        max_iter = conf_parser.getint('dork-db', 'max_iter')
        n_init = conf_parser.getint('dork-db', 'n_init')

        file_processor = dork_file_processor.DorkFileProcessor(self.dorkdb)

        clusterer = cluster.Cluster(token_pattern, n_clusters, max_iter, n_init, min_df=0.0)
        return dork_page_generator.DorkPageGenerator(self.dorkdb,
                                                                 file_processor,
                                                                 clusterer)

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

    def create_empty_dirs(self):
        dirs = ('log', 'db', 'files',
                'modules/handlers/emulators/server_files/',
                'modules/handlers/emulators/dork_list/pages')
        for entry in dirs:
            if not os.path.isdir(entry):
                os.mkdir(entry)

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
            emulator = request_handler.get_handler(attack_event.matched_pattern)
            emulator.handle(attack_event)
            # Logging the event
            if not self.test:
                #self.profiler.handle_event(attack_event)
                self.post_queue.put(attack_event)
            response_code = "200 OK"
        response_util = util.HTTPServerResponse(response_code)
        attack_event.response = response_util.get_header(attack_event) + attack_event.response
        return attack_event.response

    def post_processer(self):
        while True:
            attack_event = self.post_queue.get()

            #gen_dork_list.collect_dork(attack_event)
            self.dork_generator.collect_dork(attack_event)

            if self.maindb:
                self.maindb.insert(attack_event)

            for logger in self.loggers:
                logger.insert(attack_event)

            if self.options["hpfeeds"] == "True":
                self.hpfeeds_logger.handle_send("glastopf.events",
                                                json.dumps(attack_event.event_dict()))
                if attack_event.file_name != None:
                    with file("files/" + attack_event.file_name, 'r') as file_handler:
                        file_content = file_handler.read()
                        self.hpfeeds_logger.handle_send("glastopf.files",
                                                        attack_event.file_name + " " + base64.b64encode(file_content))
