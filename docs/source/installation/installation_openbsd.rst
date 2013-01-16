Glastopf Installation
----------------------
| 
| 

Prerequisites OpenBSD
=====================
| 

Install the dependencies::

	pkg_add -r python2.7 py-openssl autoconf automake py-chardet py-sqlalchemy py-lxml py-beautifulsoup mongodb py-numpy py-setuptools python-numpy-dev py-scipy atlas git php 

| 

Create symbolic links::

	ln -s /usr/local/bin/php-config-5.3 /usr/local/bin/php-config
	ln -s /usr/local/bin/phpize-5.3 /usr/local/bin/phpize

| 

Installing ANTLR Python runtime
================================
| 

The ANTLR runtime is needed to analyze SQL injections::

	cd /opt
	wget http://www.antlr.org/download/antlr-3.1.3.tar.gz
	tar xzf antlr-3.1.3.tar.gz
	cd antlr-3.1.3/runtime/Python
	wget http://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11-py2.7.egg
	mv setuptools-0.6c11-py2.7.egg setuptools-0.6c5-py2.7.egg
	python2.7 setup.py install


| 

SKLearn
=======
| 

SKLearn takes care of the clustering in Glastopf::

	cd /opt
	git clone git://github.com/scikit-learn/scikit-learn.git
	cd scikit-learn
	python2.7 setup.py install

| 

Install evnet module
====================
| 

Download and install evnet::

	cd /opt
	git clone git://github.com/rep/evnet.git
	cd evnet
	python2.7 setup.py install 

| 

Mongo DB
========
|

Download event.bson from http://glastopf.org/events.bson and sample database from http://glastopf.org/glastopf.db.bz2.

Install the database::

	mongorestore -d glastopf -c events events.bson

|

Get Glastopf
============
| 

Get the source from the Github repository::

	cd /opt
	git clone git://github.com/glastopf/glastopf.git

| 

Install and configure the PHP sandbox
======================================
| 

Download using git::

	cd /opt
	git clone git://github.com/glastopf/BFR.git
	cd BFR
	phpize
	./configure --enable-bfr
	make && make install
	Add the following to */etc/php-5.3.ini*
	zend_extension = /usr/local/lib/php-5.3/modules/bfr.so


| 

Go to sandbox directory */opt/glastopf/sandbox/* and create the apd_sandbox.php using command::

	 make

| 
 
Configure Glastopf
==================
| 

Setup ip address & port for glastopf on the file *glastopf.cfg*

Run the Honeypot::
	
	cd /opt/glastopf
	screen python2.7 webserver.py

| 

Testing the Honeypot
====================
| 

Use your web browser to visit your honeypot. You should see the following output on your command line::

	2013-01-12 14:06:48,215 (root) Webserver running on: 0.0.0.0:8080 waiting for connections.
	2013-01-12 14:06:48,651 (glastopf) Starting Glastopf
	2013-01-12 14:06:48,653 (glastopf) Starting Glastopf
	2013-01-12 14:06:48,667 (modules.reporting.hp_feed) Connecting to feed broker.
	2013-01-12 14:06:48,731 (modules.reporting.hp_feed) Connected to hpfeed broker.
	2013-01-12 14:06:51,758 (glastopf) HPFeeds started
	2013-01-12 14:06:51,760 (glastopf) Generating initial dork pages - this can take a while.
	2013-01-12 14:07:30,781 (glastopf) Glastopf instantiated and privileges dropped
	2013-01-12 14:12:03,447 (glastopf) 192.168.1.142 requested GET / on 192.168.1.112:8080
	2013-01-12 14:12:03,652 (glastopf) 192.168.1.142 requested GET /style.css on 192.168.1.112:8080
	2013-01-12 14:12:03,853 (glastopf) 192.168.1.142 requested GET /favicon.ico on 192.168.1.112:8080

