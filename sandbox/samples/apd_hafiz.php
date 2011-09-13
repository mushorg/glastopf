<?

rename_function('fsockopen', 'fsockopen__this_will_change__');
override_function('fsockopen', '', 'return fsockopen_mh();');
function fsockopen_mh(){
        echo("test2\n");
}
rename_function("__overridden__", "lala"); 

rename_function('exec','exec__this_will_change__');
override_function('exec', '$cmd', 'return exec_mh($cmd);');
function exec_mh($cmd){  echoXml("exec",  "\$cmd='". $cmd ."' ");        
}
rename_function("__overridden__", "lala2");


fsockopen();

?>
