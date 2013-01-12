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
from modules.handlers.emulators.dork_list import gen_dork_list

import os
from modules import logging_handler
import modules.privileges as privileges
import modules.processing.profiler as profiler


class GlastopfHoneypot(object):

    def __init__(self, test=False):
        self.create_empty_dirs()
        self.test = test
        if not self.test:
            self.loggers = logging_handler.get_loggers()
        conf_parser = ConfigParser()
        conf_parser.read("glastopf.cfg")
        self.options = {
            "hpfeeds": conf_parser.get("hpfeed", "enabled").encode('latin1'),
            "uid": conf_parser.get("webserver", "uid").encode('latin1'),
            "gid": conf_parser.get("webserver", "gid").encode('latin1'),
            "proxy_enabled": conf_parser.get("webserver", "proxy_enabled").encode('latin1')
        }
        if self.options["hpfeeds"] == "True":
            self.hpfeeds_logger = hpfeeds.HPFeedClient()
            self.log.info('HPFeeds started')
        if not self.test:
            if len(os.listdir('modules/handlers/emulators/dork_list/pages/')) == 0:
                gen_dork_list.regular_generate_dork(0)
            self.regular_gen_dork = threading.Thread(
                        target=gen_dork_list.regular_generate_dork, args=(30,))
            self.regular_gen_dork.daemon = True
            self.regular_gen_dork.start()
            self.profiler = profiler.Profiler()
        self.HTTP_parser = util.HTTPParser()
        self.MethodHandlers = method_handler.HTTPMethods()

        self.post_queue = Queue.Queue()
        self.post_processing = threading.Thread(target=self.post_processer)
        self.post_processing.daemon = True
        self.post_processing.start()
        
        privileges.drop(self.options['uid'], self.options['gid'])
        self.log.info('Glastopf instantiated and privileges dropped')

    def create_empty_dirs(self):
        dirs = ('log', 'db', 'files', 'modules/handlers/emulators/server_files/',
                'modules/handlers/emulators/dork_list/pages')
        for entry in dirs:
            if not os.path.isdir(entry):
                os.mkdir(entry)    

    def print_info(self, attack_event):
        print attack_event.event_time,
        print attack_event.source_addr[0] + " requested",
        print attack_event.parsed_request.method,
        print attack_event.parsed_request.url, "on",
        print attack_event.parsed_request.header.get('Host', "None")
        self.log.info(' '.join([attack_event.source_addr[0],
                      attack_event.parsed_request.method,
                      attack_event.parsed_request.url]))

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
        self.print_info(attack_event)
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
            self.profiler.handle_event(attack_event)
            self.post_queue.put(attack_event)
        response_util = util.HTTPServerResponse()
        attack_event.response = response_util.get_header(attack_event) + attack_event.response
        return attack_event.response

    def post_processer(self):
        while True:
            attack_event = self.post_queue.get()

            gen_dork_list.collect_dork(attack_event)

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
