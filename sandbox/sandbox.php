<?php
if(!extension_loaded('funcall')) {
  dl('funcall.so');
   }
   
function pre_socket_recvfrom_cb($args) {
	error_log("call:socket_recvfrom(" . join(', ', $args) . ")");
}
function post_socket_recvfrom_cb($args, $result, $time) {
	error_log("ret:socket_recvfrom(" . join(', ', $args) . ")= " . $result);
}
function pre_basename_cb($args) {
	error_log("call:basename(" . join(', ', $args) . ")");
}
function post_basename_cb($args, $result, $time) {
	error_log("ret:basename(" . join(', ', $args) . ")= " . $result);
}
function pre_fclose_cb($args) {
	error_log("call:fclose(" . join(', ', $args) . ")");
}
function post_fclose_cb($args, $result, $time) {
	error_log("ret:fclose(" . join(', ', $args) . ")= " . $result);
}
function pre_php_uname_cb($args) {
	error_log("call:php_uname(" . join(', ', $args) . ")");
}
function post_php_uname_cb($args, $result, $time) {
	error_log("ret:php_uname(" . join(', ', $args) . ")= " . $result);
}
function pre_fflush_cb($args) {
	error_log("call:fflush(" . join(', ', $args) . ")");
}
function post_fflush_cb($args, $result, $time) {
	error_log("ret:fflush(" . join(', ', $args) . ")= " . $result);
}
function pre_proc_get_status_cb($args) {
	error_log("call:proc_get_status(" . join(', ', $args) . ")");
}
function post_proc_get_status_cb($args, $result, $time) {
	error_log("ret:proc_get_status(" . join(', ', $args) . ")= " . $result);
}
function pre_fwrite_cb($args) {
	error_log("call:fwrite(" . join(', ', $args) . ")");
}
function post_fwrite_cb($args, $result, $time) {
	error_log("ret:fwrite(" . join(', ', $args) . ")= " . $result);
}
function pre_pfsockopen_cb($args) {
	error_log("call:pfsockopen(" . join(', ', $args) . ")");
}
function post_pfsockopen_cb($args, $result, $time) {
	error_log("ret:pfsockopen(" . join(', ', $args) . ")= " . $result);
}
function pre_msg_receive_cb($args) {
	error_log("call:msg_receive(" . join(', ', $args) . ")");
}
function post_msg_receive_cb($args, $result, $time) {
	error_log("ret:msg_receive(" . join(', ', $args) . ")= " . $result);
}
function pre_umask_cb($args) {
	error_log("call:umask(" . join(', ', $args) . ")");
}
function post_umask_cb($args, $result, $time) {
	error_log("ret:umask(" . join(', ', $args) . ")= " . $result);
}
function pre_is_writable_cb($args) {
	error_log("call:is_writable(" . join(', ', $args) . ")");
}
function post_is_writable_cb($args, $result, $time) {
	error_log("ret:is_writable(" . join(', ', $args) . ")= " . $result);
}
function pre_fputs_cb($args) {
	error_log("call:fputs(" . join(', ', $args) . ")");
}
function post_fputs_cb($args, $result, $time) {
	error_log("ret:fputs(" . join(', ', $args) . ")= " . $result);
}
function pre_lchown_cb($args) {
	error_log("call:lchown(" . join(', ', $args) . ")");
}
function post_lchown_cb($args, $result, $time) {
	error_log("ret:lchown(" . join(', ', $args) . ")= " . $result);
}
function pre_mail_cb($args) {
	error_log("call:mail(" . join(', ', $args) . ")");
}
function post_mail_cb($args, $result, $time) {
	error_log("ret:mail(" . join(', ', $args) . ")= " . $result);
}
function pre_fstat_cb($args) {
	error_log("call:fstat(" . join(', ', $args) . ")");
}
function post_fstat_cb($args, $result, $time) {
	error_log("ret:fstat(" . join(', ', $args) . ")= " . $result);
}
function pre_dl_cb($args) {
	error_log("call:dl(" . join(', ', $args) . ")");
}
function post_dl_cb($args, $result, $time) {
	error_log("ret:dl(" . join(', ', $args) . ")= " . $result);
}
function pre_touch_cb($args) {
	error_log("call:touch(" . join(', ', $args) . ")");
}
function post_touch_cb($args, $result, $time) {
	error_log("ret:touch(" . join(', ', $args) . ")= " . $result);
}
function pre_read_cb($args) {
	error_log("call:read(" . join(', ', $args) . ")");
}
function post_read_cb($args, $result, $time) {
	error_log("ret:read(" . join(', ', $args) . ")= " . $result);
}
function pre_inet_ntop_cb($args) {
	error_log("call:inet_ntop(" . join(', ', $args) . ")");
}
function post_inet_ntop_cb($args, $result, $time) {
	error_log("ret:inet_ntop(" . join(', ', $args) . ")= " . $result);
}
function pre_header_remove_cb($args) {
	error_log("call:header_remove(" . join(', ', $args) . ")");
}
function post_header_remove_cb($args, $result, $time) {
	error_log("ret:header_remove(" . join(', ', $args) . ")= " . $result);
}
function pre_readfile_cb($args) {
	error_log("call:readfile(" . join(', ', $args) . ")");
}
function post_readfile_cb($args, $result, $time) {
	error_log("ret:readfile(" . join(', ', $args) . ")= " . $result);
}
function pre_move_uploaded_file_cb($args) {
	error_log("call:move_uploaded_file(" . join(', ', $args) . ")");
}
function post_move_uploaded_file_cb($args, $result, $time) {
	error_log("ret:move_uploaded_file(" . join(', ', $args) . ")= " . $result);
}
function pre_getmygid_cb($args) {
	error_log("call:getmygid(" . join(', ', $args) . ")");
}
function post_getmygid_cb($args, $result, $time) {
	error_log("ret:getmygid(" . join(', ', $args) . ")= " . $result);
}
function pre_proc_terminate_cb($args) {
	error_log("call:proc_terminate(" . join(', ', $args) . ")");
}
function post_proc_terminate_cb($args, $result, $time) {
	error_log("ret:proc_terminate(" . join(', ', $args) . ")= " . $result);
}
function pre_filemtime_cb($args) {
	error_log("call:filemtime(" . join(', ', $args) . ")");
}
function post_filemtime_cb($args, $result, $time) {
	error_log("ret:filemtime(" . join(', ', $args) . ")= " . $result);
}
function pre_stream_socket_recvfrom_cb($args) {
	error_log("call:stream_socket_recvfrom(" . join(', ', $args) . ")");
}
function post_stream_socket_recvfrom_cb($args, $result, $time) {
	error_log("ret:stream_socket_recvfrom(" . join(', ', $args) . ")= " . $result);
}
function pre_shell_exec_cb($args) {
	error_log("call:shell_exec(" . join(', ', $args) . ")");
}
function post_shell_exec_cb($args, $result, $time) {
	error_log("ret:shell_exec(" . join(', ', $args) . ")= " . $result);
}
function pre_fileowner_cb($args) {
	error_log("call:fileowner(" . join(', ', $args) . ")");
}
function post_fileowner_cb($args, $result, $time) {
	error_log("ret:fileowner(" . join(', ', $args) . ")= " . $result);
}
function pre_tempnam_cb($args) {
	error_log("call:tempnam(" . join(', ', $args) . ")");
}
function post_tempnam_cb($args, $result, $time) {
	error_log("ret:tempnam(" . join(', ', $args) . ")= " . $result);
}
function pre_tmpfile_cb($args) {
	error_log("call:tmpfile(" . join(', ', $args) . ")");
}
function post_tmpfile_cb($args, $result, $time) {
	error_log("ret:tmpfile(" . join(', ', $args) . ")= " . $result);
}
function pre_fgetc_cb($args) {
	error_log("call:fgetc(" . join(', ', $args) . ")");
}
function post_fgetc_cb($args, $result, $time) {
	error_log("ret:fgetc(" . join(', ', $args) . ")= " . $result);
}
function pre_fputcsv_cb($args) {
	error_log("call:fputcsv(" . join(', ', $args) . ")");
}
function post_fputcsv_cb($args, $result, $time) {
	error_log("ret:fputcsv(" . join(', ', $args) . ")= " . $result);
}
function pre_pclose_cb($args) {
	error_log("call:pclose(" . join(', ', $args) . ")");
}
function post_pclose_cb($args, $result, $time) {
	error_log("ret:pclose(" . join(', ', $args) . ")= " . $result);
}
function pre_proc_close_cb($args) {
	error_log("call:proc_close(" . join(', ', $args) . ")");
}
function post_proc_close_cb($args, $result, $time) {
	error_log("ret:proc_close(" . join(', ', $args) . ")= " . $result);
}
function pre_syslog_cb($args) {
	error_log("call:syslog(" . join(', ', $args) . ")");
}
function post_syslog_cb($args, $result, $time) {
	error_log("ret:syslog(" . join(', ', $args) . ")= " . $result);
}
function pre_is_link_cb($args) {
	error_log("call:is_link(" . join(', ', $args) . ")");
}
function post_is_link_cb($args, $result, $time) {
	error_log("ret:is_link(" . join(', ', $args) . ")= " . $result);
}
function pre_dns_get_record_cb($args) {
	error_log("call:dns_get_record(" . join(', ', $args) . ")");
}
function post_dns_get_record_cb($args, $result, $time) {
	error_log("ret:dns_get_record(" . join(', ', $args) . ")= " . $result);
}
function pre_fgets_cb($args) {
	error_log("call:fgets(" . join(', ', $args) . ")");
}
function post_fgets_cb($args, $result, $time) {
	error_log("ret:fgets(" . join(', ', $args) . ")= " . $result);
}
function pre_flock_cb($args) {
	error_log("call:flock(" . join(', ', $args) . ")");
}
function post_flock_cb($args, $result, $time) {
	error_log("ret:flock(" . join(', ', $args) . ")= " . $result);
}
function pre_dirname_cb($args) {
	error_log("call:dirname(" . join(', ', $args) . ")");
}
function post_dirname_cb($args, $result, $time) {
	error_log("ret:dirname(" . join(', ', $args) . ")= " . $result);
}
function pre_is_dir_cb($args) {
	error_log("call:is_dir(" . join(', ', $args) . ")");
}
function post_is_dir_cb($args, $result, $time) {
	error_log("ret:is_dir(" . join(', ', $args) . ")= " . $result);
}
function pre_openlog_cb($args) {
	error_log("call:openlog(" . join(', ', $args) . ")");
}
function post_openlog_cb($args, $result, $time) {
	error_log("ret:openlog(" . join(', ', $args) . ")= " . $result);
}
function pre_exec_cb($args) {
	error_log("call:exec(" . join(', ', $args) . ")");
}
function post_exec_cb($args, $result, $time) {
	error_log("ret:exec(" . join(', ', $args) . ")= " . $result);
}
function pre_ftell_cb($args) {
	error_log("call:ftell(" . join(', ', $args) . ")");
}
function post_ftell_cb($args, $result, $time) {
	error_log("ret:ftell(" . join(', ', $args) . ")= " . $result);
}
function pre_escapeshellcmd_cb($args) {
	error_log("call:escapeshellcmd(" . join(', ', $args) . ")");
}
function post_escapeshellcmd_cb($args, $result, $time) {
	error_log("ret:escapeshellcmd(" . join(', ', $args) . ")= " . $result);
}
function pre_ip2long_cb($args) {
	error_log("call:ip2long(" . join(', ', $args) . ")");
}
function post_ip2long_cb($args, $result, $time) {
	error_log("ret:ip2long(" . join(', ', $args) . ")= " . $result);
}
function pre_is_readable_cb($args) {
	error_log("call:is_readable(" . join(', ', $args) . ")");
}
function post_is_readable_cb($args, $result, $time) {
	error_log("ret:is_readable(" . join(', ', $args) . ")= " . $result);
}
function pre_gethostbyaddr_cb($args) {
	error_log("call:gethostbyaddr(" . join(', ', $args) . ")");
}
function post_gethostbyaddr_cb($args, $result, $time) {
	error_log("ret:gethostbyaddr(" . join(', ', $args) . ")= " . $result);
}
function pre_clearstatcache_cb($args) {
	error_log("call:clearstatcache(" . join(', ', $args) . ")");
}
function post_clearstatcache_cb($args, $result, $time) {
	error_log("ret:clearstatcache(" . join(', ', $args) . ")= " . $result);
}
function pre_checkdnsrr_cb($args) {
	error_log("call:checkdnsrr(" . join(', ', $args) . ")");
}
function post_checkdnsrr_cb($args, $result, $time) {
	error_log("ret:checkdnsrr(" . join(', ', $args) . ")= " . $result);
}
function pre_getcwd_cb($args) {
	error_log("call:getcwd(" . join(', ', $args) . ")");
}
function post_getcwd_cb($args, $result, $time) {
	error_log("ret:getcwd(" . join(', ', $args) . ")= " . $result);
}
function pre_fgetcsv_cb($args) {
	error_log("call:fgetcsv(" . join(', ', $args) . ")");
}
function post_fgetcsv_cb($args, $result, $time) {
	error_log("ret:fgetcsv(" . join(', ', $args) . ")= " . $result);
}
function pre_symlink_cb($args) {
	error_log("call:symlink(" . join(', ', $args) . ")");
}
function post_symlink_cb($args, $result, $time) {
	error_log("ret:symlink(" . join(', ', $args) . ")= " . $result);
}
function pre_parse_ini_file_cb($args) {
	error_log("call:parse_ini_file(" . join(', ', $args) . ")");
}
function post_parse_ini_file_cb($args, $result, $time) {
	error_log("ret:parse_ini_file(" . join(', ', $args) . ")= " . $result);
}
function pre_realpath_cache_get_cb($args) {
	error_log("call:realpath_cache_get(" . join(', ', $args) . ")");
}
function post_realpath_cache_get_cb($args, $result, $time) {
	error_log("ret:realpath_cache_get(" . join(', ', $args) . ")= " . $result);
}
function pre_is_file_cb($args) {
	error_log("call:is_file(" . join(', ', $args) . ")");
}
function post_is_file_cb($args, $result, $time) {
	error_log("ret:is_file(" . join(', ', $args) . ")= " . $result);
}
function pre_recv_cb($args) {
	error_log("call:recv(" . join(', ', $args) . ")");
}
function post_recv_cb($args, $result, $time) {
	error_log("ret:recv(" . join(', ', $args) . ")= " . $result);
}
function pre_socket_cb($args) {
	error_log("call:socket(" . join(', ', $args) . ")");
}
function post_socket_cb($args, $result, $time) {
	error_log("ret:socket(" . join(', ', $args) . ")= " . $result);
}
function pre_parse_ini_string_cb($args) {
	error_log("call:parse_ini_string(" . join(', ', $args) . ")");
}
function post_parse_ini_string_cb($args, $result, $time) {
	error_log("ret:parse_ini_string(" . join(', ', $args) . ")= " . $result);
}
function pre_diskfreespace_cb($args) {
	error_log("call:diskfreespace(" . join(', ', $args) . ")");
}
function post_diskfreespace_cb($args, $result, $time) {
	error_log("ret:diskfreespace(" . join(', ', $args) . ")= " . $result);
}
function pre_popen_cb($args) {
	error_log("call:popen(" . join(', ', $args) . ")");
}
function post_popen_cb($args, $result, $time) {
	error_log("ret:popen(" . join(', ', $args) . ")= " . $result);
}
function pre_getprotobyname_cb($args) {
	error_log("call:getprotobyname(" . join(', ', $args) . ")");
}
function post_getprotobyname_cb($args, $result, $time) {
	error_log("ret:getprotobyname(" . join(', ', $args) . ")= " . $result);
}
function pre_gethostbynamel_cb($args) {
	error_log("call:gethostbynamel(" . join(', ', $args) . ")");
}
function post_gethostbynamel_cb($args, $result, $time) {
	error_log("ret:gethostbynamel(" . join(', ', $args) . ")= " . $result);
}
function pre_closelog_cb($args) {
	error_log("call:closelog(" . join(', ', $args) . ")");
}
function post_closelog_cb($args, $result, $time) {
	error_log("ret:closelog(" . join(', ', $args) . ")= " . $result);
}
function pre_lstat_cb($args) {
	error_log("call:lstat(" . join(', ', $args) . ")");
}
function post_lstat_cb($args, $result, $time) {
	error_log("ret:lstat(" . join(', ', $args) . ")= " . $result);
}
function pre_getservbyname_cb($args) {
	error_log("call:getservbyname(" . join(', ', $args) . ")");
}
function post_getservbyname_cb($args, $result, $time) {
	error_log("ret:getservbyname(" . join(', ', $args) . ")= " . $result);
}
function pre_rename_cb($args) {
	error_log("call:rename(" . join(', ', $args) . ")");
}
function post_rename_cb($args, $result, $time) {
	error_log("ret:rename(" . join(', ', $args) . ")= " . $result);
}
function pre_socket_get_status_cb($args) {
	error_log("call:socket_get_status(" . join(', ', $args) . ")");
}
function post_socket_get_status_cb($args, $result, $time) {
	error_log("ret:socket_get_status(" . join(', ', $args) . ")= " . $result);
}
function pre_headers_sent_cb($args) {
	error_log("call:headers_sent(" . join(', ', $args) . ")");
}
function post_headers_sent_cb($args, $result, $time) {
	error_log("ret:headers_sent(" . join(', ', $args) . ")= " . $result);
}
function pre_setrawcookie_cb($args) {
	error_log("call:setrawcookie(" . join(', ', $args) . ")");
}
function post_setrawcookie_cb($args, $result, $time) {
	error_log("ret:setrawcookie(" . join(', ', $args) . ")= " . $result);
}
function pre_ini_get_cb($args) {
	error_log("call:ini_get(" . join(', ', $args) . ")");
}
function post_ini_get_cb($args, $result, $time) {
	error_log("ret:ini_get(" . join(', ', $args) . ")= " . $result);
}
function pre_filetype_cb($args) {
	error_log("call:filetype(" . join(', ', $args) . ")");
}
function post_filetype_cb($args, $result, $time) {
	error_log("ret:filetype(" . join(', ', $args) . ")= " . $result);
}
function pre_chmod_cb($args) {
	error_log("call:chmod(" . join(', ', $args) . ")");
}
function post_chmod_cb($args, $result, $time) {
	error_log("ret:chmod(" . join(', ', $args) . ")= " . $result);
}
function pre_echo_cb($args) {
	error_log("call:echo(" . join(', ', $args) . ")");
}
function post_echo_cb($args, $result, $time) {
	error_log("ret:echo(" . join(', ', $args) . ")= " . $result);
}
function pre_long2ip_cb($args) {
	error_log("call:long2ip(" . join(', ', $args) . ")");
}
function post_long2ip_cb($args, $result, $time) {
	error_log("ret:long2ip(" . join(', ', $args) . ")= " . $result);
}
function pre_header_cb($args) {
	error_log("call:header(" . join(', ', $args) . ")");
}
function post_header_cb($args, $result, $time) {
	error_log("ret:header(" . join(', ', $args) . ")= " . $result);
}
function pre_is_executable_cb($args) {
	error_log("call:is_executable(" . join(', ', $args) . ")");
}
function post_is_executable_cb($args, $result, $time) {
	error_log("ret:is_executable(" . join(', ', $args) . ")= " . $result);
}
function pre_dns_check_record_cb($args) {
	error_log("call:dns_check_record(" . join(', ', $args) . ")");
}
function post_dns_check_record_cb($args, $result, $time) {
	error_log("ret:dns_check_record(" . join(', ', $args) . ")= " . $result);
}
function pre_send_cb($args) {
	error_log("call:send(" . join(', ', $args) . ")");
}
function post_send_cb($args, $result, $time) {
	error_log("ret:send(" . join(', ', $args) . ")= " . $result);
}
function pre_get_current_user_cb($args) {
	error_log("call:get_current_user(" . join(', ', $args) . ")");
}
function post_get_current_user_cb($args, $result, $time) {
	error_log("ret:get_current_user(" . join(', ', $args) . ")= " . $result);
}
function pre_fopen_cb($args) {
	error_log("call:fopen(" . join(', ', $args) . ")");
}
function post_fopen_cb($args, $result, $time) {
	error_log("ret:fopen(" . join(', ', $args) . ")= " . $result);
}
function pre_open_cb($args) {
	error_log("call:open(" . join(', ', $args) . ")");
}
function post_open_cb($args, $result, $time) {
	error_log("ret:open(" . join(', ', $args) . ")= " . $result);
}
function pre_proc_nice_cb($args) {
	error_log("call:proc_nice(" . join(', ', $args) . ")");
}
function post_proc_nice_cb($args, $result, $time) {
	error_log("ret:proc_nice(" . join(', ', $args) . ")= " . $result);
}
function pre_unlink_cb($args) {
	error_log("call:unlink(" . join(', ', $args) . ")");
}
function post_unlink_cb($args, $result, $time) {
	error_log("ret:unlink(" . join(', ', $args) . ")= " . $result);
}
function pre_gethostname_cb($args) {
	error_log("call:gethostname(" . join(', ', $args) . ")");
}
function post_gethostname_cb($args, $result, $time) {
	error_log("ret:gethostname(" . join(', ', $args) . ")= " . $result);
}
function pre_getmxrr_cb($args) {
	error_log("call:getmxrr(" . join(', ', $args) . ")");
}
function post_getmxrr_cb($args, $result, $time) {
	error_log("ret:getmxrr(" . join(', ', $args) . ")= " . $result);
}
function pre_mkdir_cb($args) {
	error_log("call:mkdir(" . join(', ', $args) . ")");
}
function post_mkdir_cb($args, $result, $time) {
	error_log("ret:mkdir(" . join(', ', $args) . ")= " . $result);
}
function pre_system_cb($args) {
	error_log("call:system(" . join(', ', $args) . ")");
}
function post_system_cb($args, $result, $time) {
	error_log("ret:system(" . join(', ', $args) . ")= " . $result);
}
function pre_getservbyport_cb($args) {
	error_log("call:getservbyport(" . join(', ', $args) . ")");
}
function post_getservbyport_cb($args, $result, $time) {
	error_log("ret:getservbyport(" . join(', ', $args) . ")= " . $result);
}
function pre_filesize_cb($args) {
	error_log("call:filesize(" . join(', ', $args) . ")");
}
function post_filesize_cb($args, $result, $time) {
	error_log("ret:filesize(" . join(', ', $args) . ")= " . $result);
}
function pre_linkinfo_cb($args) {
	error_log("call:linkinfo(" . join(', ', $args) . ")");
}
function post_linkinfo_cb($args, $result, $time) {
	error_log("ret:linkinfo(" . join(', ', $args) . ")= " . $result);
}
function pre_set_file_buffer_cb($args) {
	error_log("call:set_file_buffer(" . join(', ', $args) . ")");
}
function post_set_file_buffer_cb($args, $result, $time) {
	error_log("ret:set_file_buffer(" . join(', ', $args) . ")= " . $result);
}
function pre_rmdir_cb($args) {
	error_log("call:rmdir(" . join(', ', $args) . ")");
}
function post_rmdir_cb($args, $result, $time) {
	error_log("ret:rmdir(" . join(', ', $args) . ")= " . $result);
}
function pre_socket_set_timeout_cb($args) {
	error_log("call:socket_set_timeout(" . join(', ', $args) . ")");
}
function post_socket_set_timeout_cb($args, $result, $time) {
	error_log("ret:socket_set_timeout(" . join(', ', $args) . ")= " . $result);
}
function pre_dns_get_mx_cb($args) {
	error_log("call:dns_get_mx(" . join(', ', $args) . ")");
}
function post_dns_get_mx_cb($args, $result, $time) {
	error_log("ret:dns_get_mx(" . join(', ', $args) . ")= " . $result);
}
function pre_getenv_cb($args) {
	error_log("call:getenv(" . join(', ', $args) . ")");
}
function post_getenv_cb($args, $result, $time) {
	error_log("ret:getenv(" . join(', ', $args) . ")= " . $result);
}
function pre_lchgrp_cb($args) {
	error_log("call:lchgrp(" . join(', ', $args) . ")");
}
function post_lchgrp_cb($args, $result, $time) {
	error_log("ret:lchgrp(" . join(', ', $args) . ")= " . $result);
}
function pre_link_cb($args) {
	error_log("call:link(" . join(', ', $args) . ")");
}
function post_link_cb($args, $result, $time) {
	error_log("ret:link(" . join(', ', $args) . ")= " . $result);
}
function pre_ssh2_scp_recv_cb($args) {
	error_log("call:ssh2_scp_recv(" . join(', ', $args) . ")");
}
function post_ssh2_scp_recv_cb($args, $result, $time) {
	error_log("ret:ssh2_scp_recv(" . join(', ', $args) . ")= " . $result);
}
function pre_copy_cb($args) {
	error_log("call:copy(" . join(', ', $args) . ")");
}
function post_copy_cb($args, $result, $time) {
	error_log("ret:copy(" . join(', ', $args) . ")= " . $result);
}
function pre_fgetss_cb($args) {
	error_log("call:fgetss(" . join(', ', $args) . ")");
}
function post_fgetss_cb($args, $result, $time) {
	error_log("ret:fgetss(" . join(', ', $args) . ")= " . $result);
}
function pre_fscanf_cb($args) {
	error_log("call:fscanf(" . join(', ', $args) . ")");
}
function post_fscanf_cb($args, $result, $time) {
	error_log("ret:fscanf(" . join(', ', $args) . ")= " . $result);
}
function pre_headers_list_cb($args) {
	error_log("call:headers_list(" . join(', ', $args) . ")");
}
function post_headers_list_cb($args, $result, $time) {
	error_log("ret:headers_list(" . join(', ', $args) . ")= " . $result);
}
function pre_proc_open_cb($args) {
	error_log("call:proc_open(" . join(', ', $args) . ")");
}
function post_proc_open_cb($args, $result, $time) {
	error_log("ret:proc_open(" . join(', ', $args) . ")= " . $result);
}
function pre_enabled_cb($args) {
	error_log("call:enabled(" . join(', ', $args) . ")");
}
function post_enabled_cb($args, $result, $time) {
	error_log("ret:enabled(" . join(', ', $args) . ")= " . $result);
}
function pre_file_exists_cb($args) {
	error_log("call:file_exists(" . join(', ', $args) . ")");
}
function post_file_exists_cb($args, $result, $time) {
	error_log("ret:file_exists(" . join(', ', $args) . ")= " . $result);
}
function pre_fnmatch_cb($args) {
	error_log("call:fnmatch(" . join(', ', $args) . ")");
}
function post_fnmatch_cb($args, $result, $time) {
	error_log("ret:fnmatch(" . join(', ', $args) . ")= " . $result);
}
function pre_ftruncate_cb($args) {
	error_log("call:ftruncate(" . join(', ', $args) . ")");
}
function post_ftruncate_cb($args, $result, $time) {
	error_log("ret:ftruncate(" . join(', ', $args) . ")= " . $result);
}
function pre_getprotobynumber_cb($args) {
	error_log("call:getprotobynumber(" . join(', ', $args) . ")");
}
function post_getprotobynumber_cb($args, $result, $time) {
	error_log("ret:getprotobynumber(" . join(', ', $args) . ")= " . $result);
}
function pre_delete_cb($args) {
	error_log("call:delete(" . join(', ', $args) . ")");
}
function post_delete_cb($args, $result, $time) {
	error_log("ret:delete(" . join(', ', $args) . ")= " . $result);
}
function pre_file_put_contents_cb($args) {
	error_log("call:file_put_contents(" . join(', ', $args) . ")");
}
function post_file_put_contents_cb($args, $result, $time) {
	error_log("ret:file_put_contents(" . join(', ', $args) . ")= " . $result);
}
function pre_socket_set_blocking_cb($args) {
	error_log("call:socket_set_blocking(" . join(', ', $args) . ")");
}
function post_socket_set_blocking_cb($args, $result, $time) {
	error_log("ret:socket_set_blocking(" . join(', ', $args) . ")= " . $result);
}
function pre_disk_free_space_cb($args) {
	error_log("call:disk_free_space(" . join(', ', $args) . ")");
}
function post_disk_free_space_cb($args, $result, $time) {
	error_log("ret:disk_free_space(" . join(', ', $args) . ")= " . $result);
}
function pre_realpath_cache_size_cb($args) {
	error_log("call:realpath_cache_size(" . join(', ', $args) . ")");
}
function post_realpath_cache_size_cb($args, $result, $time) {
	error_log("ret:realpath_cache_size(" . join(', ', $args) . ")= " . $result);
}
function pre_fread_cb($args) {
	error_log("call:fread(" . join(', ', $args) . ")");
}
function post_fread_cb($args, $result, $time) {
	error_log("ret:fread(" . join(', ', $args) . ")= " . $result);
}
function pre_fileperms_cb($args) {
	error_log("call:fileperms(" . join(', ', $args) . ")");
}
function post_fileperms_cb($args, $result, $time) {
	error_log("ret:fileperms(" . join(', ', $args) . ")= " . $result);
}
function pre_inet_pton_cb($args) {
	error_log("call:inet_pton(" . join(', ', $args) . ")");
}
function post_inet_pton_cb($args, $result, $time) {
	error_log("ret:inet_pton(" . join(', ', $args) . ")= " . $result);
}
function pre_file_cb($args) {
	error_log("call:file(" . join(', ', $args) . ")");
}
function post_file_cb($args, $result, $time) {
	error_log("ret:file(" . join(', ', $args) . ")= " . $result);
}
function pre_feof_cb($args) {
	error_log("call:feof(" . join(', ', $args) . ")");
}
function post_feof_cb($args, $result, $time) {
	error_log("ret:feof(" . join(', ', $args) . ")= " . $result);
}
function pre_is_writeable_cb($args) {
	error_log("call:is_writeable(" . join(', ', $args) . ")");
}
function post_is_writeable_cb($args, $result, $time) {
	error_log("ret:is_writeable(" . join(', ', $args) . ")= " . $result);
}
function pre_fpassthru_cb($args) {
	error_log("call:fpassthru(" . join(', ', $args) . ")");
}
function post_fpassthru_cb($args, $result, $time) {
	error_log("ret:fpassthru(" . join(', ', $args) . ")= " . $result);
}
function pre_socket_recv_cb($args) {
	error_log("call:socket_recv(" . join(', ', $args) . ")");
}
function post_socket_recv_cb($args, $result, $time) {
	error_log("ret:socket_recv(" . join(', ', $args) . ")= " . $result);
}
function pre_filegroup_cb($args) {
	error_log("call:filegroup(" . join(', ', $args) . ")");
}
function post_filegroup_cb($args, $result, $time) {
	error_log("ret:filegroup(" . join(', ', $args) . ")= " . $result);
}
function pre_fseek_cb($args) {
	error_log("call:fseek(" . join(', ', $args) . ")");
}
function post_fseek_cb($args, $result, $time) {
	error_log("ret:fseek(" . join(', ', $args) . ")= " . $result);
}
function pre_sendmail_cb($args) {
	error_log("call:sendmail(" . join(', ', $args) . ")");
}
function post_sendmail_cb($args, $result, $time) {
	error_log("ret:sendmail(" . join(', ', $args) . ")= " . $result);
}
function pre_chgrp_cb($args) {
	error_log("call:chgrp(" . join(', ', $args) . ")");
}
function post_chgrp_cb($args, $result, $time) {
	error_log("ret:chgrp(" . join(', ', $args) . ")= " . $result);
}
function pre_write_cb($args) {
	error_log("call:write(" . join(', ', $args) . ")");
}
function post_write_cb($args, $result, $time) {
	error_log("ret:write(" . join(', ', $args) . ")= " . $result);
}
function pre_filectime_cb($args) {
	error_log("call:filectime(" . join(', ', $args) . ")");
}
function post_filectime_cb($args, $result, $time) {
	error_log("ret:filectime(" . join(', ', $args) . ")= " . $result);
}
function pre_rewind_cb($args) {
	error_log("call:rewind(" . join(', ', $args) . ")");
}
function post_rewind_cb($args, $result, $time) {
	error_log("ret:rewind(" . join(', ', $args) . ")= " . $result);
}
function pre_fileinode_cb($args) {
	error_log("call:fileinode(" . join(', ', $args) . ")");
}
function post_fileinode_cb($args, $result, $time) {
	error_log("ret:fileinode(" . join(', ', $args) . ")= " . $result);
}
function pre_is_uploaded_file_cb($args) {
	error_log("call:is_uploaded_file(" . join(', ', $args) . ")");
}
function post_is_uploaded_file_cb($args, $result, $time) {
	error_log("ret:is_uploaded_file(" . join(', ', $args) . ")= " . $result);
}
function pre_realpath_cb($args) {
	error_log("call:realpath(" . join(', ', $args) . ")");
}
function post_realpath_cb($args, $result, $time) {
	error_log("ret:realpath(" . join(', ', $args) . ")= " . $result);
}
function pre_stat_cb($args) {
	error_log("call:stat(" . join(', ', $args) . ")");
}
function post_stat_cb($args, $result, $time) {
	error_log("ret:stat(" . join(', ', $args) . ")= " . $result);
}
function pre_disk_total_space_cb($args) {
	error_log("call:disk_total_space(" . join(', ', $args) . ")");
}
function post_disk_total_space_cb($args, $result, $time) {
	error_log("ret:disk_total_space(" . join(', ', $args) . ")= " . $result);
}
function pre_glob_cb($args) {
	error_log("call:glob(" . join(', ', $args) . ")");
}
function post_glob_cb($args, $result, $time) {
	error_log("ret:glob(" . join(', ', $args) . ")= " . $result);
}
function pre_gethostbyname_cb($args) {
	error_log("call:gethostbyname(" . join(', ', $args) . ")");
}
function post_gethostbyname_cb($args, $result, $time) {
	error_log("ret:gethostbyname(" . join(', ', $args) . ")= " . $result);
}
function pre_define_syslog_variables_cb($args) {
	error_log("call:define_syslog_variables(" . join(', ', $args) . ")");
}
function post_define_syslog_variables_cb($args, $result, $time) {
	error_log("ret:define_syslog_variables(" . join(', ', $args) . ")= " . $result);
}
function pre_readlink_cb($args) {
	error_log("call:readlink(" . join(', ', $args) . ")");
}
function post_readlink_cb($args, $result, $time) {
	error_log("ret:readlink(" . join(', ', $args) . ")= " . $result);
}
function pre_eval_cb($args) {
	error_log("call:eval(" . join(', ', $args) . ")");
}
function post_eval_cb($args, $result, $time) {
	error_log("ret:eval(" . join(', ', $args) . ")= " . $result);
}
function pre_escapeshellarg_cb($args) {
	error_log("call:escapeshellarg(" . join(', ', $args) . ")");
}
function post_escapeshellarg_cb($args, $result, $time) {
	error_log("ret:escapeshellarg(" . join(', ', $args) . ")= " . $result);
}
function pre_setcookie_cb($args) {
	error_log("call:setcookie(" . join(', ', $args) . ")");
}
function post_setcookie_cb($args, $result, $time) {
	error_log("ret:setcookie(" . join(', ', $args) . ")= " . $result);
}
function pre_fsockopen_cb($args) {
	error_log("call:fsockopen(" . join(', ', $args) . ")");
}
function post_fsockopen_cb($args, $result, $time) {
	error_log("ret:fsockopen(" . join(', ', $args) . ")= " . $result);
}
function pre_passthru_cb($args) {
	error_log("call:passthru(" . join(', ', $args) . ")");
}
function post_passthru_cb($args, $result, $time) {
	error_log("ret:passthru(" . join(', ', $args) . ")= " . $result);
}
function pre_getmyuid_cb($args) {
	error_log("call:getmyuid(" . join(', ', $args) . ")");
}
function post_getmyuid_cb($args, $result, $time) {
	error_log("ret:getmyuid(" . join(', ', $args) . ")= " . $result);
}
function pre_fileatime_cb($args) {
	error_log("call:fileatime(" . join(', ', $args) . ")");
}
function post_fileatime_cb($args, $result, $time) {
	error_log("ret:fileatime(" . join(', ', $args) . ")= " . $result);
}
function pre_chown_cb($args) {
	error_log("call:chown(" . join(', ', $args) . ")");
}
function post_chown_cb($args, $result, $time) {
	error_log("ret:chown(" . join(', ', $args) . ")= " . $result);
}
function pre_pathinfo_cb($args) {
	error_log("call:pathinfo(" . join(', ', $args) . ")");
}
function post_pathinfo_cb($args, $result, $time) {
	error_log("ret:pathinfo(" . join(', ', $args) . ")= " . $result);
}
function pre_file_get_contents_cb($args) {
	error_log("call:file_get_contents(" . join(', ', $args) . ")");
}
function post_file_get_contents_cb($args, $result, $time) {
	error_log("ret:file_get_contents(" . join(', ', $args) . ")= " . $result);
}


fc_add_pre('socket_recvfrom', 'pre_socket_recvfrom_cb');
fc_add_post('socket_recvfrom', 'post_socket_recvfrom_cb');
fc_add_pre('basename', 'pre_basename_cb');
fc_add_post('basename', 'post_basename_cb');
fc_add_pre('fclose', 'pre_fclose_cb');
fc_add_post('fclose', 'post_fclose_cb');
fc_add_pre('php_uname', 'pre_php_uname_cb');
fc_add_post('php_uname', 'post_php_uname_cb');
fc_add_pre('fflush', 'pre_fflush_cb');
fc_add_post('fflush', 'post_fflush_cb');
fc_add_pre('proc_get_status', 'pre_proc_get_status_cb');
fc_add_post('proc_get_status', 'post_proc_get_status_cb');
fc_add_pre('fwrite', 'pre_fwrite_cb');
fc_add_post('fwrite', 'post_fwrite_cb');
fc_add_pre('pfsockopen', 'pre_pfsockopen_cb');
fc_add_post('pfsockopen', 'post_pfsockopen_cb');
fc_add_pre('msg_receive', 'pre_msg_receive_cb');
fc_add_post('msg_receive', 'post_msg_receive_cb');
fc_add_pre('umask', 'pre_umask_cb');
fc_add_post('umask', 'post_umask_cb');
fc_add_pre('is_writable', 'pre_is_writable_cb');
fc_add_post('is_writable', 'post_is_writable_cb');
fc_add_pre('fputs', 'pre_fputs_cb');
fc_add_post('fputs', 'post_fputs_cb');
fc_add_pre('lchown', 'pre_lchown_cb');
fc_add_post('lchown', 'post_lchown_cb');
fc_add_pre('mail', 'pre_mail_cb');
fc_add_post('mail', 'post_mail_cb');
fc_add_pre('fstat', 'pre_fstat_cb');
fc_add_post('fstat', 'post_fstat_cb');
fc_add_pre('dl', 'pre_dl_cb');
fc_add_post('dl', 'post_dl_cb');
fc_add_pre('touch', 'pre_touch_cb');
fc_add_post('touch', 'post_touch_cb');
fc_add_pre('read', 'pre_read_cb');
fc_add_post('read', 'post_read_cb');
fc_add_pre('inet_ntop', 'pre_inet_ntop_cb');
fc_add_post('inet_ntop', 'post_inet_ntop_cb');
fc_add_pre('header_remove', 'pre_header_remove_cb');
fc_add_post('header_remove', 'post_header_remove_cb');
fc_add_pre('readfile', 'pre_readfile_cb');
fc_add_post('readfile', 'post_readfile_cb');
fc_add_pre('move_uploaded_file', 'pre_move_uploaded_file_cb');
fc_add_post('move_uploaded_file', 'post_move_uploaded_file_cb');
fc_add_pre('getmygid', 'pre_getmygid_cb');
fc_add_post('getmygid', 'post_getmygid_cb');
fc_add_pre('proc_terminate', 'pre_proc_terminate_cb');
fc_add_post('proc_terminate', 'post_proc_terminate_cb');
fc_add_pre('filemtime', 'pre_filemtime_cb');
fc_add_post('filemtime', 'post_filemtime_cb');
fc_add_pre('stream_socket_recvfrom', 'pre_stream_socket_recvfrom_cb');
fc_add_post('stream_socket_recvfrom', 'post_stream_socket_recvfrom_cb');
fc_add_pre('shell_exec', 'pre_shell_exec_cb');
fc_add_post('shell_exec', 'post_shell_exec_cb');
fc_add_pre('fileowner', 'pre_fileowner_cb');
fc_add_post('fileowner', 'post_fileowner_cb');
fc_add_pre('tempnam', 'pre_tempnam_cb');
fc_add_post('tempnam', 'post_tempnam_cb');
fc_add_pre('tmpfile', 'pre_tmpfile_cb');
fc_add_post('tmpfile', 'post_tmpfile_cb');
fc_add_pre('fgetc', 'pre_fgetc_cb');
fc_add_post('fgetc', 'post_fgetc_cb');
fc_add_pre('fputcsv', 'pre_fputcsv_cb');
fc_add_post('fputcsv', 'post_fputcsv_cb');
fc_add_pre('pclose', 'pre_pclose_cb');
fc_add_post('pclose', 'post_pclose_cb');
fc_add_pre('proc_close', 'pre_proc_close_cb');
fc_add_post('proc_close', 'post_proc_close_cb');
fc_add_pre('syslog', 'pre_syslog_cb');
fc_add_post('syslog', 'post_syslog_cb');
fc_add_pre('is_link', 'pre_is_link_cb');
fc_add_post('is_link', 'post_is_link_cb');
fc_add_pre('dns_get_record', 'pre_dns_get_record_cb');
fc_add_post('dns_get_record', 'post_dns_get_record_cb');
fc_add_pre('fgets', 'pre_fgets_cb');
fc_add_post('fgets', 'post_fgets_cb');
fc_add_pre('flock', 'pre_flock_cb');
fc_add_post('flock', 'post_flock_cb');
fc_add_pre('dirname', 'pre_dirname_cb');
fc_add_post('dirname', 'post_dirname_cb');
fc_add_pre('is_dir', 'pre_is_dir_cb');
fc_add_post('is_dir', 'post_is_dir_cb');
fc_add_pre('openlog', 'pre_openlog_cb');
fc_add_post('openlog', 'post_openlog_cb');
fc_add_pre('exec', 'pre_exec_cb');
fc_add_post('exec', 'post_exec_cb');
fc_add_pre('ftell', 'pre_ftell_cb');
fc_add_post('ftell', 'post_ftell_cb');
fc_add_pre('escapeshellcmd', 'pre_escapeshellcmd_cb');
fc_add_post('escapeshellcmd', 'post_escapeshellcmd_cb');
fc_add_pre('ip2long', 'pre_ip2long_cb');
fc_add_post('ip2long', 'post_ip2long_cb');
fc_add_pre('is_readable', 'pre_is_readable_cb');
fc_add_post('is_readable', 'post_is_readable_cb');
fc_add_pre('gethostbyaddr', 'pre_gethostbyaddr_cb');
fc_add_post('gethostbyaddr', 'post_gethostbyaddr_cb');
fc_add_pre('clearstatcache', 'pre_clearstatcache_cb');
fc_add_post('clearstatcache', 'post_clearstatcache_cb');
fc_add_pre('checkdnsrr', 'pre_checkdnsrr_cb');
fc_add_post('checkdnsrr', 'post_checkdnsrr_cb');
fc_add_pre('getcwd', 'pre_getcwd_cb');
fc_add_post('getcwd', 'post_getcwd_cb');
fc_add_pre('fgetcsv', 'pre_fgetcsv_cb');
fc_add_post('fgetcsv', 'post_fgetcsv_cb');
fc_add_pre('symlink', 'pre_symlink_cb');
fc_add_post('symlink', 'post_symlink_cb');
fc_add_pre('parse_ini_file', 'pre_parse_ini_file_cb');
fc_add_post('parse_ini_file', 'post_parse_ini_file_cb');
fc_add_pre('realpath_cache_get', 'pre_realpath_cache_get_cb');
fc_add_post('realpath_cache_get', 'post_realpath_cache_get_cb');
fc_add_pre('is_file', 'pre_is_file_cb');
fc_add_post('is_file', 'post_is_file_cb');
fc_add_pre('recv', 'pre_recv_cb');
fc_add_post('recv', 'post_recv_cb');
fc_add_pre('socket', 'pre_socket_cb');
fc_add_post('socket', 'post_socket_cb');
fc_add_pre('parse_ini_string', 'pre_parse_ini_string_cb');
fc_add_post('parse_ini_string', 'post_parse_ini_string_cb');
fc_add_pre('diskfreespace', 'pre_diskfreespace_cb');
fc_add_post('diskfreespace', 'post_diskfreespace_cb');
fc_add_pre('popen', 'pre_popen_cb');
fc_add_post('popen', 'post_popen_cb');
fc_add_pre('getprotobyname', 'pre_getprotobyname_cb');
fc_add_post('getprotobyname', 'post_getprotobyname_cb');
fc_add_pre('gethostbynamel', 'pre_gethostbynamel_cb');
fc_add_post('gethostbynamel', 'post_gethostbynamel_cb');
fc_add_pre('closelog', 'pre_closelog_cb');
fc_add_post('closelog', 'post_closelog_cb');
fc_add_pre('lstat', 'pre_lstat_cb');
fc_add_post('lstat', 'post_lstat_cb');
fc_add_pre('getservbyname', 'pre_getservbyname_cb');
fc_add_post('getservbyname', 'post_getservbyname_cb');
fc_add_pre('rename', 'pre_rename_cb');
fc_add_post('rename', 'post_rename_cb');
fc_add_pre('socket_get_status', 'pre_socket_get_status_cb');
fc_add_post('socket_get_status', 'post_socket_get_status_cb');
fc_add_pre('headers_sent', 'pre_headers_sent_cb');
fc_add_post('headers_sent', 'post_headers_sent_cb');
fc_add_pre('setrawcookie', 'pre_setrawcookie_cb');
fc_add_post('setrawcookie', 'post_setrawcookie_cb');
fc_add_pre('ini_get', 'pre_ini_get_cb');
fc_add_post('ini_get', 'post_ini_get_cb');
fc_add_pre('filetype', 'pre_filetype_cb');
fc_add_post('filetype', 'post_filetype_cb');
fc_add_pre('chmod', 'pre_chmod_cb');
fc_add_post('chmod', 'post_chmod_cb');
fc_add_pre('echo', 'pre_echo_cb');
fc_add_post('echo', 'post_echo_cb');
fc_add_pre('long2ip', 'pre_long2ip_cb');
fc_add_post('long2ip', 'post_long2ip_cb');
fc_add_pre('header', 'pre_header_cb');
fc_add_post('header', 'post_header_cb');
fc_add_pre('is_executable', 'pre_is_executable_cb');
fc_add_post('is_executable', 'post_is_executable_cb');
fc_add_pre('dns_check_record', 'pre_dns_check_record_cb');
fc_add_post('dns_check_record', 'post_dns_check_record_cb');
fc_add_pre('send', 'pre_send_cb');
fc_add_post('send', 'post_send_cb');
fc_add_pre('get_current_user', 'pre_get_current_user_cb');
fc_add_post('get_current_user', 'post_get_current_user_cb');
fc_add_pre('fopen', 'pre_fopen_cb');
fc_add_post('fopen', 'post_fopen_cb');
fc_add_pre('open', 'pre_open_cb');
fc_add_post('open', 'post_open_cb');
fc_add_pre('proc_nice', 'pre_proc_nice_cb');
fc_add_post('proc_nice', 'post_proc_nice_cb');
fc_add_pre('unlink', 'pre_unlink_cb');
fc_add_post('unlink', 'post_unlink_cb');
fc_add_pre('gethostname', 'pre_gethostname_cb');
fc_add_post('gethostname', 'post_gethostname_cb');
fc_add_pre('getmxrr', 'pre_getmxrr_cb');
fc_add_post('getmxrr', 'post_getmxrr_cb');
fc_add_pre('mkdir', 'pre_mkdir_cb');
fc_add_post('mkdir', 'post_mkdir_cb');
fc_add_pre('system', 'pre_system_cb');
fc_add_post('system', 'post_system_cb');
fc_add_pre('getservbyport', 'pre_getservbyport_cb');
fc_add_post('getservbyport', 'post_getservbyport_cb');
fc_add_pre('filesize', 'pre_filesize_cb');
fc_add_post('filesize', 'post_filesize_cb');
fc_add_pre('linkinfo', 'pre_linkinfo_cb');
fc_add_post('linkinfo', 'post_linkinfo_cb');
fc_add_pre('set_file_buffer', 'pre_set_file_buffer_cb');
fc_add_post('set_file_buffer', 'post_set_file_buffer_cb');
fc_add_pre('rmdir', 'pre_rmdir_cb');
fc_add_post('rmdir', 'post_rmdir_cb');
fc_add_pre('socket_set_timeout', 'pre_socket_set_timeout_cb');
fc_add_post('socket_set_timeout', 'post_socket_set_timeout_cb');
fc_add_pre('dns_get_mx', 'pre_dns_get_mx_cb');
fc_add_post('dns_get_mx', 'post_dns_get_mx_cb');
fc_add_pre('getenv', 'pre_getenv_cb');
fc_add_post('getenv', 'post_getenv_cb');
fc_add_pre('lchgrp', 'pre_lchgrp_cb');
fc_add_post('lchgrp', 'post_lchgrp_cb');
fc_add_pre('link', 'pre_link_cb');
fc_add_post('link', 'post_link_cb');
fc_add_pre('ssh2_scp_recv', 'pre_ssh2_scp_recv_cb');
fc_add_post('ssh2_scp_recv', 'post_ssh2_scp_recv_cb');
fc_add_pre('copy', 'pre_copy_cb');
fc_add_post('copy', 'post_copy_cb');
fc_add_pre('fgetss', 'pre_fgetss_cb');
fc_add_post('fgetss', 'post_fgetss_cb');
fc_add_pre('fscanf', 'pre_fscanf_cb');
fc_add_post('fscanf', 'post_fscanf_cb');
fc_add_pre('headers_list', 'pre_headers_list_cb');
fc_add_post('headers_list', 'post_headers_list_cb');
fc_add_pre('proc_open', 'pre_proc_open_cb');
fc_add_post('proc_open', 'post_proc_open_cb');
fc_add_pre('enabled', 'pre_enabled_cb');
fc_add_post('enabled', 'post_enabled_cb');
fc_add_pre('file_exists', 'pre_file_exists_cb');
fc_add_post('file_exists', 'post_file_exists_cb');
fc_add_pre('fnmatch', 'pre_fnmatch_cb');
fc_add_post('fnmatch', 'post_fnmatch_cb');
fc_add_pre('ftruncate', 'pre_ftruncate_cb');
fc_add_post('ftruncate', 'post_ftruncate_cb');
fc_add_pre('getprotobynumber', 'pre_getprotobynumber_cb');
fc_add_post('getprotobynumber', 'post_getprotobynumber_cb');
fc_add_pre('delete', 'pre_delete_cb');
fc_add_post('delete', 'post_delete_cb');
fc_add_pre('file_put_contents', 'pre_file_put_contents_cb');
fc_add_post('file_put_contents', 'post_file_put_contents_cb');
fc_add_pre('socket_set_blocking', 'pre_socket_set_blocking_cb');
fc_add_post('socket_set_blocking', 'post_socket_set_blocking_cb');
fc_add_pre('disk_free_space', 'pre_disk_free_space_cb');
fc_add_post('disk_free_space', 'post_disk_free_space_cb');
fc_add_pre('realpath_cache_size', 'pre_realpath_cache_size_cb');
fc_add_post('realpath_cache_size', 'post_realpath_cache_size_cb');
fc_add_pre('fread', 'pre_fread_cb');
fc_add_post('fread', 'post_fread_cb');
fc_add_pre('fileperms', 'pre_fileperms_cb');
fc_add_post('fileperms', 'post_fileperms_cb');
fc_add_pre('inet_pton', 'pre_inet_pton_cb');
fc_add_post('inet_pton', 'post_inet_pton_cb');
fc_add_pre('file', 'pre_file_cb');
fc_add_post('file', 'post_file_cb');
fc_add_pre('feof', 'pre_feof_cb');
fc_add_post('feof', 'post_feof_cb');
fc_add_pre('is_writeable', 'pre_is_writeable_cb');
fc_add_post('is_writeable', 'post_is_writeable_cb');
fc_add_pre('fpassthru', 'pre_fpassthru_cb');
fc_add_post('fpassthru', 'post_fpassthru_cb');
fc_add_pre('socket_recv', 'pre_socket_recv_cb');
fc_add_post('socket_recv', 'post_socket_recv_cb');
fc_add_pre('filegroup', 'pre_filegroup_cb');
fc_add_post('filegroup', 'post_filegroup_cb');
fc_add_pre('fseek', 'pre_fseek_cb');
fc_add_post('fseek', 'post_fseek_cb');
fc_add_pre('sendmail', 'pre_sendmail_cb');
fc_add_post('sendmail', 'post_sendmail_cb');
fc_add_pre('chgrp', 'pre_chgrp_cb');
fc_add_post('chgrp', 'post_chgrp_cb');
fc_add_pre('write', 'pre_write_cb');
fc_add_post('write', 'post_write_cb');
fc_add_pre('filectime', 'pre_filectime_cb');
fc_add_post('filectime', 'post_filectime_cb');
fc_add_pre('rewind', 'pre_rewind_cb');
fc_add_post('rewind', 'post_rewind_cb');
fc_add_pre('fileinode', 'pre_fileinode_cb');
fc_add_post('fileinode', 'post_fileinode_cb');
fc_add_pre('is_uploaded_file', 'pre_is_uploaded_file_cb');
fc_add_post('is_uploaded_file', 'post_is_uploaded_file_cb');
fc_add_pre('realpath', 'pre_realpath_cb');
fc_add_post('realpath', 'post_realpath_cb');
fc_add_pre('stat', 'pre_stat_cb');
fc_add_post('stat', 'post_stat_cb');
fc_add_pre('disk_total_space', 'pre_disk_total_space_cb');
fc_add_post('disk_total_space', 'post_disk_total_space_cb');
fc_add_pre('glob', 'pre_glob_cb');
fc_add_post('glob', 'post_glob_cb');
fc_add_pre('gethostbyname', 'pre_gethostbyname_cb');
fc_add_post('gethostbyname', 'post_gethostbyname_cb');
fc_add_pre('define_syslog_variables', 'pre_define_syslog_variables_cb');
fc_add_post('define_syslog_variables', 'post_define_syslog_variables_cb');
fc_add_pre('readlink', 'pre_readlink_cb');
fc_add_post('readlink', 'post_readlink_cb');
fc_add_pre('eval', 'pre_eval_cb');
fc_add_post('eval', 'post_eval_cb');
fc_add_pre('escapeshellarg', 'pre_escapeshellarg_cb');
fc_add_post('escapeshellarg', 'post_escapeshellarg_cb');
fc_add_pre('setcookie', 'pre_setcookie_cb');
fc_add_post('setcookie', 'post_setcookie_cb');
fc_add_pre('fsockopen', 'pre_fsockopen_cb');
fc_add_post('fsockopen', 'post_fsockopen_cb');
fc_add_pre('passthru', 'pre_passthru_cb');
fc_add_post('passthru', 'post_passthru_cb');
fc_add_pre('getmyuid', 'pre_getmyuid_cb');
fc_add_post('getmyuid', 'post_getmyuid_cb');
fc_add_pre('fileatime', 'pre_fileatime_cb');
fc_add_post('fileatime', 'post_fileatime_cb');
fc_add_pre('chown', 'pre_chown_cb');
fc_add_post('chown', 'post_chown_cb');
fc_add_pre('pathinfo', 'pre_pathinfo_cb');
fc_add_post('pathinfo', 'post_pathinfo_cb');
fc_add_pre('file_get_contents', 'pre_file_get_contents_cb');
fc_add_post('file_get_contents', 'post_file_get_contents_cb');


include $argv[1];
 ?>
