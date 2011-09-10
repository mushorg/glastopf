#!/usr/bin/env python

import getopt
import os
import sys
import time
import hashlib
import socket
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

    for line in output.split('\n'):
        #print "line:", line
        if line.startswith('call:exec'):
            # call:exec(id, )
            proc, args = parse_fn(line)
            new_proc = (' '.join(args), 'process_spawn', args[0])
            processes.append(new_proc)
        elif line.startswith('call:diskfreespace'):
        # call:diskfreespace(/home/user/rfi-sandbox)
            proc, args = parse_fn(line)
            new_diskfreespace_call = (' '.join(args), 'diskfreespace_call', args[0])
            print new_diskfreespace_call
        elif line.startswith('ret:diskfreespace'):
        # ret:diskfreespace(/home/user/rfi-sandbox) = 45231578
            proc, args, result = parse_ret(line)
            new_diskfreespace_ret = (' '.join(args), 'diskfreespace_return', result)
            print new_diskfreespace_ret
        elif line.startswith('call:getcwd'):
            # call:getcwd()
            proc, args = parse_fn(line)
            new_getcwd_call = (' '.join(args), 'getcwd_call', args[0])
            print new_getcwd_call
        elif line.startswith('ret:getcwd'):
        # ret:getcwd()= /home/user/rfi-sandbox
            proc, args, result = parse_ret(line)
            new_getcwd_ret = (' '.join(args), 'getcwd_return', result)
            print new_getcwd_ret
        elif line.startswith('call:system'):
            # call:system(id)
            proc, args = parse_fn(line)
            new_sys_call = (' '.join(args), 'system_call', args[0])
            print new_sys_call
        elif line.startswith('ret:system'):
            # ret:system(id)= uid=1000(glaslos) gid=1000(glaslos) groups=1000(glaslos)
            proc, args, result = parse_ret(line)
            new_sys_ret = (' '.join(args), 'system_return', result)
            print new_sys_ret
        elif line.startswith('ret:fsockopen'):
            # call:fsockopen(irc, 6667, , , 30)
            proc, args, result = parse_ret(line)
            try:
                ip = socket.inet_aton(args[0])
                ip = args[0]
            except:
                try: ip = socket.gethostbyname(args[0])
                except: ip = args[0]
            tcp_conversation = (ip, args[1])
            connections[result] = tcp_conversation
        elif line.startswith('call:fwrite'):
            # call:fwrite(Resource id #5, PASS fx\n)
            proc, args = parse_fn(line)
            tcp_conversation = connections.get(args[0], False)
            if tcp_conversation:
                data = ana.data(direction='sent',
                               seq = conversation_seq,
                               valueOf_=args[1].strip())
                tcp_conversation.add_data(data)
                connections[args[0]] = tcp_conversation
                conversation_seq += 1
        elif line.startswith('ret:fgets'):
            # ret:fgets(Resource id #5, 512)= :irc.aa.arbor.net NOTICE Auth :*** Looking up your hostname...
            proc, args, result = parse_ret(line)
            tcp_conversation = connections.get(args[0], False)
            if tcp_conversation:
                data = ana.data(direction='received',
                               seq = conversation_seq,
                               valueOf_=args[1].strip())
                tcp_conversation.add_data(data)
                connections[args[0]] = tcp_conversation
                conversation_seq += 1
        elif line.startswith('ret:ini_get'):
            # ret:ini_get(disable_functions)=
            proc, args, result = parse_ret(line)
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
        proc = subprocess.Popen(['php', 'sandbox.php', prog], 
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
    print connections, processes
    sys.exit(0)

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

if __name__ == '__main__':
    main()