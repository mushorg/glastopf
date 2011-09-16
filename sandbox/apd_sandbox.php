<?php
if(!extension_loaded('apd')) {
	dl('apd.so');
}

$PHP_OS = 'Uber-Linux';
rename_function('php_uname', 'php_uname_196');
override_function('php_uname', '', 'return php_uname_rep();');
function php_uname_rep() {
	return 'Linux Server 2.6.38-11-generic #49-Ubuntu SMP Mon Aug 29 20:47:58 UTC 2011 i686';
}
rename_function('__overridden__', '0');

rename_function('popen', 'popen_412');
override_function('popen', '', 'return popen_rep();');
function popen_rep() {
	return '';
}
rename_function('__overridden__', '1');

rename_function('shell_exec', 'shell_exec_538');
override_function('shell_exec', '', 'return shell_exec_rep();');
function shell_exec_rep() {
	return '';
}
rename_function('__overridden__', '2');

rename_function('diskfreespace', 'diskfreespace_872');
override_function('diskfreespace', '', 'return diskfreespace_rep();');
function diskfreespace_rep() {
	return '36698988544';
}
rename_function('__overridden__', '3');

rename_function('passthru', 'passthru_287');
override_function('passthru', '', 'return passthru_rep();');
function passthru_rep() {
	return '';
}
rename_function('__overridden__', '4');

rename_function('getcwd', 'getcwd_168');
override_function('getcwd', '', 'return getcwd_rep();');
function getcwd_rep() {
	return '/var/www';
}
rename_function('__overridden__', '5');

rename_function('exec', 'exec_183');
override_function('exec', '$cmd, &$ret', 'return exec_rep($cmd, &$ret);');
function exec_rep($cmd, &$ret) {
	if ($cmd == 'id') {
		$ret = array('uid=0(root) gid=0(root) groups=0(root)',);
	}
	else {
		$ret = array('None',);
	}
}
rename_function('__overridden__', '6');

rename_function('disk_free_space', 'disk_free_space_247');
override_function('disk_free_space', '', 'return disk_free_space_rep();');
function disk_free_space_rep() {
	return '36698988544';
}
rename_function('__overridden__', '7');

rename_function('disk_total_space', 'disk_total_space_988');
override_function('disk_total_space', '', 'return disk_total_space_rep();');
function disk_total_space_rep() {
	return '51221590016';
}
rename_function('__overridden__', '8');

rename_function('ini_get', 'ini_get_379');
override_function('ini_get', '', 'return ini_get_rep();');
function ini_get_rep() {
	return '';
}
rename_function('__overridden__', '9');

rename_function('system', 'system_383');
override_function('system', '', 'return system_rep();');
function system_rep() {
	return '';
}
rename_function('__overridden__', '10');


include $argv[1];
?>
