================
Guidelines
================

Developers Guide
================

Indentation
----------------
* We are using 4 tab-spaces
* No one line conditionals

Style
----------------
* We obey to the `PEP8 <http://www.python.org/dev/peps/pep-0008/>`_

Copyright
----------------
* If you are adding a file/code which is produced only by you, feel free to add the license information and a notice who holds the copyrights.

Environment
----------------
* `Eclipse <http://eclipse.org/>`_ with `PyDev <http://pydev.org/>`_ and `Subclipse <http://subclipse.tigris.org/>`_ is a good combination.

Glastopf-runner for developers
------------------------------
It is recommended to use the *develop* functionality of distutils while hacking on glastopf.
When using *develop* a egg link pointing to your repository directory will be places in site-packages - 
which saves you from doing **python setup.py install** over and over again. Example::

  $ python setup.py develop

Checking if the egg was created as planned::

  $ cat /Users/jkv/virtualenv/glastopf/lib/python2.7/site-packages/Glastopf.egg-link
    /Users/jkv/repos/glastopf
    ^ output from cat

After this, we can create a tmp workdir and start testing directly from the repo::

  $ pwd
  /Users/jkv/repos/glastopf
  $ mkdir tmp
  $ cd tmp/
  $ python ../bin/glastopf-runner 
  2013-04-17 11:29:11,335 (glastopf.glastopf) Initializing Glastopf using "/Users/jkv/repos/glastopf/tmp" as work directory.
  2013-04-17 11:29:11,337 (glastopf.glastopf) Connecting to main database with: sqlite:///db/glastopf.db


