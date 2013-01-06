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

import gen_html
import process_dork_file
import dork_db
import time
import os
import database
import cluster


def prepare_text():
    line_list = []
    with codecs.open("modules/handlers/emulators/dork_list/pride.txt", "r", "utf-8") as text_file:
        for text_line in text_file.readlines():
            text_line = text_line.strip()
            if text_line != "":
                line_list.append(unicodedata.normalize('NFKD', text_line).encode('ascii', 'ignore'))
    return line_list


def generate_dork_pages(first):
    if first:
        processor = process_dork_file.DorkFileProcessor()
        processor.process_dorks()
    line_list = prepare_text()
    shuffle(line_list)
    dork_reader = dork_db.DorkDB()
    #inurl_list = dork_reader.get_dork_list('inurl')
    db = database.DorkDB()
    inurl_list = db.select_data()
    c = cluster.Cluster()
    c.cluster(inurl_list, db.config)
    inurl_cluster = choice(c.clusters)
    intext_list = dork_reader.get_dork_list('intext')
    intitle_list = dork_reader.get_dork_list('intitle')
    while len(inurl_list) > 50 and len(line_list) > 56:
        body = ''
        for i in range(0, 49):
            body += line_list.pop()
            href = inurl_list.pop()
            body += " <a href='%s'>%s</a> " % (href, choice(intext_list)[0])
        for i in range(0, 5):
            body += line_list.pop()
            href = choice(inurl_cluster)
            body += " <a href='%s'>%s</a> " % (href, choice(intext_list)[0])
        dork_page = gen_html.html_template(choice(intitle_list)[0],
                                           "http://localhost:8080",
                                           body,
                                           "Footer Powered By")
        page_md5 = hashlib.md5(dork_page).hexdigest()
        with codecs.open("modules/handlers/emulators/dork_list/pages/%s" % page_md5, "w", "utf-8") as dork_file:
            dork_file.write(dork_page)


def get_old_dork_pages_list(folder):
    dork_lists = []
    for f in os.listdir(folder):
        file_path = os.path.join(folder, f)
        if os.path.isfile(file_path):
            dork_lists.append(file_path)
    return dork_lists


def remove_old_dork_pages(old_dork_list):
    for file_path in old_dork_list:
        try:
            os.unlink(file_path)
        except Exception, e:
            pass


def regular_generate_dork(sleeper, dirname='modules/handlers/emulators/dork_list/pages/'):
    sleep_time = sleeper * 60
    old_dork_list = get_old_dork_pages_list(dirname)
    generate_dork_pages(True)
    remove_old_dork_pages(old_dork_list)
    if sleeper == 0:
        return
    if sleep_time < 60:
        sleep_time = 60
    while True:
        time.sleep(sleep_time)
        old_dork_list = get_old_dork_pages_list(dirname)
        generate_dork_pages(False)
        remove_old_dork_pages(old_dork_list)


def collect_dork(attack_event):
    if attack_event.matched_pattern != "unknown":
        dork_reader = dork_db.DorkDB()
        try:
            dork = attack_event.parsed_request.url.split('?')[0]
            dork_reader.insert([{'table': "inurl", 'content': dork}])
        except Exception as e:
            print "parsed_request split error for '?':", e
