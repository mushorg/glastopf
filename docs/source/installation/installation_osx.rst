Glastopf Installation
----------------------
| 
| 

Prerequisites OS X (Mountain Lion
====================
| 

Install the xcode and gfortran::  

    Install xcode from App Store
    brew install gfortran
| 

Setup virtual environment
================================
| 

The ANTLR runtime is needed to analyze SQL injections::

    virtualenv glastopf-virt --system-site-packages
    source glastopf-virt/glastopf/bin/activate
    pip install glastopf

| 

Starting the honeypot
=========================
| 

Prepare glastopf environment::
Note: Before using the follow command make sure you are operating within the virtual environment.

	cd 
	mkdir myhoneypot
	cd myhoneypot
	glastopf-runner

If you receive errors regarding syslog when starting glastopf, please update the syslog path in glastopf.cfg::

   [syslog]
   enabled = False
   socket = /var/run/syslog

Testing the Honeypot
====================
|

Start Glastopf (from your 'myhoneypot' directory)::

    glastopf-runner

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

