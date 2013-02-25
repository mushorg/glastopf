# Copyright (C) 2011  Lukas Rist
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
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import glastopf
from urllib import quote

def reconstruct_request(environ):
    url = environ["REQUEST_METHOD"] + " "
    url += quote(environ.get('SCRIPT_NAME', ''))
    url += quote(environ.get('PATH_INFO', ''))
    if environ.get('QUERY_STRING'):
        url += '?' + environ['QUERY_STRING']
    url += " HTTP/1.1\r\n"
    header = "Host: " + quote(environ.get('HTTP_HOST')) + "\r\n"
    request = url + header + "\r\n\r\n"
    return request

def application(environ, start_response):
    request = reconstruct_request(environ)
    status = '200 OK' # HTTP Status
    headers = [('Content-type', 'text/plain')] # HTTP Headers
    start_response(status, headers)
    glastopf_honeypot = glastopf.GlastopfHoneypot()
    # FIXME: Provide the real requesting IP address
    response = glastopf_honeypot.handle_request(request, addr = "127.0.0.1").split("\r\n\r\n")[1]
    return [response]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('', 8080, application)
    print "Listening on port 8080...."
    httpd.serve_forever()