import os
from random import choice
import codecs
from urlparse import parse_qs
from string import Template
import cgi
from glastopf.modules.handlers import base_emulator

import glastopf.modules.processing.profiler as profiler


class CommentPoster(base_emulator.BaseEmulator):
    def __init__(self, data_dir):
        super(CommentPoster, self).__init__(data_dir)

    def html_escape(self, comment):
        return cgi.escape(comment)

    def handle(self, attack_event):
        # TODO: Use the unknown emulators _get_template function.
        pages_path = os.path.join(self.data_dir, 'dork_pages')
        dork_page_list = os.listdir(pages_path)
        if '.git' in dork_page_list:
            dork_page_list.remove('.git')
        dork_page = choice(dork_page_list)
        ip_address = attack_event.source_addr[0]
        with codecs.open(os.path.join(pages_path, dork_page)) as dork_page:
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
                with codecs.open(os.path.join(self.data_dir, 'comments.txt'), "a", "utf-8") as comments_txt:
                    comments_txt.write(clean_comment)
                profiler.Profiler.add_comment(ip_address, comment)
            with codecs.open(os.path.join(self.data_dir, 'comments.txt'), "r", "utf-8") as comments_txt:
                general_comments = comments_txt.read()
                ip_comments = profiler.Profiler.get_comments(ip_address)
                display_comments = str(ip_comments) + str(general_comments)
                template = Template(dork_page.read())
                attack_event.response = template.safe_substitute(
                                                login_msg="",
                                                comments=display_comments)
