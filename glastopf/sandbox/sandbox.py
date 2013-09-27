#!/usr/bin/env python

import time
import subprocess
import threading
from functools import partial
import os
import logging

# Inspired by Jose Nazario's PHP sandbox, extended/modified by Lukas Rist

logger = logging.getLogger(__name__)


def killer(proc, secs):
    time.sleep(secs)
    try:
        if proc:
            proc.kill()
    except OSError:
        pass


def sandbox(script, secs, data_dir):
    proc = None
    try:
        proc = subprocess.Popen(["php", os.path.join(data_dir, "sandbox.php"),
                                 os.path.join(data_dir, "files", script)],
                                shell=False,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
        )
    except Exception as e:
        logger.exception("Error executing the sandbox:".format(e))
    stdout_value = ""
    stderr_value = ""
    try:
        threading.Thread(target=partial(killer, proc, secs)).start()
        stdout_value, stderr_value = proc.communicate()
    except Exception as e:
        logger.exception("Sandbox communication error:".format(e))
    else:
        logger.info("File successfully parsed with sandbox.")
    return stdout_value


def run(script, data_dir):
    secs = 10
    return sandbox(script, secs, data_dir)
