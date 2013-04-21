import os
from random import choice
import codecs
from urlparse import parse_qs
from string import Template
import cgi
from glastopf.modules.handlers import base_emulator

#import glastopf.modules.processing.profiler as profiler


class CommentPoster(base_emulator.BaseEmulator):
    MAX_COMMENT_LEN = 2048
    MAX_FILE_LEN = 33816700  # ~ 3MB

    def __init__(self, data_dir):
        super(CommentPoster, self).__init__(data_dir)

    def html_escape(self, comment):
        return cgi.escape(comment)

    def handle(self, attack_event):
        # TODO: Use the unknown emulators _get_template function.
        pages_path = os.path.join(self.data_dir, 'dork_pages')
        dork_page_list = os.listdir(pages_path)
        dork_page = choice(dork_page_list)
        ip_address = attack_event.source_addr[0]

        comments_file = os.path.join(self.data_dir, 'comments.txt')

        with codecs.open(os.path.join(pages_path, dork_page)) as dork_page:
            try:
                comment = (parse_qs(attack_event.http_request.request_body)
                           ['comment'][0])
                clean_comment = self.html_escape(comment)
                clean_comment = "<br/><br/>" + clean_comment
                comment = "<br/><br/>" + comment
            except KeyError:
                comment = ""
                clean_comment = ""
            else:

                # overwrite the comments file if its size exceeds the max length
                if os.path.isfile(comments_file):
                    if os.stat(comments_file).st_size > CommentPoster.MAX_FILE_LEN:
                        with codecs.open(comments_file, "w", "utf-8") as comments_txt:
                            comments_txt.write('')

                # store the comment only if its size does not exceed the max length
                if len(clean_comment) <= CommentPoster.MAX_COMMENT_LEN:
                    with codecs.open(comments_file, "a", "utf-8") as comments_txt:
                        comments_txt.write(clean_comment)

            if os.path.isfile(comments_file):
                with codecs.open(comments_file, "r", "utf-8") as comments_txt:
                    general_comments = comments_txt.read()
            else:
                general_comments = ''

            display_comments = str(general_comments)
            template = Template(dork_page.read())
            response = template.safe_substitute(login_msg="", comments=display_comments)
            attack_event.http_request.set_response(response)
