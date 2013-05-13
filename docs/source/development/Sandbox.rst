===================================
Using and Understanding the Sandbox
===================================

Glastopf uses sandbox for PHP script Analysis. The latest sandbox implementation is based on Jose Nazario's PHP sandbox.

Understanding the Sandbox
-------------------------

The general idea for every sandbox is providing controlled access to external scripts executing on the current machine. Glastopf's sandbox follows the same approach with a different style of controlled access.

As Glastopf's sandbox is PHP based, all tweaks are done with PHP functions. What Glastopf does is, it overrides internal PHP functions excepts the white-list functions. Glastopf maintains a list of allowed functions called white-list functions. This means when a PHP script is tested against sandbox, all functions in the script that are in white-list behave naturally(as they are defined).

Now, other functions that are not in white-list are overridden by sandbox. It means that its default behavior is changed and molded as per output given by that function if it were not overridden. 

For eg, getcwd() function gives the current working directory when executed normally. when this will be executed against the sandbox, it will just return "/var/www".

This is because its default behavior of returning current working directory is changed to returning "/var/www"

Note: Currently not all functions that are internally defined are overridden, but are renamed so no malicious effect can be caused by them when they are executed against sandbox.

Using the Sandbox
-----------------

Developers who want to customize(override) internally defined functions must follow a simple approach.
    1. Rename the old function.
    2. Override the old function and define its new behavior
    3. Give a dummy name to __overridden__

A simple approach is followed for defining new behavior for the old function. 

Functions' implementation can be done in two ways, either returning the output directly or storing the output in the variable provided in argument.

For directly coding the new implementation, It can be coded directly in "glastopf/glastopf/sandbox/functions.py".

functions.py

.. code-block:: python

    FUNCTIONS = {"disk_free_space;" : "\treturn '%s';" % "36698988544"
		}

If the function is not returning the output directly rather storing the output in the variable provided as a argument, then it can be implemented as follows:
A file with function's name(overriding function) must be created in "glastopf/glastopf/sandbox/replacement/" containing the implementation and this must be imported in "glastopf/glastopf/sandbox/functions.py". 

functions.py

.. code-block:: python
  
     from replacement import execute

     FUNCTIONS = { "exec;$cmd;&$ret;" : execute.call()
		 }

system is created in replacement with implementation defined in "call" method.

execute.py

.. code-block:: python
    
    def call():
    function = """\tif ($cmd == 'id') {
	\t\t$ret = array('uid=0(root) gid=0(root) groups=0(root)',);
	\t}
	\telse {
	\t\t$ret = array('None',);
	\t}"""
    return function

If developer wants certain function to retain its natural behavior and it must be added in whitelist. 

