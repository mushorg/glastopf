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

BFR - Extension
---------

As Glastopf overrides the internal core functions of PHP, there must be some extension modifying the way PHP handles
function calls.

Glastopf uses Better Function Replacer(BFR) `[1] <https://github.com/mushorg/BFR>`_ developed by Lukas Rist. BFR is a Zend extension based on Advanced PHP Debugger(APD).
BFR extension enables implementation of Overriding and Renaming functions in the PHP sandbox. In order to use the BFR
extension it must be installed and properly configured, all instructions for the same can be found here `[1] <https://github.com/mushorg/BFR>`_.

BFR - How It Works
------------------

BFR extension is developed considering its usage in both multi and single threaded application.

General Synatax for rename and override function

rename function

.. code-block:: php

	rename_function('original function', 'new function');
	
override function	

.. code-block:: php

	override_function('original function', 'arguments', 'new functions implementation code');


Below are two approach followed for developing 'rename' and 'override' functions.

**Approach followed for rename function:**

1 The original function is searched in the global function table and pointer with its function data is returned.

.. code-block:: c

	zend_hash_find(EG(function_table), Z_STRVAL_P(z_orig_fname),
					  Z_STRLEN_P(z_orig_fname) + 1, (void **) &func); 
					  
2 Similarly the new name assigned to the function is checked for presence in the global function table, So that it can be safely assigned to the old function.

3 New function is added in the global function table with function data pointing to old function.

.. code-block:: c

	zend_hash_add(EG(function_table), Z_STRVAL_P(z_new_fname),
					 Z_STRLEN_P(z_new_fname) + 1, func, sizeof(zend_function),
					 NULL);

4 Now old function is removed from global function table.

.. code-block:: c

	zend_hash_del(EG(function_table), Z_STRVAL_P(z_orig_fname),
					 Z_STRLEN_P(z_orig_fname) + 1);
					 
Thus old function name is replaced by new function name with function data pointer of old function pointing to new function.

**Approach followed for override function:**

1 All parameters of the override function are obtained and a special function "__overridden__" is created with characteristics of new overridden function. "eval code" represents the "__overridden__" function. TEMP_OVRD_FUNC_NAME represents __overridden__  function.

.. code-block:: c
	
	sprintf(eval_code, "function " TEMP_OVRD_FUNC_NAME "(%s){%s}",
			Z_STRVAL_P(z_function_args), Z_STRVAL_P(z_function_code));
			
2 __overridden__ function is executed so that global function table updates itself with new __overridden__ function.

.. code-block:: c

	zend_eval_string(eval_code, NULL, eval_name TSRMLS_CC);
	
3 If everything goes well, the new __overridden__ function is searched in the global function table and its function data pointer is reserved.

.. code-block:: c
	
	zend_hash_find(EG(function_table), TEMP_OVRD_FUNC_NAME,
						   sizeof(TEMP_OVRD_FUNC_NAME), (void **) &func);
						   
4 Now original function is added back to global function table with its function data pointer pointing to that of __overridden__ functions'.

.. code-block:: c
	
	zend_hash_add(EG(function_table), Z_STRVAL_P(z_function_name),
						 Z_STRLEN_P(z_function_name) + 1, func, sizeof(zend_function),
						 NULL)
						 
Thus original function's implementation is replaced with new overriding implementation.

Note: Still __overridden__ is present in global function table.
						 

References
----------
1. https://github.com/mushorg/BFR



