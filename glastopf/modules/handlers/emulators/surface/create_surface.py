# Copyright (C) 2015 Lukas Rist <glaslos@gmail.com>
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


class SurfaceCreator(base_emulator.BaseEmulator):
    def __init__(self, data_dir, conf_parser=None):
        super(SurfaceCreator, self).__init__(data_dir)
        self.conf_parser = conf_parser
        self.template_env = Environment(loader=FileSystemLoader(os.path.join(self.data_dir, "templates")))

    def get_index(self, title="Title Title", target="/index", body="Some Body", footer="Footer Text"):
        template = self.template_env.get_template('index.html')
        google_meta = ""
        bing_meta = ""
        try:
            meta_g = self.conf_parser.get('surface', 'google_meta')
            meta_b = self.conf_parser.get('surface', 'bing_meta')
            if meta_g:
                google_meta = "<meta name=\"google-site-verification\" content=\"%s\" />" % meta_g
            if meta_b:
                bing_meta = "<meta name=\"msvalidate.01\" content=\"%s\" />" % meta_b
        except:
            pass
        surface_page = template.render(
            title=title,
            google_meta=google_meta, bing_meta=bing_meta,
            target=target, body=body, footer=footer)
        return surface_page
