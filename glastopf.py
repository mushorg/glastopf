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

import modules.HTTP.util as util
import modules.HTTP.method_handler as method_handler
import modules.events.attack as attack
from modules.handlers import request_handler
import modules.reporting.log_sqlite as log_sqlite
import modules.reporting.hp_feed as hpfeeds
from modules.handlers.emulators.dork_list import gen_dork_list

import modules.reporting.file_logger as file_logger
import modules.privileges as privileges


class GlastopfHoneypot(object):

    def __init__(self):
        self.log = file_logger.FileLogger(name="honeypot").log()
        self.log.info('Starting Glastopf')
        conf_parser = ConfigParser()
        conf_parser.read("glastopf.cfg")
        self.options = {
            "enabled": conf_parser.get("hpfeed", "enabled").encode('latin1'),
            "uid": conf_parser.get("webserver", "uid").encode('latin1'),
            "gid": conf_parser.get("webserver", "gid").encode('latin1'),
        }
        if self.options["enabled"] == "True":
            self.hpfeeds_logger = hpfeeds.HPFeedClient()
            self.log.info('HPFeeds started')
        self.sqlite_logger = log_sqlite.LogSQLite()
        gen_dork_list.regular_generate_dork(0)
        self.regular_gen_dork = threading.Thread(target=gen_dork_list.regular_generate_dork,args=(30,))
        self.regular_gen_dork.daemon = True
        self.regular_gen_dork.start()
        privileges.drop(self.options['uid'], self.options['gid'])
        self.log.info('Glastopf instantiated and privileges dropped')

    def print_info(self, attack_event):
        print attack_event.event_time,
        print attack_event.source_addr[0] + " requested",
        print attack_event.parsed_request.method,
        print attack_event.parsed_request.url, "on",
        print attack_event.parsed_request.header.get('Host', "None")
        self.log.info(' '.join([attack_event.source_addr[0],
                      attack_event.parsed_request.method,
                      attack_event.parsed_request.url]))

    def handle_request(self, raw_request, addr):
        HTTP_parser = util.HTTPParser()
        attack_event = attack.AttackEvent()
        # Parse the request
        attack_event.parsed_request = HTTP_parser.parse_request(raw_request)
        attack_event.source_addr = addr
        self.print_info(attack_event)
        # Start response with the server header
        # TODO: Add msg length header
        attack_event.response = util.HTTPServerResponse.response_header
        MethodHandlers = method_handler.HTTPMethods()
        # Handle the HTTP request method
        attack_event.matched_pattern = getattr(MethodHandlers,
                                    attack_event.parsed_request.method,
                                    "GET")(attack_event.parsed_request)
        gen_dork_list.collect_dork(attack_event)
        # Handle the request with the specific vulnerability module
        getattr(request_handler, attack_event.matched_pattern,
                request_handler.unknown)(attack_event)
        # Logging the event
        self.sqlite_logger.insert(attack_event)
        if self.options["enabled"] == "True":
            self.hpfeeds_logger.handle_send("glastopf.events",
                                        json.dumps(attack_event.event_dict()))
            if attack_event.file_name != None:
                with file("files/" + attack_event.file_name, 'r') as file_handler:
                    file_content = file_handler.read()
                self.hpfeeds_logger.handle_send("glastopf.files",
                                                attack_event.file_name + " " + base64.b64encode(file_content))
        return attack_event.response
