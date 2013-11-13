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
import time
import os
import logging

from glastopf.modules.handlers.emulators.dork_list import gen_html
from glastopf.modules.handlers.emulators.surface import create_surface


logger = logging.getLogger(__name__)
package_directory = os.path.dirname(os.path.abspath(__file__))


class DorkPageGenerator(object):
    """
    Responsible for maintenance of dork pages and collection of dorks from requests.
    """

    def __init__(self,
                 database_instance,
                 dorks_file_processor_instance,
                 data_dir,
                 pages_dir=None,
                 mnem_service_instance=None):
        self.database = database_instance
        if not pages_dir:
            self.pages_path = os.path.join(data_dir, 'dork_pages')
        else:
            self.pages_path = os.path.join(pages_dir, 'dork_pages')
        if not os.path.isdir(self.pages_path):
            os.mkdir(self.pages_path, 0770)
        self.dork_file_processor = dorks_file_processor_instance
        self.mnem_service = mnem_service_instance

        #check if we need bootstrapping
        if len(self.database.get_dork_list('inurl')) == 0:
            logger.info("Bootstrapping dork database.")
            self.bootstrap_dorkdb()
        self.enabled = True
        self.surface_creator = create_surface.SurfaceCreator(data_dir=data_dir)

    def prepare_text(self):
        line_list = []
        text_file = os.path.join(package_directory, 'data/pride.txt')
        with codecs.open(text_file, "r", "utf-8") as text_file:
            for text_line in text_file.readlines():
                text_line = text_line.strip()
                if text_line != "":
                    line_list.append(unicodedata.normalize('NFKD', text_line).encode('ascii', 'ignore'))
        return line_list

    def generate_dork_pages(self):

        line_list = self.prepare_text()
        shuffle(line_list)

        inurl_list = self.database.select_data()
        #get data from dorkdb if the live database does not have enough
        if len(inurl_list) < 100:
            dork_seeds = random.sample(self.database.get_dork_list('inurl'), 100)
            inurl_list += dork_seeds

        intext_list = self.database.get_dork_list('intext')
        intitle_list = self.database.get_dork_list('intitle')
        while len(inurl_list) > 50 and len(line_list) > 56:
            body = ''
            for i in range(0, 54):
                body += line_list.pop()
                href = inurl_list.pop()
                body += " <a href='%s'>%s</a> " % (href, choice(intext_list))
            dork_page = self.surface_creator.get_index(choice(intitle_list),
                                                       "/index",
                                                       body,
                                                       "Footer Powered By")
            page_md5 = hashlib.md5(dork_page).hexdigest()
            with codecs.open("{0}/{1}".format(self.pages_path, page_md5), "w", "utf-8") as dork_file:
                dork_file.write(dork_page)

    def get_current_pages(self):
        dork_page_list = []
        for f in os.listdir(self.pages_path):
            if f.startswith("."):
                continue
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
        self.generate_dork_pages()
        self.remove_pages(old_pages)
        if sleeper == 0:
            return
        if sleep_time < 60:
            sleep_time = 60
        while self.enabled:
            time.sleep(sleep_time)
            old_pages = self.get_current_pages()
            self.generate_dork_pages()
            self.remove_pages(old_pages)

    def collect_dork(self, attack_event):
        if attack_event.matched_pattern != "unknown":
            try:
                dork = attack_event.http_request.path.split('?')[0]
                self.database.insert_dorks([{'table': "inurl", 'content': dork}])
            except Exception as e:
                logger.exception("http_request split error: {0}".format(e))

    def bootstrap_dorkdb(self):
        ignore = ()
        dorks = []
        if self.mnem_service:
            #get dorks from mnemosyne - note: only 'inurl' at the moment
            dorks = self.mnem_service.get_dorks()
            if len(dorks) > 0:
                #all went well, do not extract inurl from file
                ignore = ('inurl')
            else:
                #something went wrong (nothing extracted from mnemosyne), extract all types from file
                ignore = ()

        #combine mnemosyne dorks with file dorks - accordingly to the ignore filter.
        dorks += self.dork_file_processor.process_dorks(ignore)
        self.database.insert_dorks(dorks)
