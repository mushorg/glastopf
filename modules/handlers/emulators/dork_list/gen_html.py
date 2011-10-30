from string import Template

def html_template(titlename, formURLname, bodycontent, footstr, csstemp):
    template = Template(u"""
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>${title}</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<style type="text/css">
    ${css_file}
</style>
</head>   
<body><div id="container">
      <fieldset><h1><center>${title}</center></h1></fieldset>
      <form action="${form_URL}" method="post" class="niceform">
        <fieldset> 
        <h2>Administrator Panel</h2>
        <dl>
            <dt><label for="email">Login:</label></dt>
            <dd><input type="text" name="login" id="login" size="32" maxlength="20" /></dd>
        </dl>
        <dl>
            <dt><label for="password">Password:</label></dt>
            <dd><input type="password" name="password" id="password" size="32" maxlength="32" /></dd>
        </dl>
        <dl>
            <dt><input type="submit" name="submit" id="submit" value="Submit" /></dt>
        </dl>
        </fieldset></form>
        <fieldset>
            <h2>My Resource</h2>
            <dl>
                <p>${bodystr}</p>
            </dl>
        </fieldset>
        <fieldset>
            <dl><p id="footer">${footer}</p></dl>
        </fieldset>
</div></body>
</html>"""
)
    return template.substitute(dict(title=titlename, form_URL=formURLname, bodystr=bodycontent), footer=footstr, css_file=csstemp)

def css():
    css_str = u"""/*Defaults Styling*/
body {font:14px/17px Arial, Helvetica, sans-serif; color:#333; background:#ccc; padding:40px 20px 20px 20px;}
fieldset {background:#9da2a6; padding:10px; border:1px solid #aaa; border-color:#fff #666661 #666661 #fff; margin-bottom:36px; width:80%;}
input, textarea, select {font:14px/14px Arial, Helvetica, sans-serif; padding:0;}
fieldset.action {background:#C9BE62; border-color:#e5e5e5 #797c80 #797c80 #e5e5e5; margin-top:-20px;}
label {font-size:14px; font-weight:bold; color:#666;}
label.opt {font-weight:normal;}
dl {clear:both; background:#9da2a6}
dt {float:left; text-align:right; width:90px; line-height:25px; margin:0 10px 10px 0;}
dd {float:left; width:475px; line-height:25px; margin:0 0 10px 0;}
#footer {font-size:11px;}

#container {width:80%; margin:0 auto;}

#header {
        background: white;
        height: 60px;
}

#h1 {
    margin: 0;
    padding: 0;
}

#h2 {
    font:16px/18px
    margin: 0;
    padding: 0;
}
"""
    return css_str



 