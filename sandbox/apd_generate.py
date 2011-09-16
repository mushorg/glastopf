#!/usr/bin/env python

import random

import apd_functions

def output(s):
    print s

FUNCTIONS = apd_functions.FUNCTIONS

output("<?php\nif(!extension_loaded('apd')) {\n\tdl('apd.so');\n}\n")
output("$PHP_OS = 'Uber-Linux';")
int = 0
for function, return_val in FUNCTIONS.items():
    parts = function.split(";")
    function_name = parts[0]
    function_args = ", ".join(parts[1:-1])
    rand_int = random.randint(100, 999)
    output("rename_function('%s', '%s_%s');" % (function_name, function_name, rand_int))
    output("override_function('%s', '%s', 'return %s_rep(%s);');" % (function_name, function_args, function_name, function_args))
    output("function %s_rep(%s) {" % (function_name, function_args))
    if return_val == "":
        return_val = "\treturn '%s';" % function_name
    elif return_val == "None":
        return_val = "\treturn;"
    output(return_val)
    #output("\terror_log(\"ret:%s(\" . join(', ', $args) . \")= \" . $result);" % function_name)
    output("}")
    output("rename_function('__overridden__', '%s');\n" % int)
    int += 1

output("\ninclude $argv[1];\n?>")