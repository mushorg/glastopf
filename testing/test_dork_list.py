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
from lxml.html.soupparser import fromstring
import os
import shutil
import tempfile
import helpers

from modules.handlers.emulators.dork_list import database
from modules.handlers.emulators.dork_list.dork_page_generator import DorkPageGenerator
from modules.handlers.emulators.dork_list import dork_db
from modules.handlers.emulators.dork_list import remote_exploits
from modules.events import attack
from modules.HTTP import util


class TestEmulatorDorkList(unittest.TestCase):
    """Tests the honeypots vulnerable string selection.
    We first start with the integration test and continue with unit tests.
    The test script will connect to an mongodb instance on localhost, and populate
    with data a needed."""

    @classmethod
    def setUpClass(cls):
        if not os.path.isdir('db'):
            os.mkdir('db')

        cls.db_name = helpers.populate_mongo_testdata()

        cls.fake_config_mongo = tempfile.mkstemp()[1]
        with open(cls.fake_config_mongo, 'w') as f:
            f.writelines(helpers.gen_config(mongodb=cls.db_name))

    @classmethod
    def tearDownClass(cls):
        helpers.delete_mongo_testdata(cls.db_name)

        if os.path.isfile(cls.fake_config_mongo):
            os.remove(cls.fake_config_mongo)

    def test_db_select(self):
        """Objective: Select unique request paths from database.
        Input: Connection to the mongodb database with 500 entries and the pattern 'rfi' from the configuration.
        Expected Results: 10 data entries in total and 10 distinct paths matching the pattern.
        Notes: We can use a pattern to select a subset. Data dump available in testing/data/events.bson"""
        dork_db_file = tempfile.NamedTemporaryFile().name
        try:
            dorkdb = dork_db.DorkDB(dork_db_file)
            db = database.Database(TestEmulatorDorkList.fake_config_mongo)
            pages_dir = tempfile.mkdtemp()
            dork_generator = DorkPageGenerator(dorkdb, db, pages_dir)
            dork_generator.regular_generate_dork(0)
            print "Starting database SELECT test..."
            db.select_data()
            print "Used pattern:", db.pattern
            self.assertTrue(db.num_results == 10)
            self.assertTrue(db.num_distinct_results == 10)
        finally:
            if os.path.isfile(dork_db_file):
                os.remove(dork_db_file)

    def test_automated_extension(self):
        """Objective: Test if the dork database extends on new requests to the honeypot.
        Input: A test request with URL: http://localhost:8080/test.php?c=test
        Expected Results: An entry in the 'inurl' db table containing '/test.php'."""
        attack_event = attack.AttackEvent()
        attack_event.matched_pattern = "internal_test"
        attack_event.parsed_request = util.HTTPRequest()
        attack_event.parsed_request.url = "/test.php?c=test"
        print "Attack event prepared."
        dork_db_file = tempfile.NamedTemporaryFile().name
        try:
            dorkdb = dork_db.DorkDB(dork_db_file)
            db = database.Database(TestEmulatorDorkList.fake_config_mongo)
            dork_generator = DorkPageGenerator(dorkdb, db, None)
            dork_generator.collect_dork(attack_event)
            print "Done collecting the path from the event and writing to the database."
            results = dorkdb.get_dork_list('inurl', '/test.php')
            print "Done fetching the entries matching the request URL"
            self.assertTrue(len(results) > 0)
            print "Number of entries in the database matching our URL:",
            print len(results),
            print "which equates our expectation."
        finally:
            if os.path.isfile(dork_db_file):
                os.remove(dork_db_file)

    def test_dork_persistence(self):
        """Objective: Test if the dork database survives a application restart.
        Input: A test request with URL: http://localhost:8080/jamesbrown.php?c=test
        Expected Results: An entry in the 'inurl' db table containing '/jamesbrown.php'."""
        attack_event = attack.AttackEvent()
        attack_event.matched_pattern = "internal_test"
        attack_event.parsed_request = util.HTTPRequest()
        attack_event.parsed_request.url = "/jamesbrown.php?c=test"
        print "Attack event prepared."
        dork_db_file = tempfile.NamedTemporaryFile().name
        try:
            original_dorkdb = dork_db.DorkDB(dork_db_file)
            db = database.Database(TestEmulatorDorkList.fake_config_mongo)
            dork_generator = DorkPageGenerator(original_dorkdb, db, None)
            dork_generator.collect_dork(attack_event)
            original_dorkdb.save()
            del original_dorkdb
            print "Done collecting the path from the event and writing to the database."
            new_dorkdb = dork_db.DorkDB(dork_db_file)
            results = new_dorkdb.get_dork_list('inurl', '/jamesbrown.php')
            print "Done simulating restart and fetching the entries matching the request URL"
            self.assertTrue(len(results) == 1)
            print "Number of entries in the database matching our URL:",
            print len(results),
            print "which equates our expectation."
        finally:
            if os.path.isfile(dork_db_file):
                os.remove(dork_db_file)

    def test_result_cluster(self):
        """Objective: Tests if the cluster is generated from the result.
        Input: Connection to the mongodb database with 500 sample events.
        Expected Results: Requests from the database organized in clusters.
        Notes: String feature extraction is based on '/\w+' or /[a-zA-Z0-9_]"""
        print "Starting database cluster test..."
        pages_dir = tempfile.mkdtemp()
        dork_db_file = tempfile.NamedTemporaryFile().name
        try:
            dorkdb = dork_db.DorkDB(dork_db_file)
            db = database.Database(TestEmulatorDorkList.fake_config_mongo)
            dork_generator = DorkPageGenerator(dorkdb, db, pages_dir)
            dork_generator.regular_generate_dork(0)
            db.process()
            print "Done clustering database entries."
            self.assertTrue(len(db.clusterer.clusters) > 0)
            print "Number of clusters from the database:",
            print len(db.clusterer.clusters),
        finally:
            if os.path.isdir(pages_dir):
                shutil.rmtree(pages_dir)
            if os.path.isfile(dork_db_file):
                os.remove(dork_db_file)

    def test_dork_page(self):
        """Objective: Tests if the attack surface generation works.
        Input: Data from the dork database.
        Expected Results: HTML pages ready to be served to the adversary.
        Notes: This test covers the generation of the HTML pages from the dork database. The page number is proportional to database entries."""

        print "Starting dork page test."
        pages_dir = tempfile.mkdtemp()
        dork_db_file = tempfile.NamedTemporaryFile().name
        try:
            dorkdb = dork_db.DorkDB(dork_db_file)
            db = database.Database(TestEmulatorDorkList.fake_config_mongo)
            dork_generator = DorkPageGenerator(dorkdb, db, pages_dir)

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
            if os.path.isfile(dork_db_file):
                os.remove(dork_db_file)

    def test_dork_page_content(self):
        """Objective: Testing the attack surfaces content.
        Input: An attack surface sample. The structure is defined in a template.
        Expected Results: The attack surface should be a HTML page containing text and links.
        Notes: We extract and count the elements in the HTML document."""

        pages_dir = tempfile.mkdtemp()
        dork_db_file = tempfile.NamedTemporaryFile().name
        try:
            dorkdb = dork_db.DorkDB(dork_db_file)
            db = database.Database(TestEmulatorDorkList.fake_config_mongo)
            dork_generator = DorkPageGenerator(dorkdb, db, pages_dir)

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
            if os.path.isfile(dork_db_file):
                os.remove(dork_db_file)

    def test_dork_links(self):
        """Objective: Test if a random link from the dork page exists in the database.
        Input: A random link from a created dork page.
        Expected Results: The path of the link should be at least once in the db.
        Notes: Links have the parameters truncated, so multiple entries are likely."""

        pages_dir = tempfile.mkdtemp()
        dork_db_file = tempfile.NamedTemporaryFile().name
        try:
            dorkdb = dork_db.DorkDB(dork_db_file)
            db = database.Database(TestEmulatorDorkList.fake_config_mongo)
            dork_generator = DorkPageGenerator(dorkdb, db, pages_dir)
            dork_generator.regular_generate_dork(0)
            sample_file = choice(dork_generator.get_current_pages())
            print "Randomly selected dork page:", sample_file.rsplit('/', 1)[1]
            with open(sample_file, 'r') as sample_data:
                data = fromstring(sample_data)
            links = data.cssselect('a')
            test_link_path = choice(links).get('href')
            print "Randomly selected path:", test_link_path
            d = database.Database(TestEmulatorDorkList.fake_config_mongo)
            from_livedb = d.select_entry(test_link_path)
            #the test database has below 100 entries, so it will seeded from the dorkdb
            from_dorkdb = dorkdb.get_dork_list('inurl', starts_with=test_link_path)
            result_count = len(from_livedb) + len(from_dorkdb)
            print "Done searching for the entry."
            self.assertTrue(result_count > 0)
            print "The dork db returned:",
            print "{0} entries,".format(result_count),
            print "which equates our expectation."
        finally:
            if os.path.isdir(pages_dir):
                shutil.rmtree(pages_dir)
            if os.path.isfile(dork_db_file):
                os.remove(dork_db_file)

    def test_dork_page_regeneration(self):
        """Objective: Test if the dork pages get regenerated.
        Input: The list of previously generated dork pages.
        Expected Results: A new list of dork pages.
        Notes: A productive system generates new pages in a configurable interval."""
        pages_dir = tempfile.mkdtemp()
        dork_db_file = tempfile.NamedTemporaryFile().name
        try:
            dorkdb = dork_db.DorkDB(dork_db_file)
            db = database.Database(TestEmulatorDorkList.fake_config_mongo)
            dork_generator = DorkPageGenerator(dorkdb, db, pages_dir)
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
            if os.path.isfile(dork_db_file):
                os.remove(dork_db_file)

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
