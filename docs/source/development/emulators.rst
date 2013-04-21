=========
Emulators
=========

Developing an attack emulator
=============================

Introduction
------------
Glastopf's modular design allows for easy extension of the honeypot. This text will
briefly demonstrate how to build a simple emulator which will emulate the very popular, 
and imaginary, php beerservice.

Creating a new handler from scratch involves two steps:

1. Adding a detection rule.
2. Writing an emulator to handle the request.


Detection pattern
-----------------
A detection pattern is a regular expression which is tested against the url of
incoming requests. The following pattern will match all requests which starts
with ``/beerservice.php``.

.. code-block:: xml

    <request>
     <id>24</id>
     <patternDescription>beer service</patternDescription>
     <patternString><![CDATA[^/beerservice.php]]></patternString>
     <module>beerservice</module>
    </request>

All request patterns can be found in the requests.xml file.

Adding a basic emulator
-----------------------

To create this emulator (handler), we need to create a module (file) with a filename
that matches the ``<module>`` tag from the detection pattern. This module needs to be placed
in the ``emulators`` directory. The python file for the beerservice module will be placed at::

    glastopf/modules/handlers/emulators/beerservice.py

To create a basic handler we need to create a class with the following characteristics:

- Inherits from ``base_emulator.BaseEmulator``.
- Override the ``handle(self, attack_event)`` method to provide the needed emulation.

To return http response back to the client you need to call the ``attack_event.http_request.set_response`` method which
takes care of proper http header and other tedious stuff. If you need full control of the entire http response you can
use ``attack_event.http_request.set_response`` instead. The following code shows a simple implementation
of the beerservice emulator.

.. code-block:: python

    from glastopf.modules.handlers import base_emulator
    import urlparse

    class BeerManager(base_emulator.BaseEmulator):
        def __init__(self, data_dir):
            super(BeerManager, self).__init__(data_dir)

        def handle(self, attack_event):
            beer = attack_event.http_request.request_query['type][0]
            reponse = '{0} is a pretty lousy type of beer!'.format(beer)
            attack_event.http_request.set_response(reponse)


We can now start Glastopf and test our new emulator as follows.

.. code-block:: bash

    $ curl http://localhost:8080/beerservice.php?type=Rauchbier
    Rauchbier is a pretty lousy type of beer!

Adding files
------------
If you need to add datafiles, you can add these to the data directory at::

    glastopf/modules/handlers/emulators/data

All content of this directory will automatically be copied to the work directory
of Glastopf, which allows for easy customization. You can get the path to the
data directory by reading ``self.data_dir``.