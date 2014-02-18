# Copyright (C) 2013 Johnny Vestergaard <jkv@unixcluster.dk>
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

import requests
from requests.exceptions import Timeout, ConnectionError
import json
import logging

logger = logging.getLogger(__name__)


class Mnem_Service():
    #yes google hackers, these credentials are left here by purpose!
    def get_dorks(self, username='glastopf', password='glastopf', limit=1000, timeout=5):
        base_url = 'https://mnemosyne.honeycloud.net:8282'

        sess = requests.Session()
        try:
            #login and store session cookie
            payload = {'username': username, 'password': password}
            response = sess.post(base_url + '/login', payload, timeout=timeout, verify=False)
            if response.status_code != 200:
                logger.warning("Error while requesting session cookie from mnemosyne: {0}".format(response.status_code))
                return []

            #get the dorks
            response = sess.get(base_url + '/api/v1/aux/dorks?limit={0}'.format(limit), timeout=timeout, verify=False)

            if response.status_code == 200:
                dorks = json.loads(response.text)['dorks']
                logger.debug("Successfully retrieved {0} dorks from the mnemosyne service.".format(len(dorks)))
            else:
                logger.warning("Error while requesting dorks from mnemosyne: {0}".format(response.status_code))
                return []
        except (Timeout, ConnectionError) as e:
            logger.warning("Error while communication with mnemosyne: {0}".format(e))
            return []

        #align with glastopf db setup
        return_list = []
        for item in dorks:
            return_list.append({'content': item['content'],
                                'table': item['type']})
        return return_list
