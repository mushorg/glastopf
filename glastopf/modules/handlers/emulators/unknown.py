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
from random import choice
import codecs
import sys
from string import Template

from glastopf.modules.handlers import base_emulator


if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')


class DorkList(base_emulator.BaseEmulator):
    def __init__(self, data_dir):
        super(DorkList, self).__init__(data_dir)

    def _get_template(self, attack_event):
        # TODO: decode the file using chardet or even better create
        # them with utf-8 encoding
        pages_path = os.path.join(self.data_dir, 'dork_pages')
        dork_page_list = os.listdir(pages_path)
        self.dork_page = os.path.join(pages_path, choice(dork_page_list))
        ip_address = attack_event.source_addr[0]
        with codecs.open(self.dork_page, "rb", "utf-8") as dork_page:
            comments_file = os.path.join(self.data_dir, 'comments.txt')
            if os.path.isfile(comments_file):
                with codecs.open(comments_file, "r", "utf-8") as comments_txt:
                    general_comments = comments_txt.read()
                    #ip_comments = profiler.Profiler.get_comments(ip_address)
                    #display_comments = str(ip_comments) + str(general_comments)
                    display_comments = '' + str(general_comments)
            else:
                display_comments = ''
            template = Template(dork_page.read())
        return template, display_comments

    def handle(self, attack_event):
        template, display_comments = self._get_template(attack_event)
        self.template = template.safe_substitute(login_msg="",
                                                 comments=display_comments)
        attack_event.http_request.set_response(self.template)
        #attack_event.response += self.template
        return attack_event
