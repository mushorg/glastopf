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

import glastopf.modules.classification.request as request_classifier


class HTTPMethods(object):
    # TODO: Add more method handler

    def __init__(self, data_dir):
        self.data_dir = data_dir
        pass

    def GET(self, http_request):
        RequestClassifier = request_classifier.Classifier(self.data_dir)
        matched_pattern = RequestClassifier.classify_request(http_request)
        return matched_pattern

    def POST(self, http_request):
        RequestClassifier = request_classifier.Classifier(self.data_dir)
        matched_pattern = RequestClassifier.classify_request(http_request)
        #http_request.request_body -> File('files/payloads')
        return matched_pattern

    def HEAD(self, http_request):
        # TODO: Return the proper HEAD respone
        return "head"

    def TRACE(self, http_request):
        return "trace"

    def OPTIONS(self, http_request):
        # TODO: Return the proper OPTIONS respone
        return "options"
