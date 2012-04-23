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

import modules.classification.request as request_classifier


class HTTPMethods(object):
    # TODO: Add more method handler

    def __init__(self):
        pass

    def GET(self, parsed_request):
        RequestClassifier = request_classifier.Classifier()
        matched_pattern = RequestClassifier.classify_request(parsed_request)
        return matched_pattern

    def POST(self, parsed_request):
        RequestClassifier = request_classifier.Classifier()
        matched_pattern = RequestClassifier.classify_request(parsed_request)
        #parsed_request.body -> File('files/payloads')
        return matched_pattern

    def HEAD(self, parsed_request):
        # TODO: Return the proper HEAD respone
        return "head"

    def OPTIONS(self, parsed_request):
        # TODO: Return the proper OPTIONS respone
        return "options"
