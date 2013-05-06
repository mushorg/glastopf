# Copyright (C) 2012  Lukas Rist <glaslos@gmail.com>
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

import os

from glastopf.modules.handlers import base_emulator

from jinja2 import Environment, FileSystemLoader
from ConfigParser import ConfigParser 


class SurfaceCreator(base_emulator.BaseEmulator):
    def __init__(self, data_dir):
        super(SurfaceCreator, self).__init__(data_dir)
        self.template_env = Environment(loader=FileSystemLoader(os.path.join(self.data_dir, "templates")))

    def get_index(self, title="Title Title", target="/index", body="Some Body", footer="Footer Text"):
        template = self.template_env.get_template('index.html')
        config = os.path.join(self.data_dir, '../glastopf.cfg') #config file
        conf_parser = ConfigParser()
        conf_parser.read(config) 
        head_g = conf_parser.get('surface', 'google_meta').strip() #remove all blank space from ID 
        head_b = conf_parser.get('surface', 'bing_meta').strip()
        head_google = ""
        head_bing = ""
        if head_g:
            head_google = "<meta name=\"google-site-verification\" content=\"%s\" />" % head_g
        if head_b:
            head_bing = "<meta name=\"msvalidate.01\" content=\"%s\" />" % head_b  
        surface_page = template.render(title=title, head_metag=head_google, head_metab=head_bing, target=target, body=body, footer=footer)
        return surface_page


if __name__ == "__main__":
    sc = SurfaceCreator()
    sc.get_index()
