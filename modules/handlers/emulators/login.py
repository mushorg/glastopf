import os
from random import choice
import codecs
from urlparse import parse_qs
from string import Template


class LoginEmulator(object):
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
            url_dict = parse_qs(attack_event.parsed_request.body)
            if ('login' in url_dict) or ('password' in url_dict):
                login_msg = "Incorrect login or password! Please try again."
            else:
                login_msg = ""
            with codecs.open("modules/handlers/emulators/dork_list/"
                             "comments.txt", "r", "utf-8") as comments_txt:
                template = Template(dork_page.read())
                attack_event.response = template.safe_substitute(
                                                login_msg=login_msg,
                                                comments=comments_txt.read())
