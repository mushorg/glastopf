def call():
    # TODO: Make uptime dynamic
    function = """\tif ($cmd == 'id') {
\t\t$ret = array('uid=0(root) gid=0(root) groups=0(root)',);
\t}
\telseif ($cmd == 'uptime') {
\t\t$ret = array('16:12:55 up 152 days, 19:03,  0 user,  load average: 0.02, 0.02, 0.03',);
\t}
\telse {
\t\t$ret = array('None',);
\t}"""
    return function