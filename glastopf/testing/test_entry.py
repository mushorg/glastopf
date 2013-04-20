import random 
import unittest
import hashlib
import shutil
import os
import tempfile
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
        """Objective: Test if the entries generated by the '_get_entry()'different.
Input: Return value from GlastopfHoneypot._get_entry()
Expected Result: Two runs of GlastopfHoneypot._get_entry() generate different results
Notes:"""
        user_id1 = random.randint(1000, 1500) # Realistic user ID
        pwd_entry1, shd_entry1, grp_entry1 = GlastopfHoneypot._get_entry(user_id1)
        user_id2 = random.randint(1000, 1500)
        pwd_entry2, shd_entry2, grp_entry2 = GlastopfHoneypot._get_entry(user_id2)
        self.assertNotEqual(pwd_entry1, pwd_entry2)
        self.assertNotEqual(shd_entry1, shd_entry2)
        self.assertNotEqual(grp_entry1, grp_entry2)
