Glastopf Installation - Docker
------------------------------
| 
| 

Prerequisites
=============
|

A server with `Docker <https://www.docker.io/>`_ installed

| 

Build the Docker container image
================================
|

    docker build --rm --tag glastopf .

|

Running the Docker container
============================
|

    mkdir myhoneypot1

    docker run --detach --publish 80:80 --volume myhoneypot1:/opt/myhoneypot glastopf

A new default glastopf.cfg has been created in *myhoneypot1*, which can be customized as required.

| 


Testing the Honeypot
====================
|

Use your web browser to visit your honeypot. You should see the following output on your command line::

	2013-03-14 08:34:08,129 (glastopf.glastopf) Initializing Glastopf using "/opt/myhoneypot" as work directory.
	2013-03-14 08:34:08,130 (glastopf.glastopf) Connecting to main database with: sqlite:///db/glastopf.db
	2013-03-14 08:34:08,152 (glastopf.modules.reporting.auxiliary.log_hpfeeds) Connecting to feed broker.
	2013-03-14 08:34:08,227 (glastopf.modules.reporting.auxiliary.log_hpfeeds) Connected to hpfeed broker.
	2013-03-14 08:34:11,265 (glastopf.glastopf) Glastopf started and privileges dropped.
	2013-03-14 08:34:32,853 (glastopf.glastopf) 192.168.10.85 requested GET / on 192.168.10.102
	2013-03-14 08:34:32,960 (glastopf.glastopf) 192.168.10.85 requested GET /style.css on 192.168.10.102
	2013-03-14 08:34:33,021 (glastopf.glastopf) 192.168.10.85 requested GET /favicon.ico on 192.168.10.102

