from string import Template
import hashlib
import time

class PMAEmulator(object):
    def __init__(self):
        pass

    def handle(self, attack_event):
        page = ""
        with open('modules/handlers/emulators/phpmyadmin/script_setup.php', 'r') as setup_php:
            page += setup_php.read()
        m = hashlib.md5()
        m.update("%d" % time.time() )
        page_template = Template(page)
        attack_event.response += page_template.substitute( token_value = m.hexdigest())
        return attack_event
