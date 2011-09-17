import re

class LFIEmulator(object):
    def __init__(self):
        pass
    
    def getVirtualPath(self, injected_path):
        """Sanitises and simulates a file path with a virtual root of the corresponding virtualdocs directory."""
        
        # Strip leading ../
        pass

    def getContents(self, injected_path):
        preg = re.compile(r'/.*\?.*=(.*)&?')
        result = preg.match(injected_path)
        read_data = ""
        try:
            with open("virtualdocs/linux/" + result.group(1), "r") as f:
                read_data = f.read()
        except IOError:
            # Placeholder file not found error
            read_data = "Warning: include(vars1.php): failed to open stream: No such file or directory in /var/www/html/anonymous/test.php on line 6 Warning: include(): Failed opening 'vars1.php' for inclusion (include_path='.:/usr/share/pear:/usr/share/php') in /var/www/html/anonymous/test.php on line 6" 
        return read_data
