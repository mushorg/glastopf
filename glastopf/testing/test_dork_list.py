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

from random import choice
import unittest
import os
import shutil
import tempfile

from lxml.html.soupparser import fromstring
from glastopf.modules.HTTP import util
from glastopf.testing import helpers
from glastopf.modules.handlers.emulators.dork_list.dork_page_generator import DorkPageGenerator
from glastopf.modules.handlers.emulators.dork_list.dork_file_processor import DorkFileProcessor
from glastopf.modules.handlers.emulators.dork_list import database_mongo
from glastopf.modules.handlers.emulators.dork_list import database_sqla
from glastopf.modules.handlers.emulators.dork_list import cluster
from glastopf.modules.events import attack
from sqlalchemy import create_engine


class TestEmulatorDorkList(unittest.TestCase):
    """Tests the honeypots vulnerable string selection.
    We first start with the integration test and continue with unit tests.
    The test script will connect to an mongodb instance on localhost, and populate
    with data a needed."""

    def dork_generator_chain(self, dbtype, pages_dir):
        """
        Helper method to constructs chain of objects to satify dependencies for the dork_generator.
        Returns an instance of dork_page_generator.
        """

        if dbtype == "sql":
            engine = create_engine('sqlite:///')
            #Create mock of empty main db
            helpers.populate_main_sql_testdatabase(engine)
            db = database_sqla.Database(engine)
        elif dbtype == "mongodb":
            conn_string = helpers.create_mongo_database(fill=True)
            db = database_mongo.Database(helpers.create_mongo_database)
        else:
            raise Exception("Unsupported database type: {0}".format(dbtype))
        reduced_dorks_file = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'data/dorks_reduced.txt')
        file_processor = DorkFileProcessor(db, dorks_file=reduced_dorks_file)
        #setting the bar low for testing
        clusterer = cluster.Cluster("/\w+", 1, 1, 1, min_df=0.0)
        data_dir = os.getcwd() + "/modules/handlers/emulators/data"
        dork_generator = DorkPageGenerator(db, file_processor, clusterer, pages_dir, data_dir=data_dir)
        return db, engine, dork_generator

    def test_db_select_sqlalchemy(self):
        """Objective: Select unique request paths from database.
        Input: Connection to main glastopf database with 500 entries and the pattern 'rfi'.
        Expected Results: 10 data entries in total.
        """
        pages_dir = tempfile.mkdtemp()

        try:
            (db, engine, dork_generator) = self.dork_generator_chain('sql', pages_dir)
            dork_generator.regular_generate_dork(0)
            print "Starting database SELECT test..."
            result = db.select_data("rfi")
            self.assertEqual(len(result), 10)
        finally:
            if os.path.isdir(pages_dir):
                shutil.rmtree(pages_dir)

    def test_automated_extension(self):
        """Objective: Test if the dork database extends on new requests to the honeypot.
        Input: A test request with URL: http://localhost:8080/test.php?c=test
        Expected Results: An entry in the 'inurl' db table containing '/test.php'.
        Notes: The test adds the '/test.php' entry to the database."""
        attack_event = attack.AttackEvent()
        attack_event.matched_pattern = "internal_test"
        attack_event.parsed_request = util.HTTPRequest()
        attack_event.parsed_request.url = "/thiswillNeVeRHaPPend.php?c=test"
        print "Attack event prepared."
        pages_dir = tempfile.mkdtemp()
        try:
            (db, engine, dork_generator) = self.dork_generator_chain('sql', pages_dir)
            dork_generator.regular_generate_dork(0)
            dork_generator.collect_dork(attack_event)
            print "Done collecting the path from the event and writing to the database."
            sql = "SELECT * FROM inurl WHERE content = :x"
            result = engine.connect().execute(sql, x='/thiswillNeVeRHaPPend.php').fetchall()
            print "Done fetching the entries matching the request URL"
            self.assertTrue(len(result) > 0)
            print "Number of entries in the database matching our URL:",
            print len(result),
            print "which equates our expectation."
        finally:
            if os.path.isdir(pages_dir):
                shutil.rmtree(pages_dir)

    def test_result_cluster(self):
        """Objective: Tests if we are able to create a cluster from the sample database..
        Input: Connection to the main database with 500 sample events.
        Expected Results: Requests from the database organized in clusters.
        Notes: String feature extraction is based on '/\w+' or /[a-zA-Z0-9_]"""
        print "Starting database cluster test..."
        pages_dir = tempfile.mkdtemp()
        try:
            (db, engine, dork_generator) = self.dork_generator_chain('sql', pages_dir)
            dork_generator.regular_generate_dork(0)
            print "Done clustering database entries."
            url_list = db.select_data()
            clusterer = cluster.Cluster("/\w+", 1, 1, 1, min_df=0.0)
            clusters = clusterer.cluster(url_list)
            self.assertTrue(len(clusters) > 0)
            print "Number of clusters:",
            print len(clusters),
        finally:
            if os.path.isdir(pages_dir):
                shutil.rmtree(pages_dir)

    def test_dork_page(self):
        """Objective: Tests if the attack surface generation works.
        Input: Data from the dork database.
        Expected Results: HTML pages ready to be served to the adversary.
        Notes: This test covers the generation of the HTML pages from the dork database. The page number is proportional to database entries."""

        print "Starting dork page test."
        pages_dir = tempfile.mkdtemp()
        try:
            (db, engine, dork_generator) = self.dork_generator_chain('sql', pages_dir)
            dork_generator.regular_generate_dork(0)
            print "Done creating dork pages."
            current_pages = dork_generator.get_current_pages()
            self.assertTrue(len(current_pages) > 0)
            print "Number of created HTML pages:",
            print len(current_pages),
            print "equates our expectation."
            print "Sample page can be found in:", pages_dir
        finally:
            if os.path.isdir(pages_dir):
                shutil.rmtree(pages_dir)

    def test_dork_page_content(self):
        """Objective: Testing the attack surfaces content.
        Input: An attack surface sample. The structure is defined in a template.
        Expected Results: The attack surface should be a HTML page containing text and links.
        Notes: We extract and count the elements in the HTML document."""

        pages_dir = tempfile.mkdtemp()

        try:
            dork_generator = self.dork_generator_chain('sql', pages_dir)[2]
            dork_generator.regular_generate_dork(0)

            sample_file = choice(dork_generator.get_current_pages())
            with open(sample_file, 'r') as sample_data:
                data = fromstring(sample_data)
            self.assertTrue(len(data.cssselect('a')) > 0)
            self.assertTrue(len(data.cssselect('title')) > 0)
            self.assertTrue(len(data.cssselect('form')) > 0)
            print "The content analysis of a random HTML page returned:"
            print len(data.cssselect('a')), 'links (<a href=""></a>)',
            print len(data.cssselect('title')), 'page title (<title />)',
            print len(data.cssselect('form')), 'form field (<form />)'
            print "which equates our expectation."
        finally:
            if os.path.isdir(pages_dir):
                shutil.rmtree(pages_dir)

    def test_dork_links(self):
        """Objective: Test if a random link from the dork page exists in the database.
        Input: A random link from a created dork page.
        Expected Results: The path of the link should be at least once in the db.
        Notes: Links have the parameters truncated, so multiple entries are likely."""

        pages_dir = tempfile.mkdtemp()
        try:
            (db, engine, dork_generator) = self.dork_generator_chain('sql', pages_dir)
            dork_generator.regular_generate_dork(0)
            sample_file = choice(dork_generator.get_current_pages())
            print "Randomly selected dork page:", sample_file.rsplit('/', 1)[1]
            with open(sample_file, 'r') as sample_data:
                data = fromstring(sample_data)
            links = data.cssselect('a')
            test_link_path = choice(links).get('href')
            print "Randomly selected path:", test_link_path
            from_livedb = db.select_entry(test_link_path)
            #the test database has below 100 entries, so it will seeded from the dorkdb
            from_dorkdb = db.get_dork_list('inurl', starts_with=test_link_path)
            result_count = len(from_livedb) + len(from_dorkdb)
            print "Done searching for the entry."
            self.assertTrue(result_count > 0)
            print "The dork db returned:",
            print "{0} entries,".format(result_count),
            print "which equates our expectation."
        finally:
            if os.path.isdir(pages_dir):
                shutil.rmtree(pages_dir)

    def test_dork_page_regeneration(self):
        """Objective: Test if the dork pages get regenerated.
        Input: The list of previously generated dork pages.
        Expected Results: A new list of dork pages.
        Notes: A productive system generates new pages in a configurable interval."""
        pages_dir = tempfile.mkdtemp()
        try:
            (db, engine, dork_generator) = self.dork_generator_chain('sql', pages_dir)
            dork_generator.regular_generate_dork(0)
            old_list = dork_generator.get_current_pages()
            print "There are %s previously generated dork pages" % len(old_list),
            old_sample_file = choice(old_list)
            print "For example:", old_sample_file.rsplit('/', 1)[1]
            dork_generator.regular_generate_dork(0)
            print "Done generating new dork pages.",
            print "Old dork pages has been removed."
            new_list = dork_generator.get_current_pages()
            overlap = set(new_list).intersection(old_list)
            self.assertTrue(len(overlap) == 0)
            print "There are", len(overlap), "overlapping dork pages",
            print "which equates our expectation."
        finally:
            if os.path.isdir(pages_dir):
                shutil.rmtree(pages_dir)

        # def test_fetch_dorks(self):
        #     """Objective: Fetch vulnerability information from an external source.
        #     Input: Exploit database dump from http://exploit-db.com. The report contains the vulnerable path.
        #     Expected Results: New vulnerable paths are extracted from the input.
        #     Notes: The data is extracted using a regular expression from 8665 vulnerability reports.
        #     Reports are located in 'modules/handlers/emulators/dork_list/archive/platforms/php/webapps'"""
        #     print "Starting external dork source test."
        #     rexp = remote_exploits.ExploitDB()
        #     rexp.get_dorks()
        #     print "Done fetching and processing dorks."
        #     self.assertTrue(len(rexp.vuln_list) > 0)
        #     self.assertTrue(len(rexp.rfi_list) > 0)
        #     print 'We found:', len(rexp.vuln_list), 'vulnerable paths and',
        #     print len(rexp.rfi_list), 'RFI specific ones',
        #     print "which equates our expectation."
