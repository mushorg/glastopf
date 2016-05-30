Glastopf Installation - Ubuntu 12.04 LTS
-----------------------------------------
| 
| 

Prerequisites
=============
|
Install the dependencies::	

    sudo apt-get update
    sudo apt-get install python2.7 python-openssl python-gevent libevent-dev python2.7-dev build-essential make
    sudo apt-get install python-chardet python-requests python-sqlalchemy python-lxml
    sudo apt-get install python-beautifulsoup mongodb python-pip python-dev python-setuptools
    sudo apt-get install g++ git php5 php5-dev liblapack-dev gfortran libmysqlclient-dev
    sudo apt-get install libxml2-dev libxslt-dev
    sudo pip install --upgrade distribute
| 

Install and configure the PHP sandbox
=====================================
| 
Download using git::

    cd /opt
    sudo git clone git://github.com/mushorg/BFR.git
    cd BFR
    sudo phpize
    sudo ./configure --enable-bfr
    sudo make && sudo make install


Open the php.ini file and add bfr.so accordingly to the build output

default locations of php.ini: 

/etc/php5/apache2/php.ini (Ubuntu 14.04 LTS with apache)

/etc/php/5.6/cli/php.ini (Ubuntu 16.04 LTS)

    zend_extension = /usr/lib/php5/20090626+lfs/bfr.so

|

Install glastopf
==================
| 
Install latest stable release from pip::

	sudo pip install glastopf

Or install latest development version from the repository::

    cd /opt
    sudo git clone https://github.com/mushorg/glastopf.git
    cd glastopf
    sudo python setup.py install
| 

Configuration
=========================
| 

Prepare glastopf environment::

	cd /opt
	sudo mkdir myhoneypot
	cd myhoneypot
	sudo glastopf-runner

A new default glastopf.cfg has been created in *myhoneypot*, which can be customized as required.

| 


Testing the Honeypot
====================
|

Start Glastopf (from your 'myhoneypot' directory)::

    sudo glastopf-runner

Use your web browser to visit your honeypot. You should see the following output on your command line::

	2013-03-14 08:34:08,129 (glastopf.glastopf) Initializing Glastopf using "/opt/myhoneypot" as work directory.
	2013-03-14 08:34:08,130 (glastopf.glastopf) Connecting to main database with: sqlite:///db/glastopf.db
	2013-03-14 08:34:08,152 (glastopf.modules.reporting.auxiliary.log_hpfeeds) Connecting to feed broker.
	2013-03-14 08:34:08,227 (glastopf.modules.reporting.auxiliary.log_hpfeeds) Connected to hpfeed broker.
	2013-03-14 08:34:11,265 (glastopf.glastopf) Glastopf started and privileges dropped.
	2013-03-14 08:34:32,853 (glastopf.glastopf) 192.168.10.85 requested GET / on 192.168.10.102
	2013-03-14 08:34:32,960 (glastopf.glastopf) 192.168.10.85 requested GET /style.css on 192.168.10.102
	2013-03-14 08:34:33,021 (glastopf.glastopf) 192.168.10.85 requested GET /favicon.ico on 192.168.10.102

