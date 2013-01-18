import os
import pwd
import grp
import logging

logger = logging.getLogger(__name__)


def recursive_chown(path, run_uid, run_gid):
    for root, dirs, files in os.walk(path):
        for single_dir in dirs:
            os.chown(os.path.join(root, single_dir), run_uid, run_gid)
        for single_file in files:
            os.chown(os.path.join(root, single_file), run_uid, run_gid)


def drop(new_uid='nobody', new_gid='nogroup'):
    starting_uid = os.getuid()
    starting_gid = os.getgid()

    if os.getuid() != 0:
        return
    if starting_uid == 0:
        run_uid = pwd.getpwnam(new_uid)[2]
        run_gid = grp.getgrnam(new_gid)[2]
        try:
            os.chown("files", run_uid, run_gid)
            os.chown("db", run_uid, run_gid)
            os.chown("log", run_uid, run_gid)
            recursive_chown("files", run_uid, run_gid)
            recursive_chown("db", run_uid, run_gid)
            recursive_chown("log", run_uid, run_gid)
            os.chown("modules/handlers/emulators/dork_list/pages",
                     run_uid, run_gid)
            os.chown("modules/handlers/emulators/dork_list/comments.txt",
                     run_uid, run_gid)
        except OSError as e:
            logger.exception("Could not change file owner: {0}".format(e))
        try:
            os.setgid(run_gid)
        except OSError as e:
            logger.exception("Could not set new group: {0}".format(e))

        try:
            os.setuid(run_uid)
        except OSError as e:
            logger.exception("Could not set net user: {0}".format(e))

        new_umask = 066
        try:
            os.umask(new_umask)
        except Exception as e:
            logger.error("Failed to change umask: {0}".format(e))

