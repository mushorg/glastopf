<?php
if(!extension_loaded('apd')) {
	dl('apd.so');
}

$PHP_OS = 'Uber-Linux';
rename_function('php_uname', 'php_uname_633');
override_function('php_uname', '', 'return php_uname_rep();');
function php_uname_rep() {
	return 'Linux Server 2.6.38-11-generic #49-Ubuntu SMP Mon Aug 29 20:47:58 UTC 2011 i686';
}
rename_function('__overridden__', '0');

rename_function('popen', 'popen_290');
override_function('popen', '$cmd', 'return popen_rep($cmd);');
function popen_rep($cmd) {
	if ($cmd == 'id') {
		$temp = tmpfile();
		fwrite($temp, 'uid=0(root) gid=0(root) groups=0(root)');
		$ret = $temp;
	}
	else {
		$ret = tmpfile();
	}
	return $ret;
}
rename_function('__overridden__', '1');

rename_function('disk_free_space', 'disk_free_space_358');
override_function('disk_free_space', '', 'return disk_free_space_rep();');
function disk_free_space_rep() {
	return '36698988544';
}
rename_function('__overridden__', '2');

rename_function('system', 'system_790');
override_function('system', '$cmd, &$ret', 'return system_rep($cmd, &$ret);');
function system_rep($cmd, &$ret) {
	if ($cmd == 'id') {
		$ret = array('uid=0(root) gid=0(root) groups=0(root)',);
	}
	else {
		$ret = array('None',);
	}
}
rename_function('__overridden__', '3');

rename_function('shell_exec', 'shell_exec_900');
override_function('shell_exec', '$cmd', 'return shell_exec_rep($cmd);');
function shell_exec_rep($cmd) {
	if ($cmd == 'id') {
		$ret = array('uid=0(root) gid=0(root) groups=0(root)',);
	}
	else {
		$ret = array('None',);
	}
	return $ret;
}
rename_function('__overridden__', '4');

rename_function('diskfreespace', 'diskfreespace_427');
override_function('diskfreespace', '', 'return diskfreespace_rep();');
function diskfreespace_rep() {
	return '36698988544';
}
rename_function('__overridden__', '5');

rename_function('getcwd', 'getcwd_913');
override_function('getcwd', '', 'return getcwd_rep();');
function getcwd_rep() {
	return '/var/www';
}
rename_function('__overridden__', '6');

rename_function('exec', 'exec_284');
override_function('exec', '$cmd, &$ret', 'return exec_rep($cmd, &$ret);');
function exec_rep($cmd, &$ret) {
	if ($cmd == 'id') {
		$ret = array('uid=0(root) gid=0(root) groups=0(root)',);
	}
	else {
		$ret = array('None',);
	}
}
rename_function('__overridden__', '7');

rename_function('passthru', 'passthru_794');
override_function('passthru', '$cmd, &$ret', 'return passthru_rep($cmd, &$ret);');
function passthru_rep($cmd, &$ret) {
	if ($cmd == 'id') {
		$ret = array('uid=0(root) gid=0(root) groups=0(root)',);
	}
	else {
		$ret = array('None',);
	}
}
rename_function('__overridden__', '8');

rename_function('disk_total_space', 'disk_total_space_977');
override_function('disk_total_space', '', 'return disk_total_space_rep();');
function disk_total_space_rep() {
	return '51221590016';
}
rename_function('__overridden__', '9');

rename_function('ini_get', 'ini_get_729');
override_function('ini_get', '', 'return ini_get_rep();');
function ini_get_rep() {
	return '';
}
rename_function('__overridden__', '10');


include $argv[1];
?>
