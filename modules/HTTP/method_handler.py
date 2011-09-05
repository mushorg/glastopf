import modules.classification.request as request_classifier

class HTTPMethods(object):
	def __init__(self):
		pass
	
	def GET(self, parsed_request):
		RequestClassifier = request_classifier.Classifier()
		RequestClassifier.classify_request(parsed_request)
		return "GET"
	
	def POST(self, parsed_request):
		return "POST"
	
	def HEAD(self, parsed_request):
		return "HEAD"