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
import tempfile
import shutil
import unittest
import ConfigParser

from glastopf.glastopf import GlastopfHoneypot
from glastopf.modules.handlers.emulators.surface import create_surface


class TestSurfaceCreation(unittest.TestCase):

    def setUp(self):
        self.workdir = tempfile.mkdtemp()
        self.datadir = os.path.join(self.workdir, 'data')
        GlastopfHoneypot.prepare_environment(self.workdir)

    def tearDown(self):
        shutil.rmtree(self.workdir)

    def test_template(self):
        surface_creator = create_surface.SurfaceCreator(data_dir=self.datadir)
        print surface_creator.get_index()

    def test_meta(self):
        """
        Objective: Test google/bing page verification support.
        """
        test_meta = ['0cfa9f600839f57e90e5559b8ee54864', 'fbeefa5876ae12675451e144530b2f66']
        config = ConfigParser.RawConfigParser()
        config.add_section('surface')
        config.set('surface', 'google_meta', test_meta[0])
        config.set('surface', 'bing_meta', test_meta[1])
        surface_creator = create_surface.SurfaceCreator(data_dir=self.datadir, conf_parser=config)
        for meta in test_meta:
            self.assertTrue(meta in surface_creator.get_index())

if __name__ == '__main__':
    unittest.main()
