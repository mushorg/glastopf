Glastopf Installation
----------------------
| 
| 

Prerequisites OpenBSD
=====================
| 

Install the dependencies::

	pkg_add -r python-2.7.3 py-pip py-gevent mysql-client py-openssl py-chardet py-sqlalchemy py-lxml py-beautifulsoup py-setuptools py-jinja2 py-scipy php pear autoconf automake g77 gfortran plplot-f77 libgfortran libevent libelf plplot git lapack gettext

| 

Create symbolic links::

	ln -sf /usr/local/bin/php-config-5.3 /usr/local/bin/php-config
	ln -sf /usr/local/bin/phpize-5.3 /usr/local/bin/phpize
	ln -sf /usr/local/bin/python2.7 /usr/local/bin/python 
	ln -sf /usr/local/bin/python2.7-2to3 /usr/local/bin/2to3
	ln -sf /usr/local/bin/python2.7-config /usr/local/bin/python-config
	ln -sf /usr/local/bin/pydoc2.7  /usr/local/bin/pydoc
	ln -sf /usr/local/bin/pip-2.7 /usr/local/bin/pip

| 

Set autoconf and automake versions::

	export AUTOCONF_VERSION=2.59
	export AUTOMAKE_VERSION=1.9 


| 

Install BFR
===========
| 

Download using git::

	cd /opt
	git clone git://github.com/mushorg/BFR.git
	cd BFR
	phpize
	./configure --enable-bfr
	make && make install

Copy the search path to bfr.so and add it to */etc/php-5.3.ini*. It can look like this::

	zend_extension = /usr/local/lib/php-5.3/modules/bfr.so

| 

Install Glastopf
================
| 

Install latest stable release from pip::

	pip install glastopf

Or install latest development version from the repository::

    cd /opt
    git clone https://github.com/mushorg/glastopf.git
    cd glastopf
    python setup.py install

|

Configuration
=============
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

Use your web browser to visit your honeypot. You should see the following output on your command line::

	2013-03-15 12:56:42,075 (glastopf.glastopf) Initializing Glastopf using "/opt/myhoneypot" as work directory.
	2013-03-15 12:56:42,077 (glastopf.glastopf) Connecting to main database with: sqlite:///db/glastopf.db
	2013-03-15 12:56:42,146 (glastopf.modules.handlers.emulators.dork_list.dork_page_generator) Bootstrapping dork database.
	2013-03-15 12:56:42,159 (requests.packages.urllib3.connectionpool) Starting new HTTPS connection (1): mnemosyne.honeycloud.net
	2013-03-15 12:56:42,622 (requests.packages.urllib3.connectionpool) "POST /login HTTP/1.1" 200 30
	2013-03-15 12:56:42,753 (requests.packages.urllib3.connectionpool) "GET /api/v1/aux/dorks?limit=1000 HTTP/1.1" 200 45235
	2013-03-15 12:56:42,831 (glastopf.modules.handlers.emulators.dork_list.mnem_service) Successfully retrieved 258 dorks from the mnemosyne service.
	2013-03-15 12:56:44,406 (glastopf.glastopf) Generating initial dork pages - this can take a while.
	2013-03-15 12:56:46,382 (glastopf.modules.reporting.auxiliary.log_hpfeeds) Connecting to feed broker.
	2013-03-15 12:56:46,871 (glastopf.modules.reporting.auxiliary.log_hpfeeds) Connected to hpfeed broker.
	2013-03-15 12:56:52,856 (glastopf.glastopf) Glastopf started and privileges dropped.
	2013-03-15 12:57:04,073 (glastopf.glastopf) 192.168.10.85 requested GET / on 192.168.10.97
	2013-03-15 12:57:04,149 (glastopf.glastopf) 192.168.10.85 requested GET /style.css on 192.168.10.97
	2013-03-15 12:57:05,766 (glastopf.glastopf) 192.168.10.85 requested GET / on 192.168.10.97
	2013-03-15 12:57:05,825 (glastopf.glastopf) 192.168.10.85 requested GET /style.css on 192.168.10.97
	2013-03-15 12:57:06,611 (glastopf.glastopf) 192.168.10.85 requested GET / on 192.168.10.97

