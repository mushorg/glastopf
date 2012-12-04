==================
Installation
==================

Glastopf Installation
==================

Prerequisites 
------------------

Install the basic packages::

    sudo apt-get install git subversion python2.7 python-openssl python2.7-dev build-essential make python-chardet

Installing ANTLR Python runtime
------------------

The ANTLR runtime is needed to analyze SQL injections::

	cd /opt
	sudo wget http://www.antlr.org/download/antlr-3.1.3.tar.gz
	sudo tar xzf antlr-3.1.3.tar.gz
	cd antlr-3.1.3/runtime/Python
	sudo python2.7 setup.py install

ANTLR mirror 1: http://pkgs.fedoraproject.org/repo/pkgs/antlr3/antlr-3.1.3.tar.gz/e0c25460fa8386548871809a819e587a/antlr-3.1.3.tar.gz

SKLearn
------------------

SKLearn takes care of the clustering in Glastopf::

	sudo apt-get install python-dev python-numpy python-setuptools python-numpy-dev python-scipy libatlas-dev g++ git
	cd /opt
	sudo git clone git://github.com/scikit-learn/scikit-learn.git
	cd scikit-learn
	sudo python2.7 setup.py install

Note: Warning messages about not finding certain files can be ignored.

Mongo DB
------------------

Get the MongoDB package::

	sudo apt-get install mongodb python-pymongo

Import sample db which can be found here: http://dev.glastopf.org/projects/glaspot/files::

	cd db/
	sudo mongorestore -d glastopf -c events events.bson

SQLAlchemy
------------------

Install the SQLAlchemy package::

	sudo apt-get install sqlalchemy

HTML parsing
------------------

Get the required packages::

	sudo apt-get install python-lxml python-beautifulsoup

Install evnet module
------------------

Download evnet using git::

	git clone git://github.com/rep/evnet.git

Install it with command::

	sudo python2.7 setup.py install 

Get Glastopf
------------------

Get the source from the Subversion repository::

	sudo svn co svn://glastopf.org:9090/glaspot glaspot

Install and configure the PHP sandbox
------------------

Follow the instructions to install BFR: https://github.com/glastopf/BFR

Go to sandbox directory @opt/glaspot/trunk/sandbox@ and create the apd_sandbox.php using command::

	sudo make
 
Configure Glastopf
------------------

Setup ip address & port for glastopf on the file @glastopf.cfg@

Run the Honeypot::

	sudo python2.7 webserver.py

Testing the Honeypot
------------------

Use your web browser to visit your honeypot. You should see the following output on your command line::

	Webserver running on: 0.0.0.0:80 waiting for connections...
	2011-11-20 23:23:34 yyy.yyy.yyy.yyy requested GET / on  xxx.xxx.xxx.xxx
	2011-11-20 23:23:34 yyy.yyy.yyy.yyy requested GET /style.css on xxx.xxx.xxx.xxx
	2011-11-20 23:23:34 yyy.yyy.yyy.yyy requested GET /favicon.ico on  xxx.xxx.xxx.xxx
