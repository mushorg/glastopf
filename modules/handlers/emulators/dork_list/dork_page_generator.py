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

from random import choice, shuffle
import hashlib
import codecs
import unicodedata
import random
import dork_file_processor
import gen_html
import time
import os
import cluster
import logging

logger = logging.getLogger(__name__)


class DorkPageGenerator(object):
    """
    Responsible for maintenance of dork pages and collection of dorks from requests.
    """

    def __init__(self, dork_db_instance, database_instance, pages_path):
        self.dorkdb = dork_db_instance
        self.database = database_instance
        self.pages_path = pages_path

    def prepare_text(self):
        line_list = []
        with codecs.open("modules/handlers/emulators/dork_list/data/pride.txt", "r", "utf-8") as text_file:
            for text_line in text_file.readlines():
                text_line = text_line.strip()
                if text_line != "":
                    line_list.append(unicodedata.normalize('NFKD', text_line).encode('ascii', 'ignore'))
        return line_list

    def generate_dork_pages(self, first):
        if first:
            processor = dork_file_processor.DorkFileProcessor(self.dorkdb)
            dorks = processor.process_dorks()
            self.dorkdb.insert(dorks)
        line_list = self.prepare_text()
        shuffle(line_list)
        #inurl_list = dork_reader.get_dork_list('inurl')
        #db = database.DorkDB(self.dorkdb)
        inurl_list = self.database.select_data()
        #get data from dorkdb is the live database does not have enough
        if len(inurl_list) < 100:
            dork_seeds = random.sample(self.dorkdb.get_dork_list('inurl'), 100)
            inurl_list += dork_seeds
        c = cluster.Cluster()
        c.cluster(inurl_list, self.database.config)
        inurl_cluster = choice(c.clusters)
        intext_list = self.dorkdb.get_dork_list('intext')
        intitle_list = self.dorkdb.get_dork_list('intitle')
        while len(inurl_list) > 50 and len(line_list) > 56:
            body = ''
            for i in range(0, 49):
                body += line_list.pop()
                href = inurl_list.pop()
                body += " <a href='%s'>%s</a> " % (href, choice(intext_list))
            for i in range(0, 5):
                body += line_list.pop()
                href = choice(inurl_cluster)
                body += " <a href='%s'>%s</a> " % (href, choice(intext_list))
            dork_page = gen_html.html_template(choice(intitle_list),
                                               "http://localhost:8080",
                                               body,
                                               "Footer Powered By")
            page_md5 = hashlib.md5(dork_page).hexdigest()
            with codecs.open("{0}/{1}".format(self.pages_path, page_md5), "w", "utf-8") as dork_file:
                dork_file.write(dork_page)

    def get_current_pages(self):
        dork_page_list = []
        for f in os.listdir(self.pages_path):
            file_path = os.path.join(self.pages_path, f)
            if os.path.isfile(file_path):
                dork_page_list.append(file_path)
        return dork_page_list

    def remove_pages(self, oldpages):
        for file_path in oldpages:
            try:
                os.unlink(file_path)
            except Exception as e:
                raise

    def regular_generate_dork(self, sleeper):
        sleep_time = sleeper * 60
        old_pages = self.get_current_pages()
        self.generate_dork_pages(True)
        self.remove_pages(old_pages)
        if sleeper == 0:
            return
        if sleep_time < 60:
            sleep_time = 60
        while True:
            time.sleep(sleep_time)
            old_pages = self.get_current_pages()
            self.generate_dork_pages(False)
            self.remove_pages(old_pages)

    def collect_dork(self, attack_event):
        if attack_event.matched_pattern != "unknown":
            #dork_reader = dork_db.DorkDB(dork_db_path)
            try:
                dork = attack_event.parsed_request.url.split('?')[0]
                self.dorkdb.insert([{'table': "inurl", 'content': dork}])
            except Exception as e:
                logger.exception("Parsed_request split error: {0}".format(e))
