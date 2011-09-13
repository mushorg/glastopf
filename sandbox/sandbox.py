#!/usr/bin/env python

import getopt
import os
import sys
import time
import hashlib
import subprocess
import threading
from functools import partial   

import ana

VERSION='1.1'

"""Copyright by Jose Nazario, extended/modified by Lukas Rist"""

def usage():
    print '%s -t sec script.php' % sys.argv[0]
    sys.exit(0)

def parse_fn(line):
    fn, args = line.split('(', 1)
    fn = fn.replace('call:', '').replace('ret:', '')
    args = [ x.strip().replace(')', '') for x in args.split(',') ]
    return fn, args

def parse_ret(line):
    # ret:exec(id, )= uid=500(jose) gid=500(jose) groups=10(wheel),500(jose)
    call, res = line.split(')=', 1)
    fn, args = parse_fn(call)
    res = res.strip()
    return fn, args, res
    
def distill_out(prog, start, end, output):
    return output

def distill_err(prog, start, end, output):
    
    buffer = open(prog, 'rb').read()
    connections = {}
    conversation_seq = 0
    virtual_fn = prog
    virtual_path = os.path.realpath(prog)
    md5 = hashlib.md5(buffer).hexdigest()
    sha1 = hashlib.sha1(buffer).hexdigest()
    file_size = len(buffer)
    
    processes = []
    ana.ana(output.split('\n'))
    
    unknown_tcp_traffic = []
    for tcp_conversation in connections.values():
        unknown_tcp_traffic.append(tcp_conversation)
    
    return processes, connections, unknown_tcp_traffic

def killer(proc, secs):
    time.sleep(secs)
    print "CHILDREN : killing the sandbox"
    try:
        proc.kill()
    except OSError:
        print "CHILDREN : Process already finished"

def sandbox(prog, secs):
    try:
        proc = subprocess.Popen(['php', 'sandbox/sandbox.php', prog], 
                shell = False,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                )
    except Exception as e:
        print "PARENT : error executing the sandbox:"
        print e.message
    print 'PARENT : Pausing before killing...'
    stdout_value = ""
    stderr_value = ""
    try:
        start = time.time()
        threading.Thread(target=partial(killer, proc, secs)).start()
        stdout_value, stderr_value = proc.communicate()
    except Exception as e:
        print "Communication error:", e.message
    finally:
        end = time.time()
    output = distill_out(prog, start, end, stdout_value)
    print output
    processes, connections, unknown_tcp_traffic = distill_err(prog, start, end, stderr_value)
    return output
    #sys.exit(0)

def main():
    secs = 20
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'k:l:')
    except: 
        usage()
    for o, a in opts:
        if o == '-t':
            secs = int(a)
    if len(args) < 1: 
        usage()
    else: 
        prog = args[0]
    # run the sandbox
    sandbox(prog, secs)
    
def run(script):
    secs = 10
    output = sandbox(script, secs)
    return output