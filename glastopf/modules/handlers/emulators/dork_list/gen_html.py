from string import Template


def html_template(titlename, formURLname, bodycontent, footstr):
    template = Template(u"""
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>${title}</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link href="style.css" rel="stylesheet" type="text/css" />
</head>
<body><div id="container">
      <fieldset><h1><center>${title}</center></h1></fieldset>
      <fieldset> 
      <form action="${form_URL}" method="post" class="niceform">
        <h2>Administrator Panel</h2>
        ${login_msg}
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
        </form>
        </fieldset>
        <fieldset>
            <h2>My Resource</h2>
            <dl>
                <p>${bodystr}</p>
            </dl>
        </fieldset>
        <form action="comments" method="post" class="niceform">
        <fieldset> 
        <h2>Blog Comments</h2>
        <dl>
            <dl><label for="comments">Please post your comments for the blog</label></dl>
            <br/>
            <textarea name="comment" id="comment" rows="4" columns="300"> </textarea></dd>
        </dl>
        <dl>
            <dt><input type="submit" name="submit" id="submit" value="Submit" /></dt>
        </dl>
        ${comments}
        </fieldset></form>
        <fieldset>
            <dl><p id="footer">${footer}</p></dl>
        </fieldset>
</div></body>
</html>"""
    )
    return template.safe_substitute(
        dict(title=titlename, form_URL=formURLname, bodystr=bodycontent),
        footer=footstr)
