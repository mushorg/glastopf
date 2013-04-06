# Copyright (C) 2013  Lukas Rist <glaslos@gmail.com>
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

import unittest

from glastopf.modules.handlers.emulators.surface import create_surface


class TestSurfaceCreation(unittest.TestCase):

    def test_template(self):
        data_dir = os.getcwd() + "/modules/handlers/emulators/data"
        surface_creator = create_surface.SurfaceCreator(data_dir=data_dir)
        print surface_creator.get_index()