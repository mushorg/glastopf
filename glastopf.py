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

import modules.HTTP.util as util
import modules.HTTP.method_handler as method_handler
import modules.events.attack as attack
from modules.handlers import request_handler
import modules.reporting.hp_feed as hpfeeds
from modules.handlers.emulators.dork_list import dork_db, database, dork_page_generator

import os
from modules import logging_handler
import modules.privileges as privileges
import modules.processing.profiler as profiler
import logging
import logging.handlers

logger = logging.getLogger(__name__)


class GlastopfHoneypot(object):

    def __init__(self, test=False, config="glastopf.cfg"):
        self.create_empty_dirs()
        self.test = test
        if not self.test:
            self.loggers = logging_handler.get_loggers()
        logger.info('Starting Glastopf')
        conf_parser = ConfigParser()
        conf_parser.read(config)
        self.options = {
            "hpfeeds": conf_parser.get("hpfeed", "enabled").encode('latin1'),
            "uid": conf_parser.get("webserver", "uid").encode('latin1'),
            "gid": conf_parser.get("webserver", "gid").encode('latin1'),
            "proxy_enabled": conf_parser.get("webserver", "proxy_enabled").encode('latin1'),
            "dork_db": conf_parser.get("dork-db", "dork_db").encode('latin1')
        }
        if self.options["hpfeeds"] == "True":
            self.hpfeeds_logger = hpfeeds.HPFeedClient(config=config)
            logger.info("HPFeeds started")
        self.dorkdb = dork_db.DorkDB(self.options['dork_db'])
        self.db = database.Database(config=config)
        pages_dir = 'modules/handlers/emulators/dork_list/pages/'
        self.dork_generator = dork_page_generator.DorkPageGenerator(self.dorkdb, self.db,
                                                                    pages_dir)
        if len(os.listdir(pages_dir)) == 1:
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

    def create_empty_dirs(self):
        dirs = ('log', 'db', 'files', 'modules/handlers/emulators/server_files/',
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
        attack_event = attack.AttackEvent()
        attack_event.sensor_addr = connection.sock.getsockname()
        attack_event.raw_request = raw_request
        # Parse the request
        attack_event.parsed_request = self.HTTP_parser.parse_request(raw_request)
        if self.options["proxy_enabled"] == "True":
            self._handle_proxy(attack_event)
        else:
            attack_event.source_addr = addr

        logger.info("{0} requested {1} {2} on {3}".format(attack_event.source_addr[0],
                                                          attack_event.parsed_request.method,
                                                          attack_event.parsed_request.url,
                                                          attack_event.parsed_request.header.get('Host', "None")))
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
        response_util = util.HTTPServerResponse()
        attack_event.response = response_util.get_header(attack_event) + attack_event.response
        return attack_event.response

    def post_processer(self):
        while True:
            attack_event = self.post_queue.get()

            #gen_dork_list.collect_dork(attack_event)
            self.dork_generator.collect_dork(attack_event)

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
