import os
from random import choice
import codecs
import sys
from string import Template

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8') # for the different python version 
                                    # unicode problem

class DorkList(object):
    def __init__(self):
        pass

    def get_response(self):
        dork_page_list = os.listdir("modules/handlers/emulators/dork_list"
                                    "/pages")
        if '.svn' in dork_page_list:
            dork_page_list.remove('.svn')
        dork_page = choice(dork_page_list)
        with codecs.open("modules/handlers/emulators/dork_list/pages/" + 
                         dork_page, "r", "utf-8") as dork_page:
            with codecs.open("modules/handlers/emulators/dork_list/"
                             "comments.txt", "r", "utf-8") as comments_txt:
                template = Template(dork_page.read())
                return template.safe_substitute(login_msg="",
                                                comments=comments_txt.read())
