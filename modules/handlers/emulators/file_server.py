# Proposed and drafted by Phani Vadrevu

import os


class FileServer(object):
    def __init__(self):
        pass

    def handle(self, attack_event):
        request_file = attack_event.parsed_request.url.lstrip('/')
        with open(os.path.join('modules/handlers/emulators/server_files',
                                request_file), 'r') as f:
            attack_event.response += f.read()
        return attack_event
