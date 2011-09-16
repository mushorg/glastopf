def call():    
    function = """\tif ($varname == 'save_mode') {
\t\t$ret = 'None';
\t}
\telseif ($varname == 'disable_functions') {
\t\t$ret = 'None';
\t}
\telse {
\t\t$ret = 'None';
\t}"""
    return function