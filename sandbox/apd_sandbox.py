#!/usr/bin/env python

import time
import subprocess
import threading
from functools import partial   

VERSION='1.1'

"""Copyright by Jose Nazario, extended/modified by Lukas Rist"""

def killer(proc, secs):
    time.sleep(secs)
    try:
        proc.kill()
    except OSError:
        pass

def sandbox(prog, secs):
    try:
        proc = subprocess.Popen(["php", "sandbox/apd_sandbox.php", prog], 
                shell = False,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                )
    except Exception as e:
        print "PARENT : error executing the sandbox:"
        print e.message
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
    output = stdout_value
    return output
    
def run(script):
    secs = 10
    output = sandbox(script, secs)
    return output