import unittest

from glastopf.modules.HTTP.handler import HTTPHandler, HTTPError


class TestHTTPParsing(unittest.TestCase):
    """Tests the honeypots vulnerable string selection.
    We first start with the integration test and continue with unit tests"""

    def test_simple_get_request(self):
        """Test simple GET request"""
        http_handler = """GET /test HTTP/1.0\r\nUser-Agent: test\r\n\r\n"""
        http_parser = HTTPHandler(http_handler, None)
        self.assertTrue(http_parser.request_path == "/test")

    def test_get_request_with_encoded_space(self):
        """Test simple GET request with space url encoded in the request path"""
        request_with_spaces = """GET /pathwith%20spaces HTTP/1.0\r\nUser-Agent: test\r\n\r\n"""
        http_handler = HTTPHandler(request_with_spaces, None)
        self.assertTrue(http_handler.request_path == "/pathwith%20spaces")

    def test_get_request_with_space(self):
        """Test that a simple GET request with space in the request path fails"""
        request_with_spaces = """GET /path with spaces?param1=value1\r\nHTTP/1.0\r\nUser-Agent: test\r\n\r\n"""
        self.assertRaises(HTTPError, HTTPHandler, request_with_spaces, None)

    def test_parse_command(self):
        """ Test if the parser is able to extract the HTTP command (verb)"""
        get_request = """GET /test HTTP/1.0\r\nUser-Agent: test\r\n\r\n"""
        http_handler = HTTPHandler(get_request, None)
        self.assertTrue(http_handler.request_verb == "GET")

    def test_parse_version1(self):
        """ Test if the parser is able to extract the HTTP version"""
        get_request = """GET /test HTTP/1.0\r\nUser-Agent: test\r\n\r\n"""
        http_handler = HTTPHandler(get_request, None)
        self.assertTrue(http_handler.request_version == "HTTP/1.0")

    def test_parse_version2(self):
        """ Test if the http handler is able to customize the server version string. """
        get_request = """GET /test HTTP/1.0\r\nUser-Agent: test\r\n\r\n"""
        http_handler = HTTPHandler(get_request, None, server_version="LEET_Server/0.1", sys_version="LEET_OS/1.0")
        self.assertEqual("LEET_Server/0.1 LEET_OS/1.0", http_handler.version_string())

    def test_put_method(self):
        http_handler = HTTPHandler('PUT / HTTP/1.0', None)
        self.assertTrue(http_handler.request_verb == "PUT")

    def test_get_method(self):
        http_handler = HTTPHandler('GET / HTTP/1.0', None)
        self.assertTrue(http_handler.request_verb == "GET")

    def test_post_method(self):
        http_handler = HTTPHandler('POST / HTTP/1.0', None)
        self.assertTrue(http_handler.request_verb == "POST")

    def test_head_method(self):
        http_handler = HTTPHandler('HEAD / HTTP/1.0', None)
        self.assertTrue(http_handler.request_verb == "HEAD")

    def test_trace_method(self):
        http_handler = HTTPHandler('TRACE / HTTP/1.0', None)
        self.assertTrue(http_handler.request_verb == "TRACE")

    def test_options_method(self):
        http_handler = HTTPHandler('OPTIONS / HTTP/1.0', None)
        self.assertTrue(http_handler.request_verb == "OPTIONS")


if __name__ == '__main__':
    unittest.main()
