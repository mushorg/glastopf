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

	Webserver running on: 0.0.0.0:80 waiting for connections...
	2011-11-20 23:23:34 yyy.yyy.yyy.yyy requested GET / on  xxx.xxx.xxx.xxx
	2011-11-20 23:23:34 yyy.yyy.yyy.yyy requested GET /style.css on xxx.xxx.xxx.xxx
	2011-11-20 23:23:34 yyy.yyy.yyy.yyy requested GET /favicon.ico on  xxx.xxx.xxx.xxx
	2011-11-20 23:23:34 yyy.yyy.yyy.yyy requested GET /style.css on xxx.xxx.xxx.xxx
	2011-11-20 23:23:34 yyy.yyy.yyy.yyy requested GET /favicon.ico on  xxx.xxx.xxx.xxx



