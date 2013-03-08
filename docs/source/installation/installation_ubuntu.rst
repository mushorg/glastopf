Glastopf Installation
----------------------
| 
| 

Prerequisites Ubuntu
====================
| 

Install the dependencies::	

    sudo apt-get update
    sudo apt-get install python2.7 python-openssl python-gevent libevent-dev python2.7-dev build-essential make python-chardet python-requests python-sqlalchemy python-lxml python-beautifulsoup mongodb python-pip python-dev python-numpy python-setuptools python-numpy-dev python-scipy libatlas-dev g++ git php5 php5-dev
    sudo pip install --upgrade distribute
| 

Install and configure the PHP sandbox
=====================================
| 
Download using git::

    cd /opt
    sudo git clone git://github.com/glastopf/BFR.git
    cd BFR
    sudo phpize
    sudo ./configure --enable-bfr
    sudo make && sudo make install


Open the php.ini file and add the following::

    zend_extension = /usr/lib/php5/20100525+lfs/bfr.so

|

Install glastopf
==================
| 

Install from git::

    git clone https://github.com/glastopf/glastopf.git
    cd glastopf
    python setup.py install

Or install latest version from pypi::

	pip install glastopf

| 

Configuration
=========================
| 

Prepare glastopf environment::

	cd 
	mkdir myhoneypot
	cd myhoneypot
	glastopf-runner

A new default glastopf.cfg has been created in _myhoneypot_, which can be customized as required.

| 


Testing the Honeypot
====================
|

Start Glastopf (from your 'myhoneypot' directory)::

    glastopf-runner

Use your web browser to visit your honeypot. You should see the following output on your command line::

    2013-02-28 22:06:58,149 (root) Webserver running on: 0.0.0.0:8080 waiting for connections.
    2013-02-28 22:06:58,149 (glastopf.glastopf) Initializing Glastopf using "/home/jkv/glastopf/glastopf/123" as work directory.
    2013-02-28 22:06:58,151 (glastopf.glastopf) Connecting to main database with: sqlite:///db/glastopf.db
    2013-02-28 22:06:59,709 (glastopf.modules.handlers.emulators.dork_list.dork_page_generator) Bootstrapping dork database.
    2013-02-28 22:06:59,723 (requests.packages.urllib3.connectionpool) Starting new HTTPS connection (1): mnemosyne.honeycloud.net
    2013-02-28 22:06:59,857 (requests.packages.urllib3.connectionpool) "POST /login HTTP/1.1" 200 30
    2013-02-28 22:06:59,986 (requests.packages.urllib3.connectionpool) "GET /api/v1/aux/dorks?limit=1000 HTTP/1.1" 200 174914
    2013-02-28 22:07:00,037 (glastopf.modules.handlers.emulators.dork_list.mnem_service) Successfully retrieved 1000 dorks from the mnemosyne service.
    2013-02-28 22:07:02,027 (glastopf.glastopf) Generating initial dork pages - this can take a while.
    2013-02-28 22:07:03,829 (glastopf.modules.reporting.auxiliary.log_hpfeeds) Connecting to feed broker.
    2013-02-28 22:07:03,853 (glastopf.modules.reporting.auxiliary.log_hpfeeds) Connected to hpfeed broker.
    2013-02-28 22:07:06,880 (glastopf.glastopf) Glastopf started and privileges dropped.
    2013-02-28 22:07:12,058 (glastopf.glastopf) 192.168.1.123 requested GET / on 192.168.1.145:8080
    2013-02-28 22:07:12,087 (glastopf.glastopf) 192.168.1.123 requested GET /style.css on 192.168.1.145:8080
    2013-02-28 22:07:12,160 (glastopf.glastopf) 192.168.1.123 requested GET /favicon.ico on 192.168.1.145:8080

