==================
Releasing Glastopf
==================

Before releasing
================

Remove -dev from version numbers in the following files::

* setup.py
* glastopf/__init__.py

Add and push a git tag:

  git tag -a $VERSION_NUMBER$
  git push --tag



Releasing
=========

Build package:

  python setup.py sdist

Finally upload the package to PYPI.


After releasing
===============

Append -dev to version numbers in the following files::

* setup.py
* glastopf/__init__.py


Notes
=====

If you fucked up a tag, you can fix it using the following procedure:

Renaming:

  git tag new_tag old_tag

Delete the old tag:

  git tag -d old_tag

Delete the old tag on remote:

  git push origin :refs/tags/old_tag
