<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html dir="ltr" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml" lang="en"><head>



    <link rel="icon" href="http://rj1.locomotion.tw/phpmyadmin/favicon.ico" type="image/x-icon">
    <link rel="shortcut icon" href="http://rj1.locomotion.tw/phpmyadmin/favicon.ico" type="image/x-icon">
    <title>phpMyAdmin 2.10.1 setup</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

    <script type="text/javascript" language="javascript">
    //<![CDATA[
    // show this window in top frame
    if (top != self) {
        window.top.location.href=location;
    }
    //]]>
    </script>
    <style type="text/css">
    /* message boxes: warning, error, stolen from original theme */
    div.notice {
        color: #000000;
        background-color: #FFFFDD;
    }
    h1.notice,
    div.notice {
        margin: 0.5em 0 0.5em 0;
        border: 0.1em solid #FFD700;
        background-image: url(.././themes/original/img/s_notice.png);
        background-repeat: no-repeat;
        background-position: 10px 50%;
        padding: 10px 10px 10px 36px;
    }
    div.notice h1 {
        border-bottom: 0.1em solid #FFD700;
        font-weight: bold;
        font-size: large;
        text-align: left;
        margin: 0 0 0.2em 0;
    }

    div.warning {
        color: #CC0000;
        background-color: #FFFFCC;
    }
    h1.warning,
    div.warning {
        margin: 0.5em 0 0.5em 0;
        border: 0.1em solid #CC0000;
        background-image: url(.././themes/original/img/s_warn.png);
        background-repeat: no-repeat;
        background-position: 10px 50%;
        padding: 10px 10px 10px 36px;
    }
    div.warning h1 {
        border-bottom: 0.1em solid #cc0000;
        font-weight: bold;
        text-align: left;
        font-size: large;
        margin: 0 0 0.2em 0;
    }

    div.error {
        background-color: #FFFFCC;
        color: #ff0000;
    }
    h1.error,
    div.error {
        margin: 0.5em 0 0.5em 0;
        border: 0.1em solid #ff0000;
        background-image: url(.././themes/original/img/s_error.png);
        background-repeat: no-repeat;
        background-position: 10px 50%;
        padding: 10px 10px 10px 36px;
    }
    div.error h1 {
        border-bottom: 0.1em solid #ff0000;
        font-weight: bold;
        text-align: left;
        font-size: large;
        margin: 0 0 0.2em 0;
    }

    fieldset.toolbar form.action {
        display: block;
        width: auto;
        clear: none;
        float: left;
        margin: 0;
        padding: 0;
        border-right: 1px solid black;
    }
    fieldset.toolbar form.action input, fieldset.toolbar form.action select {
        margin: 0.7em;
        padding: 0.1em;
    }

    fieldset.toolbar {
        display: block;
        width: 100%;
        background-color: #dddddd;
        padding: 0;
    }
    fieldset.optbox {
        padding: 0;
        background-color: #FFFFDD;
    }
    div.buttons, div.opts, fieldset.optbox p, fieldset.overview div.row {
        clear: both;
        padding: 0.5em;
        margin: 0;
        background-color: white;
    }
    div.opts, fieldset.optbox p, fieldset.overview div.row {
        border-bottom: 1px dotted black;
    }
    fieldset.overview {
        display: block;
        width: 100%;
        padding: 0;
    }
    fieldset.optbox p {
        background-color: #FFFFDD;
    }
    div.buttons {
        background-color: #dddddd;
    }
    div.buttons input {
        margin: 0 1em 0 1em;
    }
    div.buttons form {
        display: inline;
        margin: 0;
        padding: 0;
    }
    input.save {
        color: green;
        font-weight: bolder;
    }
    input.cancel {
        color: red;
        font-weight: bolder;
    }
    div.desc, label.desc, fieldset.overview div.desc {
        float: left;
        width: 27em;
        max-width: 60%;
    }
    code:before, code:after {
        content: '"';
    }
    span.doc {
        margin: 0 1em 0 1em;
    }
    span.doc a {
        margin: 0 0.1em 0 0.1em;
    }
    span.doc a img {
        border: none;
    }
    </style>
</head><body>
<h1>phpMyAdmin 2.10.1 setup</h1>
<div class="notice">
<h1>Welcome</h1>
You want to configure phpMyAdmin using web interface. Please note that this only allows basic setup, please read <a href="http://rj1.locomotion.tw/phpmyadmin/Documentation.html#config">documentation</a> to see full description of all configuration directives.
</div>
<div class="warning">
<h1>Can not load or save configuration</h1>
Please create web server writable folder config in phpMyAdmin toplevel directory as described in <a href="http://rj1.locomotion.tw/phpmyadmin/Documentation.html#setup_script">documentation</a>. Otherwise you will be only able to download or display it.
</div>
<div class="warning">
<h1>Not secure connection</h1>
You are not using secure connection, all data (including sensitive,
like passwords) are transfered unencrypted! If your server is also
configured to accept HTTPS request follow <a href="https://rj1.locomotion.tw/phpmyadmin/scripts/setup.php">this link</a> to use secure connection.
</div>
<p>Available global actions (please note that these will delete any changes you could have done above):</p><fieldset class="toolbar"><legend>Servers</legend>
<form class="action" method="post" action=""><input name="token" value="${token_value}" type="hidden"><input name="action" value="addserver" type="hidden"><input value="Add" type="submit"><input name="configuration" value="a:1:{s:7:&quot;Servers&quot;;a:0:{}}" type="hidden">
<input name="eoltype" value="unix" type="hidden">
</form>
</fieldset>

<fieldset class="toolbar"><legend>Layout</legend>
<form class="action" method="post" action=""><input name="token" value="${token_value}" type="hidden"><input name="action" value="lay_navigation" type="hidden"><input value="Navigation frame" type="submit"><input name="configuration" value="a:1:{s:7:&quot;Servers&quot;;a:0:{}}" type="hidden">
<input name="eoltype" value="unix" type="hidden">
</form>
<form class="action" method="post" action=""><input name="token" value="${token_value}" type="hidden"><input name="action" value="lay_tabs" type="hidden"><input value="Tabs" type="submit"><input name="configuration" value="a:1:{s:7:&quot;Servers&quot;;a:0:{}}" type="hidden">
<input name="eoltype" value="unix" type="hidden">
</form>
<form class="action" method="post" action=""><input name="token" value="${token_value}" type="hidden"><input name="action" value="lay_icons" type="hidden"><input value="Icons" type="submit"><input name="configuration" value="a:1:{s:7:&quot;Servers&quot;;a:0:{}}" type="hidden">
<input name="eoltype" value="unix" type="hidden">
</form>
<form class="action" method="post" action=""><input name="token" value="${token_value}" type="hidden"><input name="action" value="lay_browse" type="hidden"><input value="Browsing" type="submit"><input name="configuration" value="a:1:{s:7:&quot;Servers&quot;;a:0:{}}" type="hidden">
<input name="eoltype" value="unix" type="hidden">
</form>
<form class="action" method="post" action=""><input name="token" value="${token_value}" type="hidden"><input name="action" value="lay_edit" type="hidden"><input value="Editing" type="submit"><input name="configuration" value="a:1:{s:7:&quot;Servers&quot;;a:0:{}}" type="hidden">
<input name="eoltype" value="unix" type="hidden">
</form>
<form class="action" method="post" action=""><input name="token" value="${token_value}" type="hidden"><input name="action" value="lay_window" type="hidden"><input value="Query window" type="submit"><input name="configuration" value="a:1:{s:7:&quot;Servers&quot;;a:0:{}}" type="hidden">
<input name="eoltype" value="unix" type="hidden">
</form>
</fieldset>

<fieldset class="toolbar"><legend>Features</legend>
<form class="action" method="post" action=""><input name="token" value="${token_value}" type="hidden"><input name="action" value="feat_upload" type="hidden"><input value="Upload/Download" type="submit"><input name="configuration" value="a:1:{s:7:&quot;Servers&quot;;a:0:{}}" type="hidden">
<input name="eoltype" value="unix" type="hidden">
</form>
<form class="action" method="post" action=""><input name="token" value="${token_value}" type="hidden"><input name="action" value="feat_security" type="hidden"><input value="Security" type="submit"><input name="configuration" value="a:1:{s:7:&quot;Servers&quot;;a:0:{}}" type="hidden">
<input name="eoltype" value="unix" type="hidden">
</form>
<form class="action" method="post" action=""><input name="token" value="${token_value}" type="hidden"><input name="action" value="feat_manual" type="hidden"><input value="MySQL manual" type="submit"><input name="configuration" value="a:1:{s:7:&quot;Servers&quot;;a:0:{}}" type="hidden">
<input name="eoltype" value="unix" type="hidden">
</form>
<form class="action" method="post" action=""><input name="token" value="${token_value}" type="hidden"><input name="action" value="feat_charset" type="hidden"><input value="Charsets" type="submit"><input name="configuration" value="a:1:{s:7:&quot;Servers&quot;;a:0:{}}" type="hidden">
<input name="eoltype" value="unix" type="hidden">
</form>
<form class="action" method="post" action=""><input name="token" value="${token_value}" type="hidden"><input name="action" value="feat_extensions" type="hidden"><input value="Extensions" type="submit"><input name="configuration" value="a:1:{s:7:&quot;Servers&quot;;a:0:{}}" type="hidden">
<input name="eoltype" value="unix" type="hidden">
</form>
<form class="action" method="post" action=""><input name="token" value="${token_value}" type="hidden"><input name="action" value="feat_relation" type="hidden"><input value="MIME/Relation/History" type="submit"><input name="configuration" value="a:1:{s:7:&quot;Servers&quot;;a:0:{}}" type="hidden">
<input name="eoltype" value="unix" type="hidden">
</form>
</fieldset>

<fieldset class="toolbar"><legend>Configuration</legend>
<form class="action" method="post" action=""><input name="token" value="${token_value}" type="hidden"><input name="action" value="main" type="hidden"><input value="Overview" type="submit"><input name="configuration" value="a:1:{s:7:&quot;Servers&quot;;a:0:{}}" type="hidden">
<input name="eoltype" value="unix" type="hidden">
</form>
<form class="action" method="post" action=""><input name="token" value="${token_value}" type="hidden"><input name="action" value="display" type="hidden"><input value="Display" type="submit"><input name="configuration" value="a:1:{s:7:&quot;Servers&quot;;a:0:{}}" type="hidden">
<input name="eoltype" value="unix" type="hidden">
</form>
<form class="action" method="post" action=""><input name="token" value="${token_value}" type="hidden"><input name="action" value="download" type="hidden"><input value="Download" type="submit"><input name="configuration" value="a:1:{s:7:&quot;Servers&quot;;a:0:{}}" type="hidden">
<input name="eoltype" value="unix" type="hidden">
</form>
<form class="action" method="post" action=""><input name="token" value="${token_value}" type="hidden"><input name="action" value="save" type="hidden"><input value="Save" disabled="disabled" type="submit"><input name="configuration" value="a:1:{s:7:&quot;Servers&quot;;a:0:{}}" type="hidden">
<input name="eoltype" value="unix" type="hidden">
</form>
<form class="action" method="post" action=""><input name="token" value="${token_value}" type="hidden"><input name="action" value="load" type="hidden"><input value="Load" disabled="disabled" type="submit"><input name="configuration" value="a:1:{s:7:&quot;Servers&quot;;a:0:{}}" type="hidden">
<input name="eoltype" value="unix" type="hidden">
</form>
<form class="action" method="post" action=""><input name="token" value="${token_value}" type="hidden"><input name="action" value="clear" type="hidden"><input value="Clear" type="submit"><input name="configuration" value="a:1:{s:7:&quot;Servers&quot;;a:0:{}}" type="hidden">
<input name="eoltype" value="unix" type="hidden">
</form>
<form class="action" method="post" action=""><input name="token" value="${token_value}" type="hidden"><input name="action" value="seteol" type="hidden"><select name="neweol"><option value="unix" selected="selected">UNIX/Linux (\n)</option><option value="dos">DOS/Windows (\r\n)</option><option value="mac">Macintosh (\r)</option>
        </select><input value="Change end of line" type="submit"><input name="configuration" value="a:1:{s:7:&quot;Servers&quot;;a:0:{}}" type="hidden">
<input name="eoltype" value="unix" type="hidden">
</form>
</fieldset>

<fieldset class="toolbar"><legend>Other actions</legend>
<form class="action" method="post" action=""><input name="token" value="${token_value}" type="hidden"><input name="action" value="versioncheck" type="hidden"><input value="Check for latest version" type="submit"><input name="configuration" value="a:1:{s:7:&quot;Servers&quot;;a:0:{}}" type="hidden">
<input name="eoltype" value="unix" type="hidden">
</form>
<form class="action" method="get" action="http://www.phpmyadmin.net/" target="_blank"><input name="token" value="${token_value}" type="hidden"><input value="Go to homepage" type="submit"></form>
<form class="action" method="get" action="https://sourceforge.net/donate/index.php" target="_blank"><input name="token" value="${token_value}" type="hidden"><input name="group_id" value="23067" type="hidden"><input value="Donate to phpMyAdmin" type="submit"></form>
</fieldset>

</body></html>
