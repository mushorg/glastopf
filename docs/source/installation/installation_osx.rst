Glastopf Installation - OS X (Mountain Lion)
--------------------------------------------
| 
| 

Prerequisites 
=============
| 

Xcode, gfortran, autoconf and gevent are required when installing Glastopf on OS X.

* Xcode can be installed from App Store. Command Line Tools must be installed after Xcode has been installed.
* Gfortran can be install using homebrew.

Install gfortran, autoconf and gevent using homebrew::

    brew install gfortran 
    brew install autoconf
    brew install gevent

Then we need to install pip::

    sudo easy_install pip
 

Install and configure the PHP sandbox
=====================================
| 

Download using git::

    sudo mkdir /opt
    cd /opt
    sudo git clone git://github.com/mushorg/BFR.git
    cd BFR
    sudo phpize
    sudo ./configure --enable-bfr
    sudo make && sudo make install


Open the php.ini file and add bfr.so accordingly to the build output::

    zend_extension = /usr/lib/php/extensions/no-debug-non-zts-20090626/bfr.so


Installing and setting up a virtual environment
===============================================
| 

Prepare virtual environment::

    sudo pip install virtualenv
    sudo virtualenv glastopf-virt --system-site-packages
    source glastopf-virt/bin/activate

Install Glastopf using pip::

    sudo pip install glastopf
 

Starting the honeypot
=========================
| 

Note: Before using the follow command make sure you are operating within the virtual environment.

Prepare glastopf environment::

	cd /opt
	sudo mkdir myhoneypot
	cd myhoneypot
	sudo glastopf-runner

If you receive errors regarding syslog when starting glastopf, please update the syslog path in glastopf.cfg::

   [syslog]
   enabled = False
   socket = /var/run/syslog


Testing the Honeypot
====================
|

Start Glastopf (from your 'myhoneypot' directory)::

    sudo glastopf-runner

Use your web browser to visit your honeypot. You should see the following output on your command line::

	2013-03-14 09:17:59,004 (glastopf.glastopf) Initializing Glastopf using "/opt/myhoneypot" as work directory.
	2013-03-14 09:17:59,014 (glastopf.glastopf) Connecting to main database with: sqlite:///db/glastopf.db
	2013-03-14 09:17:59,113 (glastopf.modules.handlers.emulators.dork_list.dork_page_generator) Bootstrapping dork database.
	2013-03-14 09:17:59,133 (requests.packages.urllib3.connectionpool) Starting new HTTPS connection (1): mnemosyne.honeycloud.net
	2013-03-14 09:18:00,154 (requests.packages.urllib3.connectionpool) "POST /login HTTP/1.1" 200 30
	2013-03-14 09:18:00,589 (requests.packages.urllib3.connectionpool) "GET /api/v1/aux/dorks?limit=1000 HTTP/1.1" 200 180459
	2013-03-14 09:18:00,711 (glastopf.modules.handlers.emulators.dork_list.mnem_service) Successfully retrieved 1000 dorks from the mnemosyne service.
	2013-03-14 09:18:02,752 (glastopf.glastopf) Generating initial dork pages - this can take a while.
	2013-03-14 09:18:05,223 (glastopf.modules.reporting.auxiliary.log_hpfeeds) Connecting to feed broker.
	2013-03-14 09:18:05,280 (glastopf.modules.reporting.auxiliary.log_hpfeeds) Connected to hpfeed broker.
	2013-03-14 09:18:08,408 (glastopf.glastopf) Glastopf started and privileges dropped.
	2013-03-14 09:18:49,185 (glastopf.glastopf) 172.16.177.131 requested GET / on 172.16.177.131
	2013-03-14 09:18:49,250 (glastopf.glastopf) 172.16.177.131 requested GET /style.css on 172.16.177.131
	2013-03-14 09:18:49,381 (glastopf.glastopf) 172.16.177.131 requested GET /favicon.ico on 172.16.177.131

