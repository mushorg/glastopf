Glastopf Installation - Debian Squeeze
---------------------------------------
| 
| 

Prerequisites
=============
|

Add the Backports repository to your sources.list::

    deb http://backports.debian.org/debian-backports squeeze-backports main

Or (for Wheezy)::

    deb http://ftp.debian.org/debian/ wheezy-backports main

|
Install the dependencies::	

    apt-get update
    apt-get install python python-openssl python-gevent libevent-dev python-dev build-essential make
    apt-get install python-argparse python-chardet python-requests python-sqlalchemy python-lxml 
    apt-get install python-beautifulsoup mongodb python-pip python-dev python-setuptools
    apt-get install g++ git php5 php5-dev liblapack-dev gfortran
    apt-get install libxml2-dev libxslt-dev
    apt-get install libmysqlclient-dev
    pip install --upgrade distribute
| 

Install and configure the PHP sandbox
=====================================
| 
Download using git::

    cd /opt
    git clone git://github.com/mushorg/BFR.git
    cd BFR
    phpize
    ./configure --enable-bfr
    make &&  make install


Copy the search path to bfr.so and add it to php.ini. It can look like this::

    zend_extension =   /usr/lib/php5/20131226/bfr.so

|

Install glastopf
==================
| 
Install latest stable release from pip::

    pip install glastopf

Or install latest development version from the repository::

    cd /opt
    git clone https://github.com/mushorg/glastopf.git
    git clone https://github.com/client9/libinjection.git
    git clone https://github.com/mushorg/pylibinjection.git
    cd glastopf
    python setup.py install
| 

Configuration
=========================
| 

Prepare glastopf environment::

	cd /opt
	mkdir myhoneypot
	cd myhoneypot
	glastopf-runner

A new default glastopf.cfg has been created in *myhoneypot*, which can be customized as required.

| 


Testing the Honeypot
====================
|

Start Glastopf (from your 'myhoneypot' directory)::

    glastopf-runner

Use your web browser to visit your honeypot. You should see the following output on your command line::

	2013-03-13 21:10:33,047 (glastopf.glastopf) Initializing Glastopf using "/opt/myhoneypot" as work directory.
	2013-03-13 21:10:33,048 (glastopf.glastopf) Connecting to main database with: sqlite:///db/glastopf.db
	2013-03-13 21:10:33,073 (glastopf.modules.reporting.auxiliary.log_hpfeeds) Connecting to feed broker.
	2013-03-13 21:10:33,237 (glastopf.modules.reporting.auxiliary.log_hpfeeds) Connected to hpfeed broker.
	2013-03-13 21:10:36,290 (glastopf.glastopf) Glastopf started and privileges dropped.
	2013-03-13 21:10:56,282 (glastopf.glastopf) 192.168.1.148 requested GET / on 192.168.1.109
	2013-03-13 21:10:56,401 (glastopf.glastopf) 192.168.1.148 requested GET /style.css on 192.168.1.109
	2013-03-13 21:10:56,463 (glastopf.glastopf) 192.168.1.148 requested GET /favicon.ico on 192.168.1.109

