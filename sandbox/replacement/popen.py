def call():
    function = """\tif ($cmd == 'id') {
\t\t$temp = tmpfile();
\t\tfwrite($temp, 'uid=0(root) gid=0(root) groups=0(root)');
\t\t$ret = $temp;
\t}
\telse {
\t\t$ret = tmpfile();
\t}
\treturn $ret;"""
    return function