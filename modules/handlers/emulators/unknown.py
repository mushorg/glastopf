import os
from random import choice
import codecs
import sys
from string import Template

import modules.processing.profiler as profiler


if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')  # for the different python version
                                     # unicode problem


class DorkList(object):
    def __init__(self):
        pass

    def get_response(self, attack_event):
        dork_page_list = os.listdir("modules/handlers/emulators/dork_list"
                                    "/pages")
        if '.svn' in dork_page_list:
            dork_page_list.remove('.svn')
        dork_page = choice(dork_page_list)
        ip_address = attack_event.source_addr[0]
        with codecs.open("modules/handlers/emulators/dork_list/pages/" +
                         dork_page, "r", "utf-8") as dork_page:
            with codecs.open("modules/handlers/emulators/dork_list/"
                             "comments.txt", "r", "utf-8") as comments_txt:
                general_comments = comments_txt.read()
                ip_comments = profiler.Profiler.get_comments(ip_address)
                display_comments = str(ip_comments) + str(general_comments)
                template = Template(dork_page.read())
                return template.safe_substitute(login_msg="",
                                                comments=display_comments)
