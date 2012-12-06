===========
Background
===========

General approach: Vulnerability type emulation instead of vulnerability emulation.
Idea: Once 'perfectly' emulated we are able to handle unknown attacks from the same type.
Implementation might be more complicated and delays the proper handling but once in place we are ahead of the
attackers until the come up with a new method or flaw in on our side.
Modular design to add new logging capabilities or attack type handler.
Various database capabilities already in place. HPFeeds logging for centralized data collection.
Popular attack type emulation already in place.
Remote File Inclusion via a build-in PHP sandbox, Local file Inclusion providing files from a virtual file system and HTML injection via POST requests.
The adversaries usually use search engines and special crafted search requests to find their victims.
In order to attract them, Glastopf provide those keywords (aka dork) and extracts them also from request and extends it's attack surface automatically.
So over time and with a growing number of attacks, the honeypot gets more and more attractive.
In the feature we will make the SQL injection emulator pubic, provide IP profiling for crawler recognition and intelligent dork selection.

Feasible Solution for the Web Threat Jigsaw
--------------------------------------------
Web sites are today's biggest and most vulnerable attack surface. A single compromised page can give you a lot of bang for your bugs.

Learning from expensive breaches was never feasible. We will explain how to use Honeypot, Sandbox and Botnet monitoring technology to gain
information about current threats which ultimately helps us to find vulnerabilities before they get exploited, insight into the malware
distribution network and the botnets used for mass exploitation.

Slides: :download:`pdf </_static/Feasible_Web_Threat_Solution.pdf>` (408kb)

Video: `Youtube <http://www.youtube.com/watch?v=kipxPRXKlXY>`_ (15 minutes)