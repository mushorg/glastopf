import re

from xml.dom.minidom import parse

class RequestPattern(object):
	def __init__(self, id, string, description):
		self.id = id
		self.string = string
		self.description = description

class Classifier(object):
	def __init__(self):
		self.tree = parse("requests.xml")
	
	def get_patterns(self):
		patterns = self.tree.getElementsByTagName("request")
		return patterns
	
	def getText(self, nodelist):
		rc = []
		for node in nodelist:
			if node.nodeType == node.TEXT_NODE or node.nodeType == node.CDATA_SECTION_NODE:
				rc.append(node.data)
				break
		return ''.join(rc)
	
	def parse_pattern(self, pattern):
		pattern_id = self.getText(pattern.getElementsByTagName("id")[0].childNodes)
		pattern_string = self.getText(pattern.getElementsByTagName("patternString")[0].childNodes) 
		pattern_description = pattern.getElementsByTagName("patternDescription")[0].childNodes[0].data
		parsed_pattern = RequestPattern(pattern_id, pattern_string, pattern_description)
		return parsed_pattern
		
	def classify_request(self, parsed_request):
		patterns = self.get_patterns()
		matched_patterns = []
		for pattern in patterns:
			parsed_pattern = self.parse_pattern(pattern)
			re_pattern = re.compile(parsed_pattern.string)
			match = re_pattern.search(parsed_request.url)
			if match != None:
				matched_patterns.append(parsed_pattern.id)
		for id in matched_patterns:
			print id
		return matched_patterns