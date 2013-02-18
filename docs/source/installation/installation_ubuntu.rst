Glastopf Installation
----------------------
| 
| 

Prerequisites Ubuntu
====================
| 

Install the dependencies::	

    sudo apt-get install python2.7 python-openssl python2.7-dev build-essential make python-chardet python-requests python-sqlalchemy python-lxml python-beautifulsoup mongodb python-pip python-dev python-numpy python-setuptools python-numpy-dev python-scipy libatlas-dev g++ git php5 php5-dev
    sudo pip install --upgrade pymongo
| 

Installing ANTLR Python runtime
================================
| 

The ANTLR runtime is needed to analyze SQL injections::

	cd /opt
	sudo wget http://www.antlr3.org/download/antlr-3.1.3.tar.gz
	sudo tar xzf antlr-3.1.3.tar.gz
	cd antlr-3.1.3/runtime/Python
	sudo python2.7 setup.py install

| 

ANTLR mirror 1: http://pkgs.fedoraproject.org/repo/pkgs/antlr3/antlr-3.1.3.tar.gz/e0c25460fa8386548871809a819e587a/antlr-3.1.3.tar.gz

| 

SKLearn
=======
| 

SKLearn takes care of the clustering in Glastopf::

	cd /opt
	sudo git clone git://github.com/scikit-learn/scikit-learn.git
	cd scikit-learn
	sudo python2.7 setup.py install

| 

Install evnet module
====================
| 

Download evnet using git::

	cd /opt
	git clone git://github.com/rep/evnet.git
	cd evnet
	sudo python2.7 setup.py install 

|

Get Glastopf
============
| 

Get the source from the Github repository::

	cd /opt
	sudo git clone git://github.com/glastopf/glastopf.git

| 

Install and configure the PHP sandbox
======================================
| 

Download using git::

	cd /opt
	sudo git clone git://github.com/glastopf/BFR.git
	cd BFR
	phpize
	sudo ./configure --enable-bfr
	sudo make && sudo make install

Open the php.ini file and add the following::

	zend_extension = /usr/lib/php5/20100525+lfs/bfr.so

| 

Go to sandbox directory */opt/glastopf/sandbox/* and create the apd_sandbox.php using command::

	sudo make

| 
 
Configure Glastopf
==================
| 

Setup ip address & port for glastopf on the file *glastopf.cfg*

Run the Honeypot::
	
	cd /opt/glastopf
	sudo screen python2.7 webserver.py

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

