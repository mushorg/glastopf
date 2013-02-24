# Copyright (C) 2013  Johnny Vestergaard <jkv@unixcluster.dk>
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
import shutil
import pkgutil

#  * Copy config file
#  * Copy and activate sandbox
#  * Setup pages (dork) stuff
#  * Various other stuff?

#sets up a basic directory glastopf can operate off

def bootstrap(bootstrap_dir):
    if len(os.listdir(bootstrap_dir)) != 0:
        raise Exception('Only bootstrapping of empty directories are supported..')

    #get path of glastopf module
    m_path = os.path.dirname(pkgutil.get_loader('glastopf').filename)

    shutil.copyfile(os.path.join(m_path, 'glastopf/glastopf.cfg.dist'),
                    os.path.join(bootstrap_dir, 'glastopf.cfg'))

    #directory for module level data
    os.makedirs(os.path.join(bootstrap_dir, 'data'))
