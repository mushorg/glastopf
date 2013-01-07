Glastopf Installation
----------------------
| 
| 

Prerequisites Ubuntu
====================
| 

Install the dependencies::	

    sudo apt-get install python2.7 python-openssl python2.7-dev build-essential make python-chardet python-sqlalchemy python-lxml python-beautifulsoup mongodb python-pymongo python-dev python-numpy python-setuptools python-numpy-dev python-scipy libatlas-dev g++ git php5 php5-dev

| 

Installing ANTLR Python runtime
================================
| 

The ANTLR runtime is needed to analyze SQL injections::

	cd /opt
	sudo wget http://www.antlr.org/download/antlr-3.1.3.tar.gz
	sudo tar xzf antlr-3.1.3.tar.gz
	cd antlr-3.1.3/runtime/Python
	sudo wget http://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11-py2.7.egg
	sudo mv setuptools-0.6c11-py2.7.egg setuptools-0.6c5-py2.7.egg
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

	Webserver running on: 0.0.0.0:80 waiting for connections...
	2011-11-20 23:23:34 yyy.yyy.yyy.yyy requested GET / on  xxx.xxx.xxx.xxx
	2011-11-20 23:23:34 yyy.yyy.yyy.yyy requested GET /style.css on xxx.xxx.xxx.xxx
	2011-11-20 23:23:34 yyy.yyy.yyy.yyy requested GET /favicon.ico on  xxx.xxx.xxx.xxx
	2011-11-20 23:23:34 yyy.yyy.yyy.yyy requested GET /style.css on xxx.xxx.xxx.xxx
	2011-11-20 23:23:34 yyy.yyy.yyy.yyy requested GET /favicon.ico on  xxx.xxx.xxx.xxx
