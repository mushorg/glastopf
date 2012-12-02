
import unittest

from modules.HTTP.util import HTTPRequest, HTTPParser


class TestHTTPParsing(unittest.TestCase):
    """Tests the honeypots vulnerable string selection.
    We first start with the integration test and continue with unit tests"""


    def test_simple_get_request(self):
        """Test simple GET request"""
        simple_request = """GET /test HTTP/1.0
        User-Agent: test

        """
        http_parser = HTTPParser()
        http_obj = http_parser.parse_request(simple_request)
        self.assertTrue(http_obj.url == "/test")

    def test_get_request_with_encoded_space(self):
        """Test simple GET request with space url encoded in the request path"""
        request_with_spaces = """GET /pathwith%20spaces HTTP/1.0
        User-Agent: test

        """
        http_parser = HTTPParser()
        http_obj = http_parser.parse_request(request_with_spaces)
        self.assertTrue(http_obj.url == "/pathwith spaces")

    def test_get_request_with_space(self):
        """Test simple GET request with space in the request path"""
        request_with_spaces = """GET /path with spaces?param1=value1 HTTP/1.0
        User-Agent: test

        """
        http_parser = HTTPParser()
        http_obj = http_parser.parse_request(request_with_spaces)
        self.assertTrue(http_obj.url == "/path with spaces?param1=value1")
        self.assertTrue(http_obj.parameters == "param1=value1")
        self.assertTrue(http_obj.version == "HTTP/1.0")

