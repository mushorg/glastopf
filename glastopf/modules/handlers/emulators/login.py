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

from glastopf.modules.handlers import base_emulator


class LoginEmulator(base_emulator.BaseEmulator):
    def __init__(self, data_dir):
        super(LoginEmulator, self).__init__(data_dir)

    def handle(self, attack_event):
        pages_dir = os.path.join(self.data_dir, 'dork_pages')
        dork_page_list = os.listdir(pages_dir)
        dork_page = choice(dork_page_list)
        with codecs.open(os.path.join(pages_dir, dork_page), "r", "utf-8") as dork_page:
            url_dict = parse_qs(attack_event.http_request.request_body)
            if ('login' in url_dict) or ('password' in url_dict):
                login_msg = "Incorrect login or password! Please try again."
            else:
                login_msg = ""
            with codecs.open(os.path.join(self.data_dir, 'comments.txt'), "r", "utf-8") as comments_txt:
                template = Template(dork_page.read())
                response = template.safe_substitute(
                    login_msg=login_msg,
                    comments=comments_txt.read())
            attack_event.http_request.set_response(response)
