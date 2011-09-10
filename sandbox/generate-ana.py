#!/usr/bin/env python

import functions

def output(s):
    print s

FUNCTIONS = functions.FUNCTIONS


output("""

def parse_fn(line):
    fn, args = line.split('(', 1)
    fn = fn.replace('call:', '').replace('ret:', '')
    args = [ x.strip().replace(')', '') for x in args.split(',') ]
    return fn, args

def parse_ret(line):
    call, res = line.split(')=', 1)
    fn, args = parse_fn(call)
    res = res.strip()
    return fn, args, res""")

output("""def ana(lines):
    for line in lines:
	if len(line) < 2:
	    continue""")
for function in set(FUNCTIONS):
    output("""
        elif line.startswith('call:""" + function + """'):
            proc, args = parse_fn(line)
            new_""" + function + """_call = (' '.join(args), '""" + function + """_call', args[0])
            print new_""" + function + """_call
        elif line.startswith('ret:""" + function + """'):
            proc, args, result = parse_ret(line)
            new_""" + function + """_ret = (' '.join(args), '""" + function + """_return', result)
            print new_""" + function + """_ret""")

#output('''\terror_log("call:%s(" . join(', ', $args) . ")");''' % fn)
