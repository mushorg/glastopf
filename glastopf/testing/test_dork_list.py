# Copyright (C) 2015 Lukas Rist
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

from random import choice
import unittest
import os
import shutil
import tempfile

from lxml.html.soupparser import fromstring
from lxml.etree import tostring

from glastopf.glastopf import GlastopfHoneypot
from glastopf.modules.HTTP.handler import HTTPHandler
from glastopf.testing import helpers
from glastopf.modules.handlers.emulators.dork_list.dork_page_generator import DorkPageGenerator
from glastopf.modules.handlers.emulators.dork_list.dork_file_processor import DorkFileProcessor
from glastopf.modules.handlers.emulators.dork_list import database_mongo
from glastopf.modules.handlers.emulators.dork_list import database_sqla
from glastopf.modules.events import attack

from sqlalchemy import create_engine
from ConfigParser import ConfigParser


class TestEmulatorDorkList(unittest.TestCase):
    """Tests the honeypots vulnerable string selection.
    We first start with the integration test and continue with unit tests.
    The test script will connect to an mongodb instance on localhost, and populate
    with data a needed."""

    def setUp(self):
        self.config = ConfigParser()
        self.config.add_section('main-database')
        self.config.set('main-database', 'enabled', "True")
        self.workdir = tempfile.mkdtemp()
        self.datadir = os.path.join(self.workdir, 'data')
        GlastopfHoneypot.prepare_environment(self.workdir)

    def tearDown(self):
        shutil.rmtree(self.workdir)

    def dork_generator_chain(self, dbtype):
        """
        Helper method to constructs chain of objects to satify dependencies for the dork_generator.
        Returns an instance of dork_page_generator.
        """

        engine = None
        if dbtype == "sql":
            engine = create_engine('sqlite:///')
            # Create mock of empty main db
            helpers.populate_main_sql_testdatabase(engine)
            db = database_sqla.Database(engine)
        elif dbtype == "mongodb":
            conn_string = helpers.create_mongo_database(fill=True)
            db = database_mongo.Database(helpers.create_mongo_database)
        else:
            raise Exception("Unsupported database type: {0}".format(dbtype))
        reduced_dorks_file = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'data/dorks_reduced.txt')
        file_processor = DorkFileProcessor(db, dorks_file=reduced_dorks_file)
        dork_generator = DorkPageGenerator(db, file_processor, self.datadir, conf_parser=self.config)
        return db, engine, dork_generator

    def test_db_select_sqlalchemy(self):
        """Objective: Select unique request paths from database.
        Input: Connection to main glastopf database with 500 entries and the pattern 'rfi'.
        Expected Results: 10 data entries in total.
        """

        (db, engine, dork_generator) = self.dork_generator_chain('sql')
        dork_generator.regular_generate_dork(0)
        print("Starting database SELECT test...")
        result = db.select_data("rfi")
        self.assertEqual(len(result), 10)

    def test_automated_extension(self):
        """Objective: Test if the dork database extends on new requests to the honeypot.
        Input: A test request with URL: http://localhost:8080/test.php?c=test
        Expected Results: An entry in the 'inurl' db table containing '/test.php'.
        Notes: The test adds the '/test.php' entry to the database."""
        attack_event = attack.AttackEvent()
        attack_event.matched_pattern = "internal_test"
        attack_event.http_request = HTTPHandler('GET /thiswillNeVeRHaPPend.php?c=test', None)
        print("Attack event prepared.")
        (db, engine, dork_generator) = self.dork_generator_chain('sql')
        dork_generator.regular_generate_dork(0)
        dork_generator.collect_dork(attack_event)
        print("Done collecting the path from the event and writing to the database.")
        sql = "SELECT * FROM inurl WHERE content = :x"
        result = engine.connect().execute(sql, x='/thiswillNeVeRHaPPend.php').fetchall()
        print("Done fetching the entries matching the request URL")
        self.assertTrue(len(result) > 0)
        print("Number of entries in the database matching our URL:")
        print(len(result))
        print("which equates our expectation.")

    def test_dork_page(self):
        """Objective: Tests if the attack surface generation works.
        Input: Data from the dork database.
        Expected Results: HTML pages ready to be served to the adversary.
        Notes: This test covers the generation of the HTML pages from the dork database.
        The page number is proportional to database entries."""

        print("Starting dork page test.")

        (db, engine, dork_generator) = self.dork_generator_chain('sql')
        dork_generator.regular_generate_dork(0)
        print("Done creating dork pages.")
        current_pages = dork_generator.get_current_pages()
        self.assertTrue(len(current_pages) > 0)
        print("Number of created HTML pages:")
        print(len(current_pages))
        print("equates our expectation.")

    def test_dork_page_content(self):
        """Objective: Testing the attack surfaces content.
        Input: An attack surface sample. The structure is defined in a template.
        Expected Results: The attack surface should be a HTML page containing text and links.
        Notes: We extract and count the elements in the HTML document."""

        dork_generator = self.dork_generator_chain('sql')[2]
        dork_generator.regular_generate_dork(0)
        sample_file = choice(dork_generator.get_current_pages())
        with open(sample_file, 'r') as sample_data:
            data = fromstring(sample_data)
        self.assertTrue(len(data.cssselect('a')) > 0)
        self.assertTrue(len(data.cssselect('title')) > 0)
        self.assertTrue(len(data.cssselect('form')) > 0)
        print("The content analysis of a random HTML page returned:")
        print(len(data.cssselect('a')), 'links (<a href=""></a>)')
        print(len(data.cssselect('title')), 'page title (<title />)')
        print(len(data.cssselect('form')), 'form field (<form />)')
        print("which equates our expectation.")

    def test_dork_page_regeneration(self):
        """Objective: Test if the dork pages get regenerated.
        Input: The list of previously generated dork pages.
        Expected Results: A new list of dork pages.
        Notes: A productive system generates new pages in a configurable interval."""

        (db, engine, dork_generator) = self.dork_generator_chain('sql')
        dork_generator.regular_generate_dork(0)
        old_list = dork_generator.get_current_pages()
        print("There are %s previously generated dork pages" % len(old_list))
        old_sample_file = choice(old_list)
        print("For example:", old_sample_file.rsplit('/', 1)[1])
        dork_generator.regular_generate_dork(0)
        print("Done generating new dork pages.")
        print("Old dork pages has been removed.")
        new_list = dork_generator.get_current_pages()
        overlap = set(new_list).intersection(old_list)
        self.assertTrue(len(overlap) == 0)
        print("There are", len(overlap), "overlapping dork pages")
        print("which equates our expectation.")


if __name__ == '__main__':
    unittest.main()
