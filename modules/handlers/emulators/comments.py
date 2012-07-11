import os
from random import choice
import codecs
from urlparse import parse_qs
from string import Template
import cgi


class CommentPoster(object):
    def __init__(self):
        pass

    def html_escape(self, comment):
        return cgi.escape(comment)

    def handle(self, attack_event):
        dork_page_list = os.listdir("modules/handlers/emulators/"
                                    "dork_list/pages")
        if '.svn' in dork_page_list:
            dork_page_list.remove('.svn')
        dork_page = choice(dork_page_list)
        with codecs.open("modules/handlers/emulators/dork_list/pages/" +
                            dork_page, "r", "utf-8") as dork_page:
            try:
                comment = (parse_qs(attack_event.parsed_request.body)
                            ['comment'][0])
                comment = self.html_escape(comment)
                comment = "<br/><br/>" + comment
            except KeyError:
                comment = ""
            else:
                with codecs.open("modules/handlers/emulators/dork_list/"
                                 "comments.txt", "a", "utf-8") as comments_txt:
                    comments_txt.write(comment)
            with codecs.open("modules/handlers/emulators/dork_list/"
                             "comments.txt", "r", "utf-8") as comments_txt:
                template = Template(dork_page.read())
                attack_event.response = template.safe_substitute(
                                                login_msg="",
                                                comments=comments_txt.read())
