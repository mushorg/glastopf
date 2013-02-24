# Copyright (C) 2012  Lukas Rist
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
import sys
import os

from glastopf.testing import test_honeypot, test_dork_list, HTMLTestRunner

from glastopf.testing import test_sqli, test_emulators, test_classifiers

if sys.version_info[1] == 6:
    test_list = unittest.TestSuite()
else:
    test_list = unittest.suite.TestSuite()

test_list.addTests(unittest.TestLoader().loadTestsFromModule(test_honeypot))
test_list.addTests(unittest.TestLoader().loadTestsFromModule(test_emulators))
test_list.addTests(unittest.TestLoader().loadTestsFromModule(test_sqli))
test_list.addTests(unittest.TestLoader().loadTestsFromModule(test_dork_list))
test_list.addTests(unittest.TestLoader().loadTestsFromModule(test_classifiers))


if __name__ == '__main__':
    report_name = "report.html"
    reports_dir = "testing/reports"
    if not os.path.isdir(reports_dir):
        os.mkdir(reports_dir)
    outfile = open("testing/reports/" + report_name, "w")
    html_test = HTMLTestRunner
    runner = html_test.HTMLTestRunner(
                    stream=outfile,
                    verbosity=3,
                    title="""Glastopf v3:  Web Application Honeypot - Automated Test Report""",
                    description="""Test results of the implementation and unit tests."""
                    )
    html_test.stdout_redirector.write("""Web Application Honeypot Integration and Unit Testing.\n\n""")
    runner.run(test_list)
    print "Report will be available at testing/reports/" + report_name
