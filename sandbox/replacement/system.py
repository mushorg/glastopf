def call():    
    function = """\tif ($cmd == 'id') {
\t\t$ret = array('uid=0(root) gid=0(root) groups=0(root)',);
\t}
\telse {
\t\t$ret = array('None',);
\t}"""
    return function