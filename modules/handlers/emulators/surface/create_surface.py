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

import hashlib
import codecs
import unicodedata
import time
import os

from random import choice, shuffle

import jinja2

from configobj import ConfigObj

from modules.handlers.emulators.surface import surface_html, dork_database, cluster_dorks, process_dork_file


class SurfaceCreator(object):

    def __init__(self, config="glastopf.cfg"):
        self.config = ConfigObj(config)
        self.dork_db = dork_database.DorkDB()

    def collect_dork(self, attack_event):
        if attack_event.matched_pattern != self.config["collect_dork"]["exclude_pattern"]:
            try:
                # TODO: Fix request parsing (more generic)
                dork = attack_event.parsed_request.url.split("?")[0]
                # TODO: Fix insert
                self.dork_db.insert_data("inurl", dork)
            except Exception as e:
                raise e
        else:
            # TODO: Do something
            pass

    def get_old_dork_pages_list(self, folder):
        dork_lists = []
        for f in os.listdir(folder):
            file_path = os.path.join(folder, f)
            if os.path.isfile(file_path):
                dork_lists.append(file_path)
        return dork_lists

    def fix_encoding(self, line):
        return unicodedata.normalize("NFKD", line).encode("ascii", "ignore")

    def prepare_text(self, txt_file="modules/handlers/emulators/dork_list/pride.txt"):
        # TODO: Do we really need codecs here?
        with codecs.open(txt_file, "rb", "utf-8") as text_file:
            # TODO: Test that beast
            line_list = [self.fix_encoding(text_line.strip()) for text_line in text_file.readlines() if text_line != ""]
        return line_list

    def fetch_data(self):
        self.line_list = self.prepare_text()
        shuffle(self.line_list)
        self.intext_list = self.dork_db.get_dorks_from_dorkdb("intext")
        self.intitle_list = self.dork_db.get_dorks_from_dorkdb("intitle")

    def fetch_cluster_data(self, inurl_list):
        c = cluster_dorks.Cluster()
        c.cluster(inurl_list, self.dork_db.config)
        self.inurl_cluster = choice(c.clusters)

    def create_page(self, inurl_list):
        body = ""
        for i in range(0, 49):
            body += self.line_list.pop()
            href = inurl_list.pop()
            body += " <a href='%s'>%s</a> " % (href, choice(self.intext_list)[0])
        for i in range(0, 5):
            body += self.line_list.pop()
            if self.config["use_cluster"]:
                href = choice(self.inurl_cluster)
                body += " <a href='%s'>%s</a> " % (href, choice(self.intext_list)[0])
        loader = jinja2.FileSystemLoader("modules/handlers/emulators/surface/templates/default.html", encoding="utf-8")
        env = jinja2.Environment(loader)
        template = env.get_template()
        dork_page = template.render(titel=choice(self.intitle_list)[0], form_URL="http://localhost:8080", body=body, footer="Footer Powered By")
        page_md5 = hashlib.md5(dork_page).hexdigest()
        with codecs.open("modules/handlers/emulators/dork_list/pages/%s" % page_md5, "w", "utf-8") as dork_file:
            dork_file.write(dork_page)

    def generate_dork_pages(self, first_time):
        if first_time:
            processor = process_dork_file.DorkFileProcessor()
            processor.process_dorks()
        self.fetch_data()
        #inurl_list = dork_reader.get_dork_list("inurl")
        inurl_list = self.dork_db.select_data()
        # TODO: Fix cluster config
        if self.config["use_cluster"]:
            self.fetch_cluster_data(inurl_list)
        while len(inurl_list) > 50 and len(self.line_list) > 56:
            self.create_page(inurl_list)

    def remove_old_dork_pages(self, old_dork_list):
        for file_path in old_dork_list:
            try:
                os.unlink(file_path)
            except Exception, e:
                pass

    def regular_generate_dork(self, sleeper, dirname="modules/handlers/emulators/dork_list/pages/"):
        sleep_time = sleeper * 60
        old_dork_list = self.get_old_dork_pages_list(dirname)
        self.generate_dork_pages(True)
        self.remove_old_dork_pages(old_dork_list)
        if sleeper == 0:
            return
        if sleep_time < 60:
            sleep_time = 60
        # TODO: Improve this loop
        while True:
            time.sleep(sleep_time)
            old_dork_list = self.get_old_dork_pages_list(dirname)
            self.generate_dork_pages(False)
            self.remove_old_dork_pages(old_dork_list)
