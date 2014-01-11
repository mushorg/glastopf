# Copyright (C) 2014 Johnny Vestergaard <jkv@unixcluster.dk>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from datetime import datetime
import uuid
import os
import hashlib
import base64

import jinja2
import glastopf

CAPEC_PATTERN_MAP = {'sqli': {'CAPEC-66': 'SQL Injection'},
                     'rfi':  {'CAPEC-193': 'PHP Remote File Inclusion'},
                     'lfi':  {'CAPEC-252': 'PHP Local File Inclusion'},
                     # worst case for php_cgi_rce, we need better classification in modules
                     'php_cgi_rce': {'CAPEC-193': 'PHP Remote File Inclusion'},
                     'login': {'CAPEC-112': 'Brute force'}}

# http headers accepted by cybox
CYBOX_HEADERS = set(['Accept', 'Accept_Charset', 'Accept_Language', 'Accept_Datetime', 'Accept_Encoding',
                     'Authorization', 'Cache_Control', 'Connection', 'Cookie', 'Content_Length', 'Content_MD5',
                     'Content_Type', 'Date', 'Expect', 'From', 'Host', 'If_Match', 'If_Modified_Since', 'If_None_Match',
                     'If_Range', 'If_Unmodified_Since', 'Max_Forwards', 'Pragma', 'Proxy_Authorization', 'Range',
                     'Referer', 'TE', 'User_Agent', 'Via', 'Warning', 'DNT', 'X_Requested_With', 'X_Requested_For',
                     'X_ATT_DeviceId', 'X_Wap_Profile'])

class StixTransformer(object):
    def __init__(self, config, data_dir):
        template_loader = jinja2.FileSystemLoader(searchpath=os.path.dirname(__file__))
        template_env = jinja2.Environment(loader=template_loader, trim_blocks=True, lstrip_blocks=True)
        self.template = template_env.get_template('stix_glastopf_template.xml')
        self.config = config
        self.files_dir = os.path.join(data_dir, 'files/')


    def transform(self, event):

        jinja_vars = {'package_id': str(uuid.uuid4()),
                'namespace': 'Glastopf',
                'namespace_uri': 'http://glastopf.org/stix-1',
                'package_timestamp': datetime.utcnow().isoformat(),
                'incident_id': event.id,
                'incident_timestamp': datetime.strptime(event.event_time,"%Y-%m-%d %H:%M:%S").isoformat(),
                'glastopf_version': glastopf.__version__,
                'include_contact_info': self.config.getboolean('taxii', 'include_contact_info'),
                'contact_name': self.config.get('taxii', 'contact_name'),
                'contact_mail': self.config.get('taxii', 'contact_email'),
                'source_ip': event.source_addr[0],
                'source_port': str(event.source_addr[1]),
                'honeypot_ip': event.sensor_addr[0],
                'honeypot_port': event.sensor_addr[1],
                'http_method': event.http_request.request_verb,
                'http_version': event.http_request.request_version,
                'http_path': event.http_request.request_path,
                'http_body': event.http_request.request_body,
                'http_raw_header': event.http_request.headers,
                'http_parsed_header': self._get_parsed_header(event),
                'capec': self._pattern_to_capec(event)
        }

        if event.file_name is not None:
            with file(os.path.join(self.files_dir, event.file_name), 'r') as file_handler:
                file_data = file_handler.read()
                file_content = base64.b64encode(file_data)
                jinja_vars['file_content'] = file_content
                jinja_vars['file_hash_md5'] = hashlib.md5(file_data).hexdigest()
                jinja_vars['file_hash_sha256'] = hashlib.sha256(file_data).hexdigest()
                jinja_vars['file_observable_object_id'] = str(uuid.uuid4())

        return self.template.render(jinja_vars)

    def _get_parsed_header(self, event):
        parsed_header = []
        for header_name in event.http_request.headers:
            # make candidate header fit the cybox definitions
            header_name_cap = header_name.title().replace('-', '_')
            if header_name_cap in CYBOX_HEADERS:
                parsed_header.append((header_name_cap, event.http_request.headers.get(header_name, "")))
        return parsed_header

    def _pattern_to_capec(self, event):
        if event.matched_pattern in CAPEC_PATTERN_MAP:
            return CAPEC_PATTERN_MAP[event.matched_pattern]
        else:
            return {}
