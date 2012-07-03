import os
from random import choice
import codecs
from urlparse import parse_qs


class CommentPoster(object):
    def __init__(self):
        pass

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
            except KeyError:
                comment = ""
            attack_event.response = dork_page.read() + comment
