# Copyright (C) 2015 Johnny Vestergaard
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

import unittest

from glastopf.modules.handlers.emulators.dork_list import mnem_service


class TestMnemosyneService(unittest.TestCase):
    @unittest.skip("Mnemosyne service down until further notice")
    def test_extractions(self):
        """
        Basic test to check if we can extract dorks from the mnemosyne dorks service.
        """

        sut = mnem_service.Mnem_Service()
        dorks = sut.get_dorks(username='glastopf_test', password='glastopf_test', limit=10)
        self.assertTrue(len(dorks) > 0)

    @unittest.skip("Mnemosyne service down until further notice")
    def test_error_login(self):
        """
        Test if we fail soft on login errors.
        The  mnemosyne module is designed to return an empty list on errors.
        """

        #using wrong username/pass to simulate an error
        sut = mnem_service.Mnem_Service()
        dorks = sut.get_dorks(username='glastopf_test_invalid', password='glastopf_test_invalid')
        self.assertTrue(len(dorks) == 0)


if __name__ == '__main__':
    unittest.main()
