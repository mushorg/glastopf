<?php

if(!extension_loaded('apd')) {
	dl('apd.so');
}

rename_function('fwrite', 'fwrite_875');
function fwrite_rep() {
	echo("test2\n");
}
override_function('fwrite_875', '', 'return fwrite_rep();');
//rename_function('__overridden__', ''); 

rename_function('symlink', 'symlink_408');
rename_function('__overridden__', 'symlink');
function symlink_rep() {
	echo("test3\n");
}
override_function('symlink', '', 'return symlink_rep();');
//rename_function('__overridden__', 'symlink');

fwrite("test\n");
?>
