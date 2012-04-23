import re

class SQLiEmulator(object):
    """
    Emulates a SQL injection vulnerability and a successful attack.
    """
    
    def __init__(self):
        pass
    
    def extract_hex(self, url):
        """
        Extracts HEX encoded parts of the request based on a re pattern.
        """
        # TODO: Extract HEX encoded strings from request
        hex_pattern = r".*(?<hexstring>0x[a-fA-F0-9]{10,}).*"
        preg = re.compile(hex_pattern)
        hex_str = ""
        return hex_str

    def hex_to_ascii(self, hex_encoded):
        """
        Decodes the hex encoded string into ascii.
        """
        # TODO: Decode HEX encoded string
        ascii_str = ""
        return ascii_str

    def handle(self, attack_event):
        """
        Attackers are testing for a SQL vulnerability by injecting a string
        and checking if the string reappears in the web application response.
        So we are trying to extract the usually HEX encoded string and add
        it to our response.
        """
        # TODO: Implement SQL injection handler
        extracted_hex_str = self.extract_hex(attack_event.parsed_request.url)
        extracted_ascii_str = self.hex_to_ascii(extracted_hex_str)
        # TODO: Embed the ascii string properly into an error msg
        attack_event.response += extracted_ascii_str