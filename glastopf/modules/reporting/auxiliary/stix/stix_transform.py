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
        self.config = config._sections['taxii']
        self.template = template_env.get_template('stix_glastopf_template.xml')

    def transform(self, event):
        vars = {'package_id': str(uuid.uuid4()),
                'namespace': 'Glastopf',
                'namespace_uri': 'http://glastopf.org/stix-1',
                'package_timestamp': datetime.utcnow().isoformat(),
                'incident_id': event['session_id'],
                'incident_timestamp': event['timestamp'].isoformat(),
                'glastopf_version': glastopf.__version__,
                'include_contact_info': self.config['include_contact_info'],
                'contact_name': self.config['contact_name'],
                'contact_mail': self.config['contact_email']}

        return self.template.render(vars)