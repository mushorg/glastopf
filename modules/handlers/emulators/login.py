# Copyright (C) 2012  Phani Vadrevu
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
from random import choice
import codecs
from urlparse import parse_qs
from string import Template

from modules.handlers import base_emulator


class LoginEmulator(base_emulator.BaseEmulator):
    def __init__(self):
        pass

    def handle(self, attack_event):
        dork_page_list = os.listdir("modules/handlers/emulators/"
                                    "dork_list/pages")
        if '.svn' in dork_page_list:
            dork_page_list.remove('.svn')
        dork_page = choice(dork_page_list)
        with codecs.open("modules/handlers/emulators/dork_list/pages/" +
                            dork_page, "r", "utf-8") as dork_page:
            url_dict = parse_qs(attack_event.parsed_request.body)
            if ('login' in url_dict) or ('password' in url_dict):
                login_msg = "Incorrect login or password! Please try again."
            else:
                login_msg = ""
            with codecs.open("modules/handlers/emulators/dork_list/"
                             "comments.txt", "r", "utf-8") as comments_txt:
                template = Template(dork_page.read())
                attack_event.response = template.safe_substitute(
                                                login_msg=login_msg,
                                                comments=comments_txt.read())
