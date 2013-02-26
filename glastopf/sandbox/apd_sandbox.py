#!/usr/bin/env python

import time
import subprocess
import threading
from functools import partial
import os

VERSION = '1.0'

"""Inspired by Jose Nazario's PHP sandbox, extended/modified by Lukas Rist"""


def killer(proc, secs):
    time.sleep(secs)
    try:
        proc.kill()
    except OSError:
        pass


def sandbox(script, secs, data_dir):
    proc = None
    try:
        proc = subprocess.Popen(["php5", os.path.join(data_dir, "apd_sandbox.php"),
                                 os.path.join(data_dir, "files", script)],
                                shell=False,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
        )
    except Exception as e:
        print "PARENT : error executing the sandbox:", e
    stdout_value = ""
    stderr_value = ""
    try:
        threading.Thread(target=partial(killer, proc, secs)).start()
        stdout_value, stderr_value = proc.communicate()
        print stdout_value
        print stderr_value
    except Exception as e:
        print "Sandbox communication error:", e
    else:
        print "Successfully parsed with sandbox"
    return stdout_value


def run(script, data_dir):
    secs = 10
    return sandbox(script, secs, data_dir)