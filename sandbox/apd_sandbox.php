<?php
if(!extension_loaded('apd')) {
	dl('apd.so');
}

rename_function('getcwd', 'getcwd_250');
override_function('getcwd', '', 'return getcwd_rep();');
function getcwd_rep() {
	return '/var/www';
}
rename_function('__overridden__', '0');

rename_function('getmygid', 'getmygid_667');
override_function('getmygid', '', 'return getmygid_rep();');
function getmygid_rep() {
	return '0';
}
rename_function('__overridden__', '1');

rename_function('is_writable', 'is_writable_225');
override_function('is_writable', '', 'return is_writable_rep();');
function is_writable_rep() {
	return true;
}
rename_function('__overridden__', '2');

rename_function('function_exists', 'function_exists_153');
override_function('function_exists', '', 'return function_exists_rep();');
function function_exists_rep() {
	return true;
}
rename_function('__overridden__', '3');

rename_function('exec', 'exec_277');
override_function('exec', '$cmd, &$ret', 'return exec_rep($cmd, &$ret);');
function exec_rep($cmd, &$ret) {
	if ($cmd == 'id') {
		$ret = array('uid=0(root) gid=0(root) groups=0(root)',);
	}
	else {
		$ret = array('None',);
	}
}
rename_function('__overridden__', '4');

rename_function('passthru', 'passthru_416');
override_function('passthru', '$cmd, &$ret', 'return passthru_rep($cmd, &$ret);');
function passthru_rep($cmd, &$ret) {
	if ($cmd == 'id') {
		$ret = array('uid=0(root) gid=0(root) groups=0(root)',);
	}
	else {
		$ret = array('None',);
	}
}
rename_function('__overridden__', '5');

rename_function('disk_free_space', 'disk_free_space_222');
override_function('disk_free_space', '', 'return disk_free_space_rep();');
function disk_free_space_rep() {
	return '36698988544';
}
rename_function('__overridden__', '6');

rename_function('php_uname', 'php_uname_909');
override_function('php_uname', '', 'return php_uname_rep();');
function php_uname_rep() {
	return 'Linux Server 2.6.38-11-generic #49-Ubuntu SMP Mon Aug 29 20:47:58 UTC 2011 i686';
}
rename_function('__overridden__', '7');

rename_function('system', 'system_198');
override_function('system', '$cmd, &$ret', 'return system_rep($cmd, &$ret);');
function system_rep($cmd, &$ret) {
	if ($cmd == 'id') {
		$ret = array('uid=0(root) gid=0(root) groups=0(root)',);
	}
	elseif ($cmd == 'uptime') {
		$ret = array('16:12:55 up 152 days, 19:03,  0 user,  load average: 0.02, 0.02, 0.03',);
	}
	else {
		$ret = array('None',);
	}
}
rename_function('__overridden__', '8');

rename_function('disk_total_space', 'disk_total_space_254');
override_function('disk_total_space', '', 'return disk_total_space_rep();');
function disk_total_space_rep() {
	return '51221590016';
}
rename_function('__overridden__', '9');

rename_function('shell_exec', 'shell_exec_834');
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
rename_function('__overridden__', '10');

rename_function('get_current_user', 'get_current_user_422');
override_function('get_current_user', '', 'return get_current_user_rep();');
function get_current_user_rep() {
	return 'root';
}
rename_function('__overridden__', '11');

rename_function('getenv', 'getenv_316');
override_function('getenv', '$varname', 'return getenv_rep($varname);');
function getenv_rep($varname) {
	$ret = "";
	return $ret;
}
rename_function('__overridden__', '12');

rename_function('getmyuid', 'getmyuid_208');
override_function('getmyuid', '', 'return getmyuid_rep();');
function getmyuid_rep() {
	return '0';
}
rename_function('__overridden__', '13');

rename_function('diskfreespace', 'diskfreespace_515');
override_function('diskfreespace', '', 'return diskfreespace_rep();');
function diskfreespace_rep() {
	return '36698988544';
}
rename_function('__overridden__', '14');

rename_function('ini_get', 'ini_get_207');
override_function('ini_get', '$varname', 'return ini_get_rep($varname);');
function ini_get_rep($varname) {
	if ($varname == 'save_mode') {
		$ret = 'None';
	}
	elseif ($varname == 'disable_functions') {
		$ret = 'None';
	}
	else {
		$ret = 'None';
	}
}
rename_function('__overridden__', '15');

rename_function('is_callable', 'is_callable_762');
override_function('is_callable', '', 'return is_callable_rep();');
function is_callable_rep() {
	return true;
}
rename_function('__overridden__', '16');

rename_function('popen', 'popen_770');
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
rename_function('__overridden__', '17');


include $argv[1];
?>
