#!/usr/bin/env python

# Copyright (C) 2014  Lukas Rist
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import os
import logging

from gevent import Timeout
import gevent.subprocess


logger = logging.getLogger(__name__)


def sandbox(script, secs, data_dir):
    proc = None
    stdout_value = ""
    try:
        proc = gevent.subprocess.Popen(
            ["php", os.path.join(data_dir, "sandbox.php"), os.path.join(data_dir, "files", script)],
            shell=False,
            stdin=gevent.subprocess.PIPE,
            stdout=gevent.subprocess.PIPE,
            stderr=gevent.subprocess.PIPE,
        )
    except Exception as e:
        logger.exception("Error executing the sandbox:".format(e))
    try:
        with Timeout(secs, False):
            if proc:
                stdout_value, stderr_value = proc.communicate()
    except Exception as e:
        logger.exception("Sandbox communication error:".format(e))
    else:
        logger.info("File successfully parsed with sandbox.")
    return stdout_value


def run(script, data_dir):
    secs = 10
    return sandbox(script, secs, data_dir)
