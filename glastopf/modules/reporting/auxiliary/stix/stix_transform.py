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

import jinja2
import glastopf


class StixTransformer(object):
    def __init__(self, config):
        template_loader = jinja2.FileSystemLoader(searchpath=os.path.dirname(__file__))
        template_env = jinja2.Environment(loader=template_loader)
        self.template = template_env.get_template('stix_glastopf_template.xml')

        self.config = config
        self.capec_mapping = {'sqli': {'CAPEC-66': 'SQL Injection'},
                              'rfi':  {'CAPEC-193': 'PHP Remote File Inclusion'},
                              'lfi':  {'CAPEC-252': 'PHP Local File Inclusion'},
                              #worst case for php_cgi_rce, we need better classification in modules
                              'php_cgi_rce': {'CAPEC-193': 'PHP Remote File Inclusion'}}

    def transform(self, event):

        headers = []
        for w in event.http_request.headers:
            headers.append((w, event.http_request.headers.get(w, "")))

        vars = {'package_id': str(uuid.uuid4()),
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
                'http_parsed_header': headers,
                'capec': self._pattern_to_capec(event)
        }

        return self.template.render(vars)

    def _pattern_to_capec(self, event):
        print event.matched_pattern
        if event.matched_pattern in self.capec_mapping:
            return self.capec_mapping[event.matched_pattern]
        else:
            return {}
