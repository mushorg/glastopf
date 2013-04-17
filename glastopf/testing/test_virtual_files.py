import unittest
import hashlib
import shutil
import os

from glastopf.glastopf import GlastopfHoneypot

class TestVirtualFiles(unittest.TestCase):

    def test_files(self):
	v_files=('shadow', 'passwd', 'group' )
	f_dir1	= "/tmp/test1/"
	f_dir2	= "/tmp/test2/"
	os.makedirs(f_dir1)
	os.makedirs(f_dir2)

	GlastopfHoneypot.randomize_vdocs(f_dir1)
        GlastopfHoneypot.randomize_vdocs(f_dir2)
	for v_file in v_files:
        	dat_1  = open(os.path.join(f_dir1, "linux/etc/shadow"), 'r').read()
        	dat_2  = open(os.path.join(f_dir2, "linux/etc/passwd"), 'r').read()
		md5_1  = hashlib.md5(dat_1).hexdigest()
		md5_2  = hashlib.md5(dat_2).hexdigest()
		self.assertNotEqual(md5_1,md5_2)
	shutil.rmtree(f_dir1)
	shutil.rmtree(f_dir2)

