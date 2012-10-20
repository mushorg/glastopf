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

from random import choice, randint
import unittest
from lxml.html.soupparser import fromstring

from modules.handlers.emulators.dork_list import database
from modules.handlers.emulators.dork_list import gen_dork_list
from modules.handlers.emulators.dork_list import dork_db
from modules.handlers.emulators.dork_list import remote_exploits
from modules.events import attack
from modules.HTTP import util


class TestDorks(unittest.TestCase):
    """Tests the honeypots vulnerable string selection.
    We first start with the integration test and continue with unit tests"""
    def setUp(self):
        self.db = database.DorkDB()

    def tearDown(self):
        del self.db

    def test_db(self):
        """Objective: Tests database connectivity.
        Input: Connection details to the mongodb database.
        Expected Results: Successful connected to the database.
        Notes: We check if we are connected to the right database and collection.""" 
        print "Starting database test..."
        dbtype, database, table = self.db.conn_info()
        if (dbtype == 'mongodb'):
            self.assertEqual(database, 'glastopf')
            self.assertEqual(table, 'events')
        elif dbtype == 'sqlite':
            self.assertEqual(database, 'glastopf.db')
            self.assertEqual(table, 'events')
        else:
            raise Exception('Database type not supported in unittest')
        print "Database type, Database name and Collection(or table) name:",
        print dbtype + ', ' + database + ', ' + table + '.'
        #print self.db.db.name, 'and', self.db.collection.name
        print "equates our expectation."

    def test_db_data(self):
        """Objective: Tests if the database is holding the expected amount of data.
        Input: Connection to the mongodb database filled with 12442 sample events.
        Expected Results: 12442 data entries.
        Notes: Data dump available in honeypot/db/events.bson""" 
        print "Starting database data test..."
        self.db.count_data()
        print "Done counting database entries."
        self.assertTrue(self.db.num_entries > 0)
        print "Number of entries in the database:", self.db.num_entries,
        print "equates our expectation."

    def test_db_select(self):
        """Objective: Select unique request paths from database.
        Input: Connection to the mongodb database with 12442 entries and the pattern 'rfi' from the configuration.
        Expected Results: 459 data entries in total and 360 distinct paths matching the pattern.
        Notes: We can use a pattern to select a subset. Data dump available in honeypot/db/events.bson""" 
        print "Starting database SELECT test..."
        self.db.select_data()
        print "Used pattern:", self.db.pattern
        self.assertTrue(self.db.num_results >= 0)
        self.assertTrue(self.db.num_distinct_results >= 0)
        print "Number of entries with pattern",
        print self.db.pattern, ":", self.db.num_results
        print "Number of distinct entries with pattern",
        print self.db.pattern, ":", self.db.num_distinct_results
        print "equates our expectation."

    def test_automated_extension(self):
        """Objective: Test if the database extends on new requests to the honeypot.
        Input: A test request with URL: http://localhost:8080/test.php?c=test
        Expected Results: An entry in the 'inurl' db table containing '/test.php'. 
        Notes: The test adds the '/test.php' entry to the database."""
        attack_event = attack.AttackEvent()
        attack_event.matched_pattern = "internal_test"
        attack_event.parsed_request = util.HTTPRequest()
        attack_event.parsed_request.url = "/test.php?c=test"
        print "Attack event prepared."
        gen_dork_list.collect_dork(attack_event)
        print "Done collecting the path from the event and writing to the database."
        sql = "SELECT * FROM inurl WHERE content = ?"
        db = dork_db.DorkDB()
        self.cursor = db.conn.cursor()
        cnt = self.cursor.execute(sql,
                (attack_event.parsed_request.url.split('?')[0],)).fetchall()
        self.cursor.close()
        print "Done fetching the entries matching the request URL"
        self.assertTrue(len(cnt) > 0)
        print "Number of entries in the database matching our URL:", 
        print len(cnt),
        print "which equates our expectation."

    def test_result_cluster(self):
        """Objective: Tests if the cluster is generated from the result.
        Input: Connection to the mongodb database with 12442 sample events.
        Expected Results: Requests from the database organized in clusters.
        Notes: String feature extraction is based on '/\w+' or /[a-zA-Z0-9_]"""
        print "Starting database cluster test..."
        self.db.process()
        print "Done clustering database entries."
        self.assertTrue(len(self.db.clusterer.clusters) > 0)
        print "Number of clusters from the database:",
        print len(self.db.clusterer.clusters),
        rand_cluster = randint(0, 5)
        print "Example cluster no.", rand_cluster, "has",
        print len(self.db.clusterer.clusters[rand_cluster]), "element(s)."
        print "Random element from example cluster:"
        print choice(self.db.clusterer.clusters[rand_cluster])
        print "which equates our expectation."

    def test_dork_page(self):
        """Objective: Tests if the attack surface generation works.
        Input: Data from the dork database.
        Expected Results: HTML pages ready to be served to the adversary.
        Notes: This test covers the generation of the HTML pages from the dork database. The page number is proportional to database entries.""" 
        print "Starting dork page test."
        gen_dork_list.regular_generate_dork(0)
        print "Done creating dork pages."
        dirname = 'modules/handlers/emulators/dork_list/pages/'
        self.assertTrue(
                len(gen_dork_list.get_old_dork_pages_list(dirname)) > 0
                )
        print "Number of created HTML pages:",
        print len(gen_dork_list.get_old_dork_pages_list(dirname)),
        print "equates our expectation."
        print "Sample page can be found in:", dirname
        gen_dork_list.remove_old_dork_pages(
                            gen_dork_list.get_old_dork_pages_list(dirname)
                            )

    def test_dork_page_content(self):
        """Objective: Testing the attack surfaces content.
        Input: An attack surface sample. The structure is defined in a template.
        Expected Results: The attack surface should be a HTML page containing text and links.
        Notes: We extract and count the elements in the HTML document."""
        dirname = 'modules/handlers/emulators/dork_list/pages/'
        gen_dork_list.regular_generate_dork(0)
        sample_file = choice(gen_dork_list.get_old_dork_pages_list(dirname))
        with open(sample_file, 'r') as sample_data:
            data = fromstring(sample_data)
            #print tostring(data)
        self.assertTrue(len(data.cssselect('a')) > 0)
        self.assertTrue(len(data.cssselect('title')) > 0)
        self.assertTrue(len(data.cssselect('form')) > 0)
        print "The content analysis of a random HTML page returned:"
        print len(data.cssselect('a')), 'links (<a href=""></a>)',
        print len(data.cssselect('title')), 'page title (<title />)',
        print len(data.cssselect('form')), 'form field (<form />)'
        print "which equates our expectation."

    def test_dork_links(self):
        """Objective: Test if a random link from the dork page exists in the database.
        Input: A random link from a created dork page.
        Expected Results: The path of the link should be at least once in the db.
        Notes: Links have the parameters truncated, so multiple entries are likely."""
        dirname = 'modules/handlers/emulators/dork_list/pages/'
        sample_file = choice(gen_dork_list.get_old_dork_pages_list(dirname))
        print "Randomly selected dork page:", sample_file.rsplit('/', 1)[1]
        with open(sample_file, 'r') as sample_data:
            data = fromstring(sample_data)
        links = data.cssselect('a')
        test_link_path = choice(links).get('href')
        print "Randomly selected path:", test_link_path
        data = self.db.select_entry(test_link_path)
        print "Done searching for the entry."
        self.assertTrue(len(data) > 0)
        print "The dork db returned:",
        print str(len(data)), "entries,",
        print "which equates our expectation."

    def test_dork_page_regeneration(self):
        """Objective: Test if the dork pages get regenerated.
        Input: The list of previously generated dork pages.
        Expected Results: A new list of dork pages.
        Notes: A productive system generates new pages in a configurable interval."""
        dirname = 'modules/handlers/emulators/dork_list/pages/'
        gen_dork_list.regular_generate_dork(0, dirname)
        old_list = gen_dork_list.get_old_dork_pages_list(dirname)
        print "There are %s previously generated dork pages" % len(old_list),
        old_sample_file = choice(old_list)
        print "For example:", old_sample_file.rsplit('/', 1)[1]
        gen_dork_list.regular_generate_dork(0, dirname)
        print "Done generating new dork pages.",
        print "Old dork pages has been removed."
        new_list = gen_dork_list.get_old_dork_pages_list(dirname)
        overlap = set(new_list).intersection(old_list)
        self.assertTrue(len(overlap) == 0)
        print "There are", len(overlap), "overlapping dork pages",
        print "which equates our expectation."

    def test_fetch_dorks(self):
        """Objective: Fetch vulnerability information from an external source.
        Input: Exploit database dump from http://exploit-db.com. The report contains the vulnerable path.
        Expected Results: New vulnerable paths are extracted from the input.
        Notes: The data is extracted using a regular expression from 8665 vulnerability reports. Reports are located in 'modules/handlers/emulators/dork_list/archive/platforms/php/webapps'"""
        print "Starting external dork source test."
        rexp = remote_exploits.ExploitDB()
        rexp.get_dorks()
        print "Done fetching and processing dorks."
        self.assertTrue(len(rexp.vuln_list) > 0)
        self.assertTrue(len(rexp.rfi_list) > 0)
        print 'We found:', len(rexp.vuln_list), 'vulnerable paths and',
        print len(rexp.rfi_list), 'RFI specific ones',
        print "which equates our expectation."
