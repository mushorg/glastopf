# Proposed and drafted by Phani Vadrevu

import os


class FileServer(object):
    def __init__(self):
        pass

    def handle(self, attack_event):
        server_path = 'modules/handlers/emulators/server_files'
        request_file = attack_event.parsed_request.url.lstrip('/')
        if request_file == "":
            request_file = "index.html"
        if os.path.isfile(os.path.join(server_path, request_file)):
            with open(os.path.join(server_path, request_file), 'r') as f:
                attack_event.response += f.read()
        return attack_event
