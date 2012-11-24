import os
from random import choice
import codecs
from urlparse import parse_qs
from string import Template
import cgi

import modules.processing.profiler as profiler

from modules.handlers import base_emulator


class CommentPoster(base_emulator.BaseEmulator):
    def __init__(self):
        pass

    def html_escape(self, comment):
        return cgi.escape(comment)

    def handle(self, attack_event):
        # TODO: Use the unknown emulators _get_template function.
        pages_path = "modules/handlers/emulators/dork_list/pages"
        dork_page_list = os.listdir(pages_path)
        if '.git' in dork_page_list:
            dork_page_list.remove('.git')
        dork_page = choice(dork_page_list)
        ip_address = attack_event.source_addr[0]
        with codecs.open("modules/handlers/emulators/dork_list/pages/" +
                            dork_page, "r", "utf-8") as dork_page:
            try:
                comment = (parse_qs(attack_event.parsed_request.body)
                            ['comment'][0])
                clean_comment = self.html_escape(comment)
                clean_comment = "<br/><br/>" + clean_comment
                comment = "<br/><br/>" + comment
            except KeyError:
                comment = ""
                clean_comment = ""
            else:
                with codecs.open("modules/handlers/emulators/dork_list/"
                                 "comments.txt", "a", "utf-8") as comments_txt:
                    comments_txt.write(clean_comment)
                profiler.Profiler.add_comment(ip_address, comment)
            with codecs.open("modules/handlers/emulators/dork_list/"
                             "comments.txt", "r", "utf-8") as comments_txt:
                general_comments = comments_txt.read()
                ip_comments = profiler.Profiler.get_comments(ip_address)
                display_comments = str(ip_comments) + str(general_comments)
                template = Template(dork_page.read())
                attack_event.response = template.safe_substitute(
                                                login_msg="",
                                                comments=display_comments)
