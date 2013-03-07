Glastopf |Build Status|
=======================

.. |Build Status| image:: https://travis-ci.org/glastopf/glastopf.png?branch=master
                       :target: https://travis-ci.org/glastopf/glastopf

ABOUT
-----

Glastopf is a Python web application honeypot founded by Lukas Rist.

General approach: Vulnerability type emulation instead of vulnerability emulation. Idea: Once 'perfectly' emulated we are able to handle unknown attacks from the same type. Implementation might be more complicated and delays the proper handling but once in place we are ahead of the attackers until the come up with a new method or flaw in on our side.
Modular design to add new logging capabilities or attack type handler. Various database capabilities already in place. HPFeeds logging for centralized data collection.
Popular attack type emulation already in place. Remote File Inclusion via a build-in PHP sandbox, Local file Inclusion providing files from a virtual file system and HTML injection via POST requests.
The adversaries usually use search engines and special crafted search requests to find their victims. In order to attract them, Glastopf provide those keywords (aka dork) and extracts them also from request and extends it's attack surface automatically. So over time and with a growing number of attacks, the honeypot gets more and more attractive.
In the feature we will make the SQL injection emulator pubic, provide IP profiling for crawler recognition and intelligent dork selection.

HPFEEDS
-------

The honeypot has hpfeeds, our central logging feature enabled by
default. If you don't want to report your events, turn of hpfeeds in
glastopf.cfg. By sending your data via hpfeeds you agree that your data
might be shared with 3rd parties. If you are interested in the data
collected by Glastopf instances, please contact Lukas at
glaslos@gmail.com

SUPPORT
-------

Thanks to JetBrains for free PyCharm licenses!

INSTALL
-------
Install instruction can be found on `here <https://github.com/glastopf/glastopf/tree/master/docs/source/installation>`_.