Glastopf Installation
----------------------
| 
| 

Prerequisites OS X (Mountain Lion)
==================================
| 

Xcode, gfortran and autoconf are required when installing Glastopf on OS X.

* Xcode can be installed from App Store. 
* Gfortran can be install using homebrew.

Installing gfortran and autoconf using homebrew::

	brew install gfortran 
        brew install autoconf

| 

Install and configure the PHP sandbox
=====================================
| 
Download using git::

    cd /opt
    sudo git clone git://github.com/glastopf/BFR.git
    cd BFR
    phpize
    sudo ./configure --enable-bfr
    sudo make && sudo make install


Open the php.ini file and add bfr.so accordingly to the build output::

    zend_extension = /usr/lib/php/extensions/no-debug-non-zts-20090626/bfr.so

|

Installing and setting up a virtual environment
===============================================
| 

Prepare virtual environment::

    virtualenv glastopf-virt --system-site-packages
    source glastopf-virt/glastopf/bin/activate

Install Glastopf using pip::

    pip install glastopf

| 

Starting the honeypot
=========================
| 

Note: Before using the follow command make sure you are operating within the virtual environment.

Prepare glastopf environment::

	cd 
	mkdir myhoneypot
	cd myhoneypot
	glastopf-runner.py

If you receive errors regarding syslog when starting glastopf, please update the syslog path in glastopf.cfg::

   [syslog]
   enabled = False
   socket = /var/run/syslog

Testing the Honeypot
====================
|

Start Glastopf (from your 'myhoneypot' directory)::

    glastopf-runner.py

Use your web browser to visit your honeypot. You should see the following output on your command line::

    2013-03-04 09:34:48,335 (glastopf.glastopf) Initializing Glastopf using "/Users/jkv/123" as work directory. 
    2013-03-04 09:34:48,337 (glastopf.glastopf) Connecting to main database with: sqlite:///db/glastopf.db
    2013-03-04 09:34:48,394 (glastopf.modules.handlers.emulators.dork_list.dork_page_generator) Bootstrapping dork database.
    2013-03-04 09:34:48,426 (requests.packages.urllib3.connectionpool) Starting new HTTPS connection (1): mnemosyne.honeycloud.net
    2013-03-04 09:40:54,885 (glastopf.glastopf) Initializing Glastopf using "/Users/jkv/123" as work directory.
    2013-03-04 09:40:54,886 (glastopf.glastopf) Connecting to main database with: sqlite:///db/glastopf.db
    2013-03-04 09:40:54,933 (glastopf.modules.reporting.auxiliary.log_hpfeeds) Connecting to feed broker.
    2013-03-04 09:40:54,962 (glastopf.modules.reporting.auxiliary.log_hpfeeds) Connected to hpfeed broker.
    2013-03-04 09:40:57,994 (glastopf.glastopf) Glastopf started and privileges dropped.
    2013-03-04 09:41:05,954 (glastopf.glastopf) 127.0.0.1 requested GET / on localhost:8080
    2013-03-04 09:41:06,027 (glastopf.glastopf) 127.0.0.1 requested GET /style.css on localhost:8080
    2013-03-04 09:41:06,129 (glastopf.glastopf) 127.0.0.1 requested GET /favicon.ico on localhost:8080vicon.ico on 192.168.1.145:8080

