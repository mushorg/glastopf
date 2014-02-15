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

import random
import string
import os


PASSWD_STATIC = """root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/bin/sh
man:x:6:12:man:/var/cache/man:/bin/sh
lp:x:7:7:lp:/var/spool/lpd:/bin/sh
mail:x:8:8:mail:/var/mail:/bin/sh
news:x:9:9:news:/var/spool/news:/bin/sh
uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh
proxy:x:13:13:proxy:/bin:/bin/sh
www-data:x:33:33:www-data:/var/www:/bin/sh
backup:x:34:34:backup:/var/backups:/bin/sh
list:x:38:38:Mailing List Manager:/var/list:/bin/sh
irc:x:39:39:ircd:/var/run/ircd:/bin/sh
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
libuuid:x:100:101::/var/lib/libuuid:/bin/sh
Debian-exim:x:101:104::/var/spool/exim4:/bin/false
statd:x:102:65534::/var/lib/nfs:/bin/false
sshd:x:103:65534::/var/run/sshd:/usr/sbin/nologin"""

SHADOW_STATIC = """daemon:*:16083:0:99999:7:::
bin:*:16083:0:99999:7:::
sys:*:16083:0:99999:7:::
sync:*:16083:0:99999:7:::
games:*:16083:0:99999:7:::
man:*:16083:0:99999:7:::
lp:*:16083:0:99999:7:::
mail:*:16083:0:99999:7:::
news:*:16083:0:99999:7:::
uucp:*:16083:0:99999:7:::
proxy:*:16083:0:99999:7:::
www-data:*:16083:0:99999:7:::
backup:*:16083:0:99999:7:::
list:*:16083:0:99999:7:::
irc:*:16083:0:99999:7:::
gnats:*:16083:0:99999:7:::
nobody:*:16083:0:99999:7:::
libuuid:!:16083:0:99999:7:::
Debian-exim:!:16083:0:99999:7:::
statd:*:16083:0:99999:7:::
sshd:*:16083:0:99999:7:::"""

GROUP_STATIC = """root:x:0:
daemon:x:1:
bin:x:2:
sys:x:3:
adm:x:4:
tty:x:5:
disk:x:6:
lp:x:7:
mail:x:8:
news:x:9:
uucp:x:10:
man:x:12:
proxy:x:13:
kmem:x:15:
dialout:x:20:
fax:x:21:
voice:x:22:
cdrom:x:24:
floppy:x:25:
tape:x:26:
sudo:x:27:
audio:x:29:
dip:x:30:
www-data:x:33:
backup:x:34:
operator:x:37:
list:x:38:
irc:x:39:
src:x:40:
gnats:x:41:
shadow:x:42:
utmp:x:43:
video:x:44:
sasl:x:45:
plugdev:x:46:
staff:x:50:
games:x:60:
users:x:100:
nogroup:x:65534:
libuuid:x:101:
crontab:x:102:
vboxsf:x:103:
Debian-exim:x:104:
mlocate:x:105:
ssh:x:106:"""


def _get_entry(user_id):
    # Random username of 3 characters
    name = "".join([random.choice(string.letters[:26]) for i in xrange(3)])
    gid = user_id
    uid = user_id
    g = "\n" + name + ":x:" + str(gid) + ":"
    p = "\n" + name + ":x:" + str(uid) + ":" + str(gid) + "::" + "/home/" + name + \
        "/:/bin/sh"
    # If we want to, we could also give a password hash in place of '*'
    s = "\n" + name + ":*:6723:0:99999:7:::"
    return p, s, g


def _gen_data():
    data = []
    num_entries = random.randint(1, 10)  # number of random entries
    for i in xrange(num_entries):
        # Possible duplication of user id, but very low probability
        user_id = random.randint(1000, 1500)
        data.append(_get_entry(user_id))
    return data


def _create_passwd(vpath, data):
    pwd_path = os.path.join(vpath, 'linux/etc/passwd')
    with open(pwd_path, "wb") as pwd:
        pwd.write(PASSWD_STATIC)
        for entry in data:
            pwd.write(entry[0])


def _create_shadow(vpath, data):
    shd_path = os.path.join(vpath, 'linux/etc/shadow')
    with open(shd_path, "wb") as shd:
        shd.write(SHADOW_STATIC)
        for entry in data:
            shd.write(entry[1])


def _create_group(vpath, data):
    grp_path = os.path.join(vpath, 'linux/etc/group')
    with open(grp_path, "wb") as grp:
        grp.write(GROUP_STATIC)
        for entry in data:
            grp.write(entry[2])


def randomize_vdocs(vpath):
    data = _gen_data()
    _create_passwd(vpath, data)
    _create_shadow(vpath, data)
    _create_group(vpath, data)