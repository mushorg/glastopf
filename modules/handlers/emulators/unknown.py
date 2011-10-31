import os
from random import choice, shuffle
import codecs

class DorkList(object):
    
    def __init__(self):
        pass
    
    def get_response(self):
        dork_page_list = os.listdir("modules/handlers/emulators/dork_list/pages")
        shuffle(dork_page_list)
        with codecs.open("modules/handlers/emulators/dork_list/pages/" + choice(dork_page_list), "r", "utf-8") as dork_page:
            #return dork_page.read().decode('iso-8859-1')
            return dork_page.read().encode('ascii')