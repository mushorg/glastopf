==========
Braindump
==========

Attack classification
----------------------
We can use the PHPIDS rules? https://dev.itratos.de/projects/php-ids/repository/entry/trunk/lib/IDS/default_filter.xml

SPDY
-----
Do we want to support SPDY? http://dev.chromium.org/spdy/spdy-protocol/spdy-protocol-draft1

PHP Interpreter
----------------
The REAL PHP interpreter would be awesome for RFI analysis and response generation. Maybe separated from the honeypot.
I'm working on a modified version of Jose Nazario's PHP sandbox using funcall for PHP script analysis: http://monkey.org/~jose/software/rfi-sandbox/
I'll add the code to Glastopf later.
We should think about if we want to provide this as a service for Glastopf instances.

SQL interpreter
----------------
Interpreter for SQL injections?

Jeremy: I guess detection of SQL input might be detected with the key Data Description and Manipulation Language keywords (CREATE, INSERT, etc). Wouldn't be very hard to discover the attacker's purpose. What's interesting to explore might be a probabilistic SQL module to the honeypot. 

Jeremy's Dump after attending PyCon APAC
=========================================

mod_wsgi
---------
Possible integration option with the Apache webserver? Perhaps as a setup option as a complement to investigate attacks on an exposed/production server?

Lukas: Maybe setting up Apache as a proxy to Glastopf?

python curses
--------------
Cool terminal interface.

Modular Structure
------------------
A general purpose honeypot extensible by Python modules?

Lukas: You mean more general than a web server honeypot? I'm not sure if this is too much ;)