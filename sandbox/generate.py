#!/usr/bin/env python

import functions

def output(s):
    print s

FUNCTIONS = functions.FUNCTIONS

output("""<?php
if(!extension_loaded('funcall')) {
  dl('funcall.so');
   }
   """)

for fn in set(FUNCTIONS):
    output("function pre_%s_cb($args) {" % fn)
    output('''\terror_log("call:%s(" . join(', ', $args) . ")");''' % fn)
    output("}")

    output("function post_%s_cb($args, $result, $time) {" % fn)
    #output('\tprint "######### POST \n\n\n"; ')
    output("\terror_log(\"ret:%s(\" . join(', ', $args) . \")= \" . $result);" % fn)
    #output('\terror_log(print"\n");')
    output("}")


output('\n')

for fn in set(FUNCTIONS):
    output("fc_add_pre('%s', 'pre_%s_cb');" % (fn, fn))
    output("fc_add_post('%s', 'post_%s_cb');" % (fn, fn))

output("""

include $argv[1];
 ?>""")
