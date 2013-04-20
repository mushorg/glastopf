import random #for randint()
import unittest
import hashlib
import uuid
import shutil
import os
import tempfile
import inspect
import helpers
from glastopf.glastopf import GlastopfHoneypot

class TestVirtualDocs(unittest.TestCase):

    def test_virtualdocs(self):
        """Objective: Test for the creation of random files in the virtual directories
Input: Return value from GlastopfHoneypot.randomize_vdocs()
Expected Result: Two runs of GlastopfHoneypot.randomize_vdocs() have different results
Notes:"""
        v_files = ("shadow", "passwd", "group")
        f_dir1 = tempfile.mkdtemp()
        f_dir2 = tempfile.mkdtemp()
        os.makedirs(os.path.join(f_dir1, "linux/etc"))
        os.makedirs(os.path.join(f_dir2, "linux/etc"))
        GlastopfHoneypot.randomize_vdocs(f_dir1)
        GlastopfHoneypot.randomize_vdocs(f_dir2)
        for v_file in v_files:
            file_1 = open(os.path.join(f_dir1, "linux/etc/", v_file), "r")
            file_2 = open(os.path.join(f_dir2, "linux/etc/", v_file), "r")
            md5_1 = hashlib.md5(file_1.read()).hexdigest()
            md5_2 = hashlib.md5(file_2.read()).hexdigest()
            file_1.close()
            file_2.close()
            self.assertNotEqual(md5_1, md5_2)
        shutil.rmtree(f_dir1)
        shutil.rmtree(f_dir2)

    def test_get_entry(self):
  """Objective: Test for the creation of random usernames
Input: Return value from GlastopfHoneypot._get_entry()
Expected Result: Two runs of GlastopfHoneypot._get_entry() have different results
Notes:"""
        rnd_id1 = random.randint(1,100)
        rnd_id2 = random.randint(1,100) #generating random user_id        
        ret1 = GlastopfHoneypot._get_entry(rnd_id1)
        ret2 = GlastopfHoneypot._get_entry(rnd_id2)
        dat1 = ret1[0].split(":")[0].strip()
        dat2 = ret2[0].split(":")[0].strip()# get the username
        md5_1 = hashlib.md5(dat1).hexdigest()
        md5_2 = hashlib.md5(dat2).hexdigest()
        self.assertNotEqual(md5_1, md5_2)
