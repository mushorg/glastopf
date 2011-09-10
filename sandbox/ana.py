def parse_fn(line):
    fn, args = line.split('(', 1)
    fn = fn.replace('call:', '').replace('ret:', '')
    args = [ x.strip().replace(')', '') for x in args.split(',') ]
    return fn, args

def parse_ret(line):
    call, res = line.split(')=', 1)
    fn, args = parse_fn(call)
    res = res.strip()
    return fn, args, res

def ana(lines):
    for line in lines:
        if len(line) < 2:
            continue
        elif line.startswith('call:socket_recvfrom'):
            proc, args = parse_fn(line)
            new_socket_recvfrom_call = (' '.join(args), 'socket_recvfrom_call', args[0])
            print new_socket_recvfrom_call
        elif line.startswith('ret:socket_recvfrom'):
            proc, args, result = parse_ret(line)
            new_socket_recvfrom_ret = (' '.join(args), 'socket_recvfrom_return', result)
            print new_socket_recvfrom_ret
    
        elif line.startswith('call:basename'):
            proc, args = parse_fn(line)
            new_basename_call = (' '.join(args), 'basename_call', args[0])
            print new_basename_call
        elif line.startswith('ret:basename'):
            proc, args, result = parse_ret(line)
            new_basename_ret = (' '.join(args), 'basename_return', result)
            print new_basename_ret
    
        elif line.startswith('call:fclose'):
            proc, args = parse_fn(line)
            new_fclose_call = (' '.join(args), 'fclose_call', args[0])
            print new_fclose_call
        elif line.startswith('ret:fclose'):
            proc, args, result = parse_ret(line)
            new_fclose_ret = (' '.join(args), 'fclose_return', result)
            print new_fclose_ret
    
        elif line.startswith('call:php_uname'):
            proc, args = parse_fn(line)
            new_php_uname_call = (' '.join(args), 'php_uname_call', args[0])
            print new_php_uname_call
        elif line.startswith('ret:php_uname'):
            proc, args, result = parse_ret(line)
            new_php_uname_ret = (' '.join(args), 'php_uname_return', result)
            print new_php_uname_ret
    
        elif line.startswith('call:fflush'):
            proc, args = parse_fn(line)
            new_fflush_call = (' '.join(args), 'fflush_call', args[0])
            print new_fflush_call
        elif line.startswith('ret:fflush'):
            proc, args, result = parse_ret(line)
            new_fflush_ret = (' '.join(args), 'fflush_return', result)
            print new_fflush_ret
    
        elif line.startswith('call:proc_get_status'):
            proc, args = parse_fn(line)
            new_proc_get_status_call = (' '.join(args), 'proc_get_status_call', args[0])
            print new_proc_get_status_call
        elif line.startswith('ret:proc_get_status'):
            proc, args, result = parse_ret(line)
            new_proc_get_status_ret = (' '.join(args), 'proc_get_status_return', result)
            print new_proc_get_status_ret
    
        elif line.startswith('call:fwrite'):
            proc, args = parse_fn(line)
            new_fwrite_call = (' '.join(args), 'fwrite_call', args[0])
            print new_fwrite_call
        elif line.startswith('ret:fwrite'):
            proc, args, result = parse_ret(line)
            new_fwrite_ret = (' '.join(args), 'fwrite_return', result)
            print new_fwrite_ret
    
        elif line.startswith('call:pfsockopen'):
            proc, args = parse_fn(line)
            new_pfsockopen_call = (' '.join(args), 'pfsockopen_call', args[0])
            print new_pfsockopen_call
        elif line.startswith('ret:pfsockopen'):
            proc, args, result = parse_ret(line)
            new_pfsockopen_ret = (' '.join(args), 'pfsockopen_return', result)
            print new_pfsockopen_ret
    
        elif line.startswith('call:msg_receive'):
            proc, args = parse_fn(line)
            new_msg_receive_call = (' '.join(args), 'msg_receive_call', args[0])
            print new_msg_receive_call
        elif line.startswith('ret:msg_receive'):
            proc, args, result = parse_ret(line)
            new_msg_receive_ret = (' '.join(args), 'msg_receive_return', result)
            print new_msg_receive_ret
    
        elif line.startswith('call:umask'):
            proc, args = parse_fn(line)
            new_umask_call = (' '.join(args), 'umask_call', args[0])
            print new_umask_call
        elif line.startswith('ret:umask'):
            proc, args, result = parse_ret(line)
            new_umask_ret = (' '.join(args), 'umask_return', result)
            print new_umask_ret
    
        elif line.startswith('call:is_writable'):
            proc, args = parse_fn(line)
            new_is_writable_call = (' '.join(args), 'is_writable_call', args[0])
            print new_is_writable_call
        elif line.startswith('ret:is_writable'):
            proc, args, result = parse_ret(line)
            new_is_writable_ret = (' '.join(args), 'is_writable_return', result)
            print new_is_writable_ret
    
        elif line.startswith('call:fputs'):
            proc, args = parse_fn(line)
            new_fputs_call = (' '.join(args), 'fputs_call', args[0])
            print new_fputs_call
        elif line.startswith('ret:fputs'):
            proc, args, result = parse_ret(line)
            new_fputs_ret = (' '.join(args), 'fputs_return', result)
            print new_fputs_ret
    
        elif line.startswith('call:lchown'):
            proc, args = parse_fn(line)
            new_lchown_call = (' '.join(args), 'lchown_call', args[0])
            print new_lchown_call
        elif line.startswith('ret:lchown'):
            proc, args, result = parse_ret(line)
            new_lchown_ret = (' '.join(args), 'lchown_return', result)
            print new_lchown_ret
    
        elif line.startswith('call:mail'):
            proc, args = parse_fn(line)
            new_mail_call = (' '.join(args), 'mail_call', args[0])
            print new_mail_call
        elif line.startswith('ret:mail'):
            proc, args, result = parse_ret(line)
            new_mail_ret = (' '.join(args), 'mail_return', result)
            print new_mail_ret
    
        elif line.startswith('call:fstat'):
            proc, args = parse_fn(line)
            new_fstat_call = (' '.join(args), 'fstat_call', args[0])
            print new_fstat_call
        elif line.startswith('ret:fstat'):
            proc, args, result = parse_ret(line)
            new_fstat_ret = (' '.join(args), 'fstat_return', result)
            print new_fstat_ret
    
        elif line.startswith('call:dl'):
            proc, args = parse_fn(line)
            new_dl_call = (' '.join(args), 'dl_call', args[0])
            print new_dl_call
        elif line.startswith('ret:dl'):
            proc, args, result = parse_ret(line)
            new_dl_ret = (' '.join(args), 'dl_return', result)
            print new_dl_ret
    
        elif line.startswith('call:touch'):
            proc, args = parse_fn(line)
            new_touch_call = (' '.join(args), 'touch_call', args[0])
            print new_touch_call
        elif line.startswith('ret:touch'):
            proc, args, result = parse_ret(line)
            new_touch_ret = (' '.join(args), 'touch_return', result)
            print new_touch_ret
    
        elif line.startswith('call:read'):
            proc, args = parse_fn(line)
            new_read_call = (' '.join(args), 'read_call', args[0])
            print new_read_call
        elif line.startswith('ret:read'):
            proc, args, result = parse_ret(line)
            new_read_ret = (' '.join(args), 'read_return', result)
            print new_read_ret
    
        elif line.startswith('call:inet_ntop'):
            proc, args = parse_fn(line)
            new_inet_ntop_call = (' '.join(args), 'inet_ntop_call', args[0])
            print new_inet_ntop_call
        elif line.startswith('ret:inet_ntop'):
            proc, args, result = parse_ret(line)
            new_inet_ntop_ret = (' '.join(args), 'inet_ntop_return', result)
            print new_inet_ntop_ret
    
        elif line.startswith('call:header_remove'):
            proc, args = parse_fn(line)
            new_header_remove_call = (' '.join(args), 'header_remove_call', args[0])
            print new_header_remove_call
        elif line.startswith('ret:header_remove'):
            proc, args, result = parse_ret(line)
            new_header_remove_ret = (' '.join(args), 'header_remove_return', result)
            print new_header_remove_ret
    
        elif line.startswith('call:readfile'):
            proc, args = parse_fn(line)
            new_readfile_call = (' '.join(args), 'readfile_call', args[0])
            print new_readfile_call
        elif line.startswith('ret:readfile'):
            proc, args, result = parse_ret(line)
            new_readfile_ret = (' '.join(args), 'readfile_return', result)
            print new_readfile_ret
    
        elif line.startswith('call:move_uploaded_file'):
            proc, args = parse_fn(line)
            new_move_uploaded_file_call = (' '.join(args), 'move_uploaded_file_call', args[0])
            print new_move_uploaded_file_call
        elif line.startswith('ret:move_uploaded_file'):
            proc, args, result = parse_ret(line)
            new_move_uploaded_file_ret = (' '.join(args), 'move_uploaded_file_return', result)
            print new_move_uploaded_file_ret
    
        elif line.startswith('call:getmygid'):
            proc, args = parse_fn(line)
            new_getmygid_call = (' '.join(args), 'getmygid_call', args[0])
            print new_getmygid_call
        elif line.startswith('ret:getmygid'):
            proc, args, result = parse_ret(line)
            new_getmygid_ret = (' '.join(args), 'getmygid_return', result)
            print new_getmygid_ret
    
        elif line.startswith('call:proc_terminate'):
            proc, args = parse_fn(line)
            new_proc_terminate_call = (' '.join(args), 'proc_terminate_call', args[0])
            print new_proc_terminate_call
        elif line.startswith('ret:proc_terminate'):
            proc, args, result = parse_ret(line)
            new_proc_terminate_ret = (' '.join(args), 'proc_terminate_return', result)
            print new_proc_terminate_ret
    
        elif line.startswith('call:filemtime'):
            proc, args = parse_fn(line)
            new_filemtime_call = (' '.join(args), 'filemtime_call', args[0])
            print new_filemtime_call
        elif line.startswith('ret:filemtime'):
            proc, args, result = parse_ret(line)
            new_filemtime_ret = (' '.join(args), 'filemtime_return', result)
            print new_filemtime_ret
    
        elif line.startswith('call:stream_socket_recvfrom'):
            proc, args = parse_fn(line)
            new_stream_socket_recvfrom_call = (' '.join(args), 'stream_socket_recvfrom_call', args[0])
            print new_stream_socket_recvfrom_call
        elif line.startswith('ret:stream_socket_recvfrom'):
            proc, args, result = parse_ret(line)
            new_stream_socket_recvfrom_ret = (' '.join(args), 'stream_socket_recvfrom_return', result)
            print new_stream_socket_recvfrom_ret
    
        elif line.startswith('call:shell_exec'):
            proc, args = parse_fn(line)
            new_shell_exec_call = (' '.join(args), 'shell_exec_call', args[0])
            print new_shell_exec_call
        elif line.startswith('ret:shell_exec'):
            proc, args, result = parse_ret(line)
            new_shell_exec_ret = (' '.join(args), 'shell_exec_return', result)
            print new_shell_exec_ret
    
        elif line.startswith('call:fileowner'):
            proc, args = parse_fn(line)
            new_fileowner_call = (' '.join(args), 'fileowner_call', args[0])
            print new_fileowner_call
        elif line.startswith('ret:fileowner'):
            proc, args, result = parse_ret(line)
            new_fileowner_ret = (' '.join(args), 'fileowner_return', result)
            print new_fileowner_ret
    
        elif line.startswith('call:tempnam'):
            proc, args = parse_fn(line)
            new_tempnam_call = (' '.join(args), 'tempnam_call', args[0])
            print new_tempnam_call
        elif line.startswith('ret:tempnam'):
            proc, args, result = parse_ret(line)
            new_tempnam_ret = (' '.join(args), 'tempnam_return', result)
            print new_tempnam_ret
    
        elif line.startswith('call:tmpfile'):
            proc, args = parse_fn(line)
            new_tmpfile_call = (' '.join(args), 'tmpfile_call', args[0])
            print new_tmpfile_call
        elif line.startswith('ret:tmpfile'):
            proc, args, result = parse_ret(line)
            new_tmpfile_ret = (' '.join(args), 'tmpfile_return', result)
            print new_tmpfile_ret
    
        elif line.startswith('call:fgetc'):
            proc, args = parse_fn(line)
            new_fgetc_call = (' '.join(args), 'fgetc_call', args[0])
            print new_fgetc_call
        elif line.startswith('ret:fgetc'):
            proc, args, result = parse_ret(line)
            new_fgetc_ret = (' '.join(args), 'fgetc_return', result)
            print new_fgetc_ret
    
        elif line.startswith('call:fputcsv'):
            proc, args = parse_fn(line)
            new_fputcsv_call = (' '.join(args), 'fputcsv_call', args[0])
            print new_fputcsv_call
        elif line.startswith('ret:fputcsv'):
            proc, args, result = parse_ret(line)
            new_fputcsv_ret = (' '.join(args), 'fputcsv_return', result)
            print new_fputcsv_ret
    
        elif line.startswith('call:pclose'):
            proc, args = parse_fn(line)
            new_pclose_call = (' '.join(args), 'pclose_call', args[0])
            print new_pclose_call
        elif line.startswith('ret:pclose'):
            proc, args, result = parse_ret(line)
            new_pclose_ret = (' '.join(args), 'pclose_return', result)
            print new_pclose_ret
    
        elif line.startswith('call:proc_close'):
            proc, args = parse_fn(line)
            new_proc_close_call = (' '.join(args), 'proc_close_call', args[0])
            print new_proc_close_call
        elif line.startswith('ret:proc_close'):
            proc, args, result = parse_ret(line)
            new_proc_close_ret = (' '.join(args), 'proc_close_return', result)
            print new_proc_close_ret
    
        elif line.startswith('call:syslog'):
            proc, args = parse_fn(line)
            new_syslog_call = (' '.join(args), 'syslog_call', args[0])
            print new_syslog_call
        elif line.startswith('ret:syslog'):
            proc, args, result = parse_ret(line)
            new_syslog_ret = (' '.join(args), 'syslog_return', result)
            print new_syslog_ret
    
        elif line.startswith('call:is_link'):
            proc, args = parse_fn(line)
            new_is_link_call = (' '.join(args), 'is_link_call', args[0])
            print new_is_link_call
        elif line.startswith('ret:is_link'):
            proc, args, result = parse_ret(line)
            new_is_link_ret = (' '.join(args), 'is_link_return', result)
            print new_is_link_ret
    
        elif line.startswith('call:dns_get_record'):
            proc, args = parse_fn(line)
            new_dns_get_record_call = (' '.join(args), 'dns_get_record_call', args[0])
            print new_dns_get_record_call
        elif line.startswith('ret:dns_get_record'):
            proc, args, result = parse_ret(line)
            new_dns_get_record_ret = (' '.join(args), 'dns_get_record_return', result)
            print new_dns_get_record_ret
    
        elif line.startswith('call:fgets'):
            proc, args = parse_fn(line)
            new_fgets_call = (' '.join(args), 'fgets_call', args[0])
            print new_fgets_call
        elif line.startswith('ret:fgets'):
            proc, args, result = parse_ret(line)
            new_fgets_ret = (' '.join(args), 'fgets_return', result)
            print new_fgets_ret
    
        elif line.startswith('call:flock'):
            proc, args = parse_fn(line)
            new_flock_call = (' '.join(args), 'flock_call', args[0])
            print new_flock_call
        elif line.startswith('ret:flock'):
            proc, args, result = parse_ret(line)
            new_flock_ret = (' '.join(args), 'flock_return', result)
            print new_flock_ret
    
        elif line.startswith('call:dirname'):
            proc, args = parse_fn(line)
            new_dirname_call = (' '.join(args), 'dirname_call', args[0])
            print new_dirname_call
        elif line.startswith('ret:dirname'):
            proc, args, result = parse_ret(line)
            new_dirname_ret = (' '.join(args), 'dirname_return', result)
            print new_dirname_ret
    
        elif line.startswith('call:is_dir'):
            proc, args = parse_fn(line)
            new_is_dir_call = (' '.join(args), 'is_dir_call', args[0])
            print new_is_dir_call
        elif line.startswith('ret:is_dir'):
            proc, args, result = parse_ret(line)
            new_is_dir_ret = (' '.join(args), 'is_dir_return', result)
            print new_is_dir_ret
    
        elif line.startswith('call:openlog'):
            proc, args = parse_fn(line)
            new_openlog_call = (' '.join(args), 'openlog_call', args[0])
            print new_openlog_call
        elif line.startswith('ret:openlog'):
            proc, args, result = parse_ret(line)
            new_openlog_ret = (' '.join(args), 'openlog_return', result)
            print new_openlog_ret
    
        elif line.startswith('call:exec'):
            proc, args = parse_fn(line)
            new_exec_call = (' '.join(args), 'exec_call', args[0])
            print new_exec_call
        elif line.startswith('ret:exec'):
            proc, args, result = parse_ret(line)
            new_exec_ret = (' '.join(args), 'exec_return', result)
            print new_exec_ret
    
        elif line.startswith('call:ftell'):
            proc, args = parse_fn(line)
            new_ftell_call = (' '.join(args), 'ftell_call', args[0])
            print new_ftell_call
        elif line.startswith('ret:ftell'):
            proc, args, result = parse_ret(line)
            new_ftell_ret = (' '.join(args), 'ftell_return', result)
            print new_ftell_ret
    
        elif line.startswith('call:escapeshellcmd'):
            proc, args = parse_fn(line)
            new_escapeshellcmd_call = (' '.join(args), 'escapeshellcmd_call', args[0])
            print new_escapeshellcmd_call
        elif line.startswith('ret:escapeshellcmd'):
            proc, args, result = parse_ret(line)
            new_escapeshellcmd_ret = (' '.join(args), 'escapeshellcmd_return', result)
            print new_escapeshellcmd_ret
    
        elif line.startswith('call:ip2long'):
            proc, args = parse_fn(line)
            new_ip2long_call = (' '.join(args), 'ip2long_call', args[0])
            print new_ip2long_call
        elif line.startswith('ret:ip2long'):
            proc, args, result = parse_ret(line)
            new_ip2long_ret = (' '.join(args), 'ip2long_return', result)
            print new_ip2long_ret
    
        elif line.startswith('call:is_readable'):
            proc, args = parse_fn(line)
            new_is_readable_call = (' '.join(args), 'is_readable_call', args[0])
            print new_is_readable_call
        elif line.startswith('ret:is_readable'):
            proc, args, result = parse_ret(line)
            new_is_readable_ret = (' '.join(args), 'is_readable_return', result)
            print new_is_readable_ret
    
        elif line.startswith('call:gethostbyaddr'):
            proc, args = parse_fn(line)
            new_gethostbyaddr_call = (' '.join(args), 'gethostbyaddr_call', args[0])
            print new_gethostbyaddr_call
        elif line.startswith('ret:gethostbyaddr'):
            proc, args, result = parse_ret(line)
            new_gethostbyaddr_ret = (' '.join(args), 'gethostbyaddr_return', result)
            print new_gethostbyaddr_ret
    
        elif line.startswith('call:clearstatcache'):
            proc, args = parse_fn(line)
            new_clearstatcache_call = (' '.join(args), 'clearstatcache_call', args[0])
            print new_clearstatcache_call
        elif line.startswith('ret:clearstatcache'):
            proc, args, result = parse_ret(line)
            new_clearstatcache_ret = (' '.join(args), 'clearstatcache_return', result)
            print new_clearstatcache_ret
    
        elif line.startswith('call:checkdnsrr'):
            proc, args = parse_fn(line)
            new_checkdnsrr_call = (' '.join(args), 'checkdnsrr_call', args[0])
            print new_checkdnsrr_call
        elif line.startswith('ret:checkdnsrr'):
            proc, args, result = parse_ret(line)
            new_checkdnsrr_ret = (' '.join(args), 'checkdnsrr_return', result)
            print new_checkdnsrr_ret
    
        elif line.startswith('call:getcwd'):
            proc, args = parse_fn(line)
            new_getcwd_call = (' '.join(args), 'getcwd_call', args[0])
            print new_getcwd_call
        elif line.startswith('ret:getcwd'):
            proc, args, result = parse_ret(line)
            new_getcwd_ret = (' '.join(args), 'getcwd_return', result)
            print new_getcwd_ret
    
        elif line.startswith('call:fgetcsv'):
            proc, args = parse_fn(line)
            new_fgetcsv_call = (' '.join(args), 'fgetcsv_call', args[0])
            print new_fgetcsv_call
        elif line.startswith('ret:fgetcsv'):
            proc, args, result = parse_ret(line)
            new_fgetcsv_ret = (' '.join(args), 'fgetcsv_return', result)
            print new_fgetcsv_ret
    
        elif line.startswith('call:symlink'):
            proc, args = parse_fn(line)
            new_symlink_call = (' '.join(args), 'symlink_call', args[0])
            print new_symlink_call
        elif line.startswith('ret:symlink'):
            proc, args, result = parse_ret(line)
            new_symlink_ret = (' '.join(args), 'symlink_return', result)
            print new_symlink_ret
    
        elif line.startswith('call:parse_ini_file'):
            proc, args = parse_fn(line)
            new_parse_ini_file_call = (' '.join(args), 'parse_ini_file_call', args[0])
            print new_parse_ini_file_call
        elif line.startswith('ret:parse_ini_file'):
            proc, args, result = parse_ret(line)
            new_parse_ini_file_ret = (' '.join(args), 'parse_ini_file_return', result)
            print new_parse_ini_file_ret
    
        elif line.startswith('call:realpath_cache_get'):
            proc, args = parse_fn(line)
            new_realpath_cache_get_call = (' '.join(args), 'realpath_cache_get_call', args[0])
            print new_realpath_cache_get_call
        elif line.startswith('ret:realpath_cache_get'):
            proc, args, result = parse_ret(line)
            new_realpath_cache_get_ret = (' '.join(args), 'realpath_cache_get_return', result)
            print new_realpath_cache_get_ret
    
        elif line.startswith('call:is_file'):
            proc, args = parse_fn(line)
            new_is_file_call = (' '.join(args), 'is_file_call', args[0])
            print new_is_file_call
        elif line.startswith('ret:is_file'):
            proc, args, result = parse_ret(line)
            new_is_file_ret = (' '.join(args), 'is_file_return', result)
            print new_is_file_ret
    
        elif line.startswith('call:recv'):
            proc, args = parse_fn(line)
            new_recv_call = (' '.join(args), 'recv_call', args[0])
            print new_recv_call
        elif line.startswith('ret:recv'):
            proc, args, result = parse_ret(line)
            new_recv_ret = (' '.join(args), 'recv_return', result)
            print new_recv_ret
    
        elif line.startswith('call:socket'):
            proc, args = parse_fn(line)
            new_socket_call = (' '.join(args), 'socket_call', args[0])
            print new_socket_call
        elif line.startswith('ret:socket'):
            proc, args, result = parse_ret(line)
            new_socket_ret = (' '.join(args), 'socket_return', result)
            print new_socket_ret
    
        elif line.startswith('call:parse_ini_string'):
            proc, args = parse_fn(line)
            new_parse_ini_string_call = (' '.join(args), 'parse_ini_string_call', args[0])
            print new_parse_ini_string_call
        elif line.startswith('ret:parse_ini_string'):
            proc, args, result = parse_ret(line)
            new_parse_ini_string_ret = (' '.join(args), 'parse_ini_string_return', result)
            print new_parse_ini_string_ret
    
        elif line.startswith('call:diskfreespace'):
            proc, args = parse_fn(line)
            new_diskfreespace_call = (' '.join(args), 'diskfreespace_call', args[0])
            print new_diskfreespace_call
        elif line.startswith('ret:diskfreespace'):
            proc, args, result = parse_ret(line)
            new_diskfreespace_ret = (' '.join(args), 'diskfreespace_return', result)
            print new_diskfreespace_ret
    
        elif line.startswith('call:popen'):
            proc, args = parse_fn(line)
            new_popen_call = (' '.join(args), 'popen_call', args[0])
            print new_popen_call
        elif line.startswith('ret:popen'):
            proc, args, result = parse_ret(line)
            new_popen_ret = (' '.join(args), 'popen_return', result)
            print new_popen_ret
    
        elif line.startswith('call:getprotobyname'):
            proc, args = parse_fn(line)
            new_getprotobyname_call = (' '.join(args), 'getprotobyname_call', args[0])
            print new_getprotobyname_call
        elif line.startswith('ret:getprotobyname'):
            proc, args, result = parse_ret(line)
            new_getprotobyname_ret = (' '.join(args), 'getprotobyname_return', result)
            print new_getprotobyname_ret
    
        elif line.startswith('call:gethostbynamel'):
            proc, args = parse_fn(line)
            new_gethostbynamel_call = (' '.join(args), 'gethostbynamel_call', args[0])
            print new_gethostbynamel_call
        elif line.startswith('ret:gethostbynamel'):
            proc, args, result = parse_ret(line)
            new_gethostbynamel_ret = (' '.join(args), 'gethostbynamel_return', result)
            print new_gethostbynamel_ret
    
        elif line.startswith('call:closelog'):
            proc, args = parse_fn(line)
            new_closelog_call = (' '.join(args), 'closelog_call', args[0])
            print new_closelog_call
        elif line.startswith('ret:closelog'):
            proc, args, result = parse_ret(line)
            new_closelog_ret = (' '.join(args), 'closelog_return', result)
            print new_closelog_ret
    
        elif line.startswith('call:lstat'):
            proc, args = parse_fn(line)
            new_lstat_call = (' '.join(args), 'lstat_call', args[0])
            print new_lstat_call
        elif line.startswith('ret:lstat'):
            proc, args, result = parse_ret(line)
            new_lstat_ret = (' '.join(args), 'lstat_return', result)
            print new_lstat_ret
    
        elif line.startswith('call:getservbyname'):
            proc, args = parse_fn(line)
            new_getservbyname_call = (' '.join(args), 'getservbyname_call', args[0])
            print new_getservbyname_call
        elif line.startswith('ret:getservbyname'):
            proc, args, result = parse_ret(line)
            new_getservbyname_ret = (' '.join(args), 'getservbyname_return', result)
            print new_getservbyname_ret
    
        elif line.startswith('call:rename'):
            proc, args = parse_fn(line)
            new_rename_call = (' '.join(args), 'rename_call', args[0])
            print new_rename_call
        elif line.startswith('ret:rename'):
            proc, args, result = parse_ret(line)
            new_rename_ret = (' '.join(args), 'rename_return', result)
            print new_rename_ret
    
        elif line.startswith('call:socket_get_status'):
            proc, args = parse_fn(line)
            new_socket_get_status_call = (' '.join(args), 'socket_get_status_call', args[0])
            print new_socket_get_status_call
        elif line.startswith('ret:socket_get_status'):
            proc, args, result = parse_ret(line)
            new_socket_get_status_ret = (' '.join(args), 'socket_get_status_return', result)
            print new_socket_get_status_ret
    
        elif line.startswith('call:headers_sent'):
            proc, args = parse_fn(line)
            new_headers_sent_call = (' '.join(args), 'headers_sent_call', args[0])
            print new_headers_sent_call
        elif line.startswith('ret:headers_sent'):
            proc, args, result = parse_ret(line)
            new_headers_sent_ret = (' '.join(args), 'headers_sent_return', result)
            print new_headers_sent_ret
    
        elif line.startswith('call:setrawcookie'):
            proc, args = parse_fn(line)
            new_setrawcookie_call = (' '.join(args), 'setrawcookie_call', args[0])
            print new_setrawcookie_call
        elif line.startswith('ret:setrawcookie'):
            proc, args, result = parse_ret(line)
            new_setrawcookie_ret = (' '.join(args), 'setrawcookie_return', result)
            print new_setrawcookie_ret
    
        elif line.startswith('call:ini_get'):
            proc, args = parse_fn(line)
            new_ini_get_call = (' '.join(args), 'ini_get_call', args[0])
            print new_ini_get_call
        elif line.startswith('ret:ini_get'):
            proc, args, result = parse_ret(line)
            new_ini_get_ret = (' '.join(args), 'ini_get_return', result)
            print new_ini_get_ret
    
        elif line.startswith('call:filetype'):
            proc, args = parse_fn(line)
            new_filetype_call = (' '.join(args), 'filetype_call', args[0])
            print new_filetype_call
        elif line.startswith('ret:filetype'):
            proc, args, result = parse_ret(line)
            new_filetype_ret = (' '.join(args), 'filetype_return', result)
            print new_filetype_ret
    
        elif line.startswith('call:chmod'):
            proc, args = parse_fn(line)
            new_chmod_call = (' '.join(args), 'chmod_call', args[0])
            print new_chmod_call
        elif line.startswith('ret:chmod'):
            proc, args, result = parse_ret(line)
            new_chmod_ret = (' '.join(args), 'chmod_return', result)
            print new_chmod_ret
    
        elif line.startswith('call:echo'):
            proc, args = parse_fn(line)
            new_echo_call = (' '.join(args), 'echo_call', args[0])
            print new_echo_call
        elif line.startswith('ret:echo'):
            proc, args, result = parse_ret(line)
            new_echo_ret = (' '.join(args), 'echo_return', result)
            print new_echo_ret
    
        elif line.startswith('call:long2ip'):
            proc, args = parse_fn(line)
            new_long2ip_call = (' '.join(args), 'long2ip_call', args[0])
            print new_long2ip_call
        elif line.startswith('ret:long2ip'):
            proc, args, result = parse_ret(line)
            new_long2ip_ret = (' '.join(args), 'long2ip_return', result)
            print new_long2ip_ret
    
        elif line.startswith('call:header'):
            proc, args = parse_fn(line)
            new_header_call = (' '.join(args), 'header_call', args[0])
            print new_header_call
        elif line.startswith('ret:header'):
            proc, args, result = parse_ret(line)
            new_header_ret = (' '.join(args), 'header_return', result)
            print new_header_ret
    
        elif line.startswith('call:is_executable'):
            proc, args = parse_fn(line)
            new_is_executable_call = (' '.join(args), 'is_executable_call', args[0])
            print new_is_executable_call
        elif line.startswith('ret:is_executable'):
            proc, args, result = parse_ret(line)
            new_is_executable_ret = (' '.join(args), 'is_executable_return', result)
            print new_is_executable_ret
    
        elif line.startswith('call:dns_check_record'):
            proc, args = parse_fn(line)
            new_dns_check_record_call = (' '.join(args), 'dns_check_record_call', args[0])
            print new_dns_check_record_call
        elif line.startswith('ret:dns_check_record'):
            proc, args, result = parse_ret(line)
            new_dns_check_record_ret = (' '.join(args), 'dns_check_record_return', result)
            print new_dns_check_record_ret
    
        elif line.startswith('call:send'):
            proc, args = parse_fn(line)
            new_send_call = (' '.join(args), 'send_call', args[0])
            print new_send_call
        elif line.startswith('ret:send'):
            proc, args, result = parse_ret(line)
            new_send_ret = (' '.join(args), 'send_return', result)
            print new_send_ret
    
        elif line.startswith('call:get_current_user'):
            proc, args = parse_fn(line)
            new_get_current_user_call = (' '.join(args), 'get_current_user_call', args[0])
            print new_get_current_user_call
        elif line.startswith('ret:get_current_user'):
            proc, args, result = parse_ret(line)
            new_get_current_user_ret = (' '.join(args), 'get_current_user_return', result)
            print new_get_current_user_ret
    
        elif line.startswith('call:fopen'):
            proc, args = parse_fn(line)
            new_fopen_call = (' '.join(args), 'fopen_call', args[0])
            print new_fopen_call
        elif line.startswith('ret:fopen'):
            proc, args, result = parse_ret(line)
            new_fopen_ret = (' '.join(args), 'fopen_return', result)
            print new_fopen_ret
    
        elif line.startswith('call:open'):
            proc, args = parse_fn(line)
            new_open_call = (' '.join(args), 'open_call', args[0])
            print new_open_call
        elif line.startswith('ret:open'):
            proc, args, result = parse_ret(line)
            new_open_ret = (' '.join(args), 'open_return', result)
            print new_open_ret
    
        elif line.startswith('call:proc_nice'):
            proc, args = parse_fn(line)
            new_proc_nice_call = (' '.join(args), 'proc_nice_call', args[0])
            print new_proc_nice_call
        elif line.startswith('ret:proc_nice'):
            proc, args, result = parse_ret(line)
            new_proc_nice_ret = (' '.join(args), 'proc_nice_return', result)
            print new_proc_nice_ret
    
        elif line.startswith('call:unlink'):
            proc, args = parse_fn(line)
            new_unlink_call = (' '.join(args), 'unlink_call', args[0])
            print new_unlink_call
        elif line.startswith('ret:unlink'):
            proc, args, result = parse_ret(line)
            new_unlink_ret = (' '.join(args), 'unlink_return', result)
            print new_unlink_ret
    
        elif line.startswith('call:gethostname'):
            proc, args = parse_fn(line)
            new_gethostname_call = (' '.join(args), 'gethostname_call', args[0])
            print new_gethostname_call
        elif line.startswith('ret:gethostname'):
            proc, args, result = parse_ret(line)
            new_gethostname_ret = (' '.join(args), 'gethostname_return', result)
            print new_gethostname_ret
    
        elif line.startswith('call:getmxrr'):
            proc, args = parse_fn(line)
            new_getmxrr_call = (' '.join(args), 'getmxrr_call', args[0])
            print new_getmxrr_call
        elif line.startswith('ret:getmxrr'):
            proc, args, result = parse_ret(line)
            new_getmxrr_ret = (' '.join(args), 'getmxrr_return', result)
            print new_getmxrr_ret
    
        elif line.startswith('call:mkdir'):
            proc, args = parse_fn(line)
            new_mkdir_call = (' '.join(args), 'mkdir_call', args[0])
            print new_mkdir_call
        elif line.startswith('ret:mkdir'):
            proc, args, result = parse_ret(line)
            new_mkdir_ret = (' '.join(args), 'mkdir_return', result)
            print new_mkdir_ret
    
        elif line.startswith('call:system'):
            proc, args = parse_fn(line)
            new_system_call = (' '.join(args), 'system_call', args[0])
            print new_system_call
        elif line.startswith('ret:system'):
            proc, args, result = parse_ret(line)
            new_system_ret = (' '.join(args), 'system_return', result)
            print new_system_ret
    
        elif line.startswith('call:getservbyport'):
            proc, args = parse_fn(line)
            new_getservbyport_call = (' '.join(args), 'getservbyport_call', args[0])
            print new_getservbyport_call
        elif line.startswith('ret:getservbyport'):
            proc, args, result = parse_ret(line)
            new_getservbyport_ret = (' '.join(args), 'getservbyport_return', result)
            print new_getservbyport_ret
    
        elif line.startswith('call:filesize'):
            proc, args = parse_fn(line)
            new_filesize_call = (' '.join(args), 'filesize_call', args[0])
            print new_filesize_call
        elif line.startswith('ret:filesize'):
            proc, args, result = parse_ret(line)
            new_filesize_ret = (' '.join(args), 'filesize_return', result)
            print new_filesize_ret
    
        elif line.startswith('call:linkinfo'):
            proc, args = parse_fn(line)
            new_linkinfo_call = (' '.join(args), 'linkinfo_call', args[0])
            print new_linkinfo_call
        elif line.startswith('ret:linkinfo'):
            proc, args, result = parse_ret(line)
            new_linkinfo_ret = (' '.join(args), 'linkinfo_return', result)
            print new_linkinfo_ret
    
        elif line.startswith('call:set_file_buffer'):
            proc, args = parse_fn(line)
            new_set_file_buffer_call = (' '.join(args), 'set_file_buffer_call', args[0])
            print new_set_file_buffer_call
        elif line.startswith('ret:set_file_buffer'):
            proc, args, result = parse_ret(line)
            new_set_file_buffer_ret = (' '.join(args), 'set_file_buffer_return', result)
            print new_set_file_buffer_ret
    
        elif line.startswith('call:rmdir'):
            proc, args = parse_fn(line)
            new_rmdir_call = (' '.join(args), 'rmdir_call', args[0])
            print new_rmdir_call
        elif line.startswith('ret:rmdir'):
            proc, args, result = parse_ret(line)
            new_rmdir_ret = (' '.join(args), 'rmdir_return', result)
            print new_rmdir_ret
    
        elif line.startswith('call:socket_set_timeout'):
            proc, args = parse_fn(line)
            new_socket_set_timeout_call = (' '.join(args), 'socket_set_timeout_call', args[0])
            print new_socket_set_timeout_call
        elif line.startswith('ret:socket_set_timeout'):
            proc, args, result = parse_ret(line)
            new_socket_set_timeout_ret = (' '.join(args), 'socket_set_timeout_return', result)
            print new_socket_set_timeout_ret
    
        elif line.startswith('call:dns_get_mx'):
            proc, args = parse_fn(line)
            new_dns_get_mx_call = (' '.join(args), 'dns_get_mx_call', args[0])
            print new_dns_get_mx_call
        elif line.startswith('ret:dns_get_mx'):
            proc, args, result = parse_ret(line)
            new_dns_get_mx_ret = (' '.join(args), 'dns_get_mx_return', result)
            print new_dns_get_mx_ret
    
        elif line.startswith('call:getenv'):
            proc, args = parse_fn(line)
            new_getenv_call = (' '.join(args), 'getenv_call', args[0])
            print new_getenv_call
        elif line.startswith('ret:getenv'):
            proc, args, result = parse_ret(line)
            new_getenv_ret = (' '.join(args), 'getenv_return', result)
            print new_getenv_ret
    
        elif line.startswith('call:lchgrp'):
            proc, args = parse_fn(line)
            new_lchgrp_call = (' '.join(args), 'lchgrp_call', args[0])
            print new_lchgrp_call
        elif line.startswith('ret:lchgrp'):
            proc, args, result = parse_ret(line)
            new_lchgrp_ret = (' '.join(args), 'lchgrp_return', result)
            print new_lchgrp_ret
    
        elif line.startswith('call:link'):
            proc, args = parse_fn(line)
            new_link_call = (' '.join(args), 'link_call', args[0])
            print new_link_call
        elif line.startswith('ret:link'):
            proc, args, result = parse_ret(line)
            new_link_ret = (' '.join(args), 'link_return', result)
            print new_link_ret
    
        elif line.startswith('call:ssh2_scp_recv'):
            proc, args = parse_fn(line)
            new_ssh2_scp_recv_call = (' '.join(args), 'ssh2_scp_recv_call', args[0])
            print new_ssh2_scp_recv_call
        elif line.startswith('ret:ssh2_scp_recv'):
            proc, args, result = parse_ret(line)
            new_ssh2_scp_recv_ret = (' '.join(args), 'ssh2_scp_recv_return', result)
            print new_ssh2_scp_recv_ret
    
        elif line.startswith('call:copy'):
            proc, args = parse_fn(line)
            new_copy_call = (' '.join(args), 'copy_call', args[0])
            print new_copy_call
        elif line.startswith('ret:copy'):
            proc, args, result = parse_ret(line)
            new_copy_ret = (' '.join(args), 'copy_return', result)
            print new_copy_ret
    
        elif line.startswith('call:fgetss'):
            proc, args = parse_fn(line)
            new_fgetss_call = (' '.join(args), 'fgetss_call', args[0])
            print new_fgetss_call
        elif line.startswith('ret:fgetss'):
            proc, args, result = parse_ret(line)
            new_fgetss_ret = (' '.join(args), 'fgetss_return', result)
            print new_fgetss_ret
    
        elif line.startswith('call:fscanf'):
            proc, args = parse_fn(line)
            new_fscanf_call = (' '.join(args), 'fscanf_call', args[0])
            print new_fscanf_call
        elif line.startswith('ret:fscanf'):
            proc, args, result = parse_ret(line)
            new_fscanf_ret = (' '.join(args), 'fscanf_return', result)
            print new_fscanf_ret
    
        elif line.startswith('call:headers_list'):
            proc, args = parse_fn(line)
            new_headers_list_call = (' '.join(args), 'headers_list_call', args[0])
            print new_headers_list_call
        elif line.startswith('ret:headers_list'):
            proc, args, result = parse_ret(line)
            new_headers_list_ret = (' '.join(args), 'headers_list_return', result)
            print new_headers_list_ret
    
        elif line.startswith('call:proc_open'):
            proc, args = parse_fn(line)
            new_proc_open_call = (' '.join(args), 'proc_open_call', args[0])
            print new_proc_open_call
        elif line.startswith('ret:proc_open'):
            proc, args, result = parse_ret(line)
            new_proc_open_ret = (' '.join(args), 'proc_open_return', result)
            print new_proc_open_ret
    
        elif line.startswith('call:enabled'):
            proc, args = parse_fn(line)
            new_enabled_call = (' '.join(args), 'enabled_call', args[0])
            print new_enabled_call
        elif line.startswith('ret:enabled'):
            proc, args, result = parse_ret(line)
            new_enabled_ret = (' '.join(args), 'enabled_return', result)
            print new_enabled_ret
    
        elif line.startswith('call:file_exists'):
            proc, args = parse_fn(line)
            new_file_exists_call = (' '.join(args), 'file_exists_call', args[0])
            print new_file_exists_call
        elif line.startswith('ret:file_exists'):
            proc, args, result = parse_ret(line)
            new_file_exists_ret = (' '.join(args), 'file_exists_return', result)
            print new_file_exists_ret
    
        elif line.startswith('call:fnmatch'):
            proc, args = parse_fn(line)
            new_fnmatch_call = (' '.join(args), 'fnmatch_call', args[0])
            print new_fnmatch_call
        elif line.startswith('ret:fnmatch'):
            proc, args, result = parse_ret(line)
            new_fnmatch_ret = (' '.join(args), 'fnmatch_return', result)
            print new_fnmatch_ret
    
        elif line.startswith('call:ftruncate'):
            proc, args = parse_fn(line)
            new_ftruncate_call = (' '.join(args), 'ftruncate_call', args[0])
            print new_ftruncate_call
        elif line.startswith('ret:ftruncate'):
            proc, args, result = parse_ret(line)
            new_ftruncate_ret = (' '.join(args), 'ftruncate_return', result)
            print new_ftruncate_ret
    
        elif line.startswith('call:getprotobynumber'):
            proc, args = parse_fn(line)
            new_getprotobynumber_call = (' '.join(args), 'getprotobynumber_call', args[0])
            print new_getprotobynumber_call
        elif line.startswith('ret:getprotobynumber'):
            proc, args, result = parse_ret(line)
            new_getprotobynumber_ret = (' '.join(args), 'getprotobynumber_return', result)
            print new_getprotobynumber_ret
    
        elif line.startswith('call:delete'):
            proc, args = parse_fn(line)
            new_delete_call = (' '.join(args), 'delete_call', args[0])
            print new_delete_call
        elif line.startswith('ret:delete'):
            proc, args, result = parse_ret(line)
            new_delete_ret = (' '.join(args), 'delete_return', result)
            print new_delete_ret
    
        elif line.startswith('call:file_put_contents'):
            proc, args = parse_fn(line)
            new_file_put_contents_call = (' '.join(args), 'file_put_contents_call', args[0])
            print new_file_put_contents_call
        elif line.startswith('ret:file_put_contents'):
            proc, args, result = parse_ret(line)
            new_file_put_contents_ret = (' '.join(args), 'file_put_contents_return', result)
            print new_file_put_contents_ret
    
        elif line.startswith('call:socket_set_blocking'):
            proc, args = parse_fn(line)
            new_socket_set_blocking_call = (' '.join(args), 'socket_set_blocking_call', args[0])
            print new_socket_set_blocking_call
        elif line.startswith('ret:socket_set_blocking'):
            proc, args, result = parse_ret(line)
            new_socket_set_blocking_ret = (' '.join(args), 'socket_set_blocking_return', result)
            print new_socket_set_blocking_ret
    
        elif line.startswith('call:disk_free_space'):
            proc, args = parse_fn(line)
            new_disk_free_space_call = (' '.join(args), 'disk_free_space_call', args[0])
            print new_disk_free_space_call
        elif line.startswith('ret:disk_free_space'):
            proc, args, result = parse_ret(line)
            new_disk_free_space_ret = (' '.join(args), 'disk_free_space_return', result)
            print new_disk_free_space_ret
    
        elif line.startswith('call:realpath_cache_size'):
            proc, args = parse_fn(line)
            new_realpath_cache_size_call = (' '.join(args), 'realpath_cache_size_call', args[0])
            print new_realpath_cache_size_call
        elif line.startswith('ret:realpath_cache_size'):
            proc, args, result = parse_ret(line)
            new_realpath_cache_size_ret = (' '.join(args), 'realpath_cache_size_return', result)
            print new_realpath_cache_size_ret
    
        elif line.startswith('call:fread'):
            proc, args = parse_fn(line)
            new_fread_call = (' '.join(args), 'fread_call', args[0])
            print new_fread_call
        elif line.startswith('ret:fread'):
            proc, args, result = parse_ret(line)
            new_fread_ret = (' '.join(args), 'fread_return', result)
            print new_fread_ret
    
        elif line.startswith('call:fileperms'):
            proc, args = parse_fn(line)
            new_fileperms_call = (' '.join(args), 'fileperms_call', args[0])
            print new_fileperms_call
        elif line.startswith('ret:fileperms'):
            proc, args, result = parse_ret(line)
            new_fileperms_ret = (' '.join(args), 'fileperms_return', result)
            print new_fileperms_ret
    
        elif line.startswith('call:inet_pton'):
            proc, args = parse_fn(line)
            new_inet_pton_call = (' '.join(args), 'inet_pton_call', args[0])
            print new_inet_pton_call
        elif line.startswith('ret:inet_pton'):
            proc, args, result = parse_ret(line)
            new_inet_pton_ret = (' '.join(args), 'inet_pton_return', result)
            print new_inet_pton_ret
    
        elif line.startswith('call:file'):
            proc, args = parse_fn(line)
            new_file_call = (' '.join(args), 'file_call', args[0])
            print new_file_call
        elif line.startswith('ret:file'):
            proc, args, result = parse_ret(line)
            new_file_ret = (' '.join(args), 'file_return', result)
            print new_file_ret
    
        elif line.startswith('call:feof'):
            proc, args = parse_fn(line)
            new_feof_call = (' '.join(args), 'feof_call', args[0])
            print new_feof_call
        elif line.startswith('ret:feof'):
            proc, args, result = parse_ret(line)
            new_feof_ret = (' '.join(args), 'feof_return', result)
            print new_feof_ret
    
        elif line.startswith('call:is_writeable'):
            proc, args = parse_fn(line)
            new_is_writeable_call = (' '.join(args), 'is_writeable_call', args[0])
            print new_is_writeable_call
        elif line.startswith('ret:is_writeable'):
            proc, args, result = parse_ret(line)
            new_is_writeable_ret = (' '.join(args), 'is_writeable_return', result)
            print new_is_writeable_ret
    
        elif line.startswith('call:fpassthru'):
            proc, args = parse_fn(line)
            new_fpassthru_call = (' '.join(args), 'fpassthru_call', args[0])
            print new_fpassthru_call
        elif line.startswith('ret:fpassthru'):
            proc, args, result = parse_ret(line)
            new_fpassthru_ret = (' '.join(args), 'fpassthru_return', result)
            print new_fpassthru_ret
    
        elif line.startswith('call:socket_recv'):
            proc, args = parse_fn(line)
            new_socket_recv_call = (' '.join(args), 'socket_recv_call', args[0])
            print new_socket_recv_call
        elif line.startswith('ret:socket_recv'):
            proc, args, result = parse_ret(line)
            new_socket_recv_ret = (' '.join(args), 'socket_recv_return', result)
            print new_socket_recv_ret
    
        elif line.startswith('call:filegroup'):
            proc, args = parse_fn(line)
            new_filegroup_call = (' '.join(args), 'filegroup_call', args[0])
            print new_filegroup_call
        elif line.startswith('ret:filegroup'):
            proc, args, result = parse_ret(line)
            new_filegroup_ret = (' '.join(args), 'filegroup_return', result)
            print new_filegroup_ret
    
        elif line.startswith('call:fseek'):
            proc, args = parse_fn(line)
            new_fseek_call = (' '.join(args), 'fseek_call', args[0])
            print new_fseek_call
        elif line.startswith('ret:fseek'):
            proc, args, result = parse_ret(line)
            new_fseek_ret = (' '.join(args), 'fseek_return', result)
            print new_fseek_ret
    
        elif line.startswith('call:sendmail'):
            proc, args = parse_fn(line)
            new_sendmail_call = (' '.join(args), 'sendmail_call', args[0])
            print new_sendmail_call
        elif line.startswith('ret:sendmail'):
            proc, args, result = parse_ret(line)
            new_sendmail_ret = (' '.join(args), 'sendmail_return', result)
            print new_sendmail_ret
    
        elif line.startswith('call:chgrp'):
            proc, args = parse_fn(line)
            new_chgrp_call = (' '.join(args), 'chgrp_call', args[0])
            print new_chgrp_call
        elif line.startswith('ret:chgrp'):
            proc, args, result = parse_ret(line)
            new_chgrp_ret = (' '.join(args), 'chgrp_return', result)
            print new_chgrp_ret
    
        elif line.startswith('call:write'):
            proc, args = parse_fn(line)
            new_write_call = (' '.join(args), 'write_call', args[0])
            print new_write_call
        elif line.startswith('ret:write'):
            proc, args, result = parse_ret(line)
            new_write_ret = (' '.join(args), 'write_return', result)
            print new_write_ret
    
        elif line.startswith('call:filectime'):
            proc, args = parse_fn(line)
            new_filectime_call = (' '.join(args), 'filectime_call', args[0])
            print new_filectime_call
        elif line.startswith('ret:filectime'):
            proc, args, result = parse_ret(line)
            new_filectime_ret = (' '.join(args), 'filectime_return', result)
            print new_filectime_ret
    
        elif line.startswith('call:rewind'):
            proc, args = parse_fn(line)
            new_rewind_call = (' '.join(args), 'rewind_call', args[0])
            print new_rewind_call
        elif line.startswith('ret:rewind'):
            proc, args, result = parse_ret(line)
            new_rewind_ret = (' '.join(args), 'rewind_return', result)
            print new_rewind_ret
    
        elif line.startswith('call:fileinode'):
            proc, args = parse_fn(line)
            new_fileinode_call = (' '.join(args), 'fileinode_call', args[0])
            print new_fileinode_call
        elif line.startswith('ret:fileinode'):
            proc, args, result = parse_ret(line)
            new_fileinode_ret = (' '.join(args), 'fileinode_return', result)
            print new_fileinode_ret
    
        elif line.startswith('call:is_uploaded_file'):
            proc, args = parse_fn(line)
            new_is_uploaded_file_call = (' '.join(args), 'is_uploaded_file_call', args[0])
            print new_is_uploaded_file_call
        elif line.startswith('ret:is_uploaded_file'):
            proc, args, result = parse_ret(line)
            new_is_uploaded_file_ret = (' '.join(args), 'is_uploaded_file_return', result)
            print new_is_uploaded_file_ret
    
        elif line.startswith('call:realpath'):
            proc, args = parse_fn(line)
            new_realpath_call = (' '.join(args), 'realpath_call', args[0])
            print new_realpath_call
        elif line.startswith('ret:realpath'):
            proc, args, result = parse_ret(line)
            new_realpath_ret = (' '.join(args), 'realpath_return', result)
            print new_realpath_ret
    
        elif line.startswith('call:stat'):
            proc, args = parse_fn(line)
            new_stat_call = (' '.join(args), 'stat_call', args[0])
            print new_stat_call
        elif line.startswith('ret:stat'):
            proc, args, result = parse_ret(line)
            new_stat_ret = (' '.join(args), 'stat_return', result)
            print new_stat_ret
    
        elif line.startswith('call:disk_total_space'):
            proc, args = parse_fn(line)
            new_disk_total_space_call = (' '.join(args), 'disk_total_space_call', args[0])
            print new_disk_total_space_call
        elif line.startswith('ret:disk_total_space'):
            proc, args, result = parse_ret(line)
            new_disk_total_space_ret = (' '.join(args), 'disk_total_space_return', result)
            print new_disk_total_space_ret
    
        elif line.startswith('call:glob'):
            proc, args = parse_fn(line)
            new_glob_call = (' '.join(args), 'glob_call', args[0])
            print new_glob_call
        elif line.startswith('ret:glob'):
            proc, args, result = parse_ret(line)
            new_glob_ret = (' '.join(args), 'glob_return', result)
            print new_glob_ret
    
        elif line.startswith('call:gethostbyname'):
            proc, args = parse_fn(line)
            new_gethostbyname_call = (' '.join(args), 'gethostbyname_call', args[0])
            print new_gethostbyname_call
        elif line.startswith('ret:gethostbyname'):
            proc, args, result = parse_ret(line)
            new_gethostbyname_ret = (' '.join(args), 'gethostbyname_return', result)
            print new_gethostbyname_ret
    
        elif line.startswith('call:define_syslog_variables'):
            proc, args = parse_fn(line)
            new_define_syslog_variables_call = (' '.join(args), 'define_syslog_variables_call', args[0])
            print new_define_syslog_variables_call
        elif line.startswith('ret:define_syslog_variables'):
            proc, args, result = parse_ret(line)
            new_define_syslog_variables_ret = (' '.join(args), 'define_syslog_variables_return', result)
            print new_define_syslog_variables_ret
    
        elif line.startswith('call:readlink'):
            proc, args = parse_fn(line)
            new_readlink_call = (' '.join(args), 'readlink_call', args[0])
            print new_readlink_call
        elif line.startswith('ret:readlink'):
            proc, args, result = parse_ret(line)
            new_readlink_ret = (' '.join(args), 'readlink_return', result)
            print new_readlink_ret
    
        elif line.startswith('call:eval'):
            proc, args = parse_fn(line)
            new_eval_call = (' '.join(args), 'eval_call', args[0])
            print new_eval_call
        elif line.startswith('ret:eval'):
            proc, args, result = parse_ret(line)
            new_eval_ret = (' '.join(args), 'eval_return', result)
            print new_eval_ret
    
        elif line.startswith('call:escapeshellarg'):
            proc, args = parse_fn(line)
            new_escapeshellarg_call = (' '.join(args), 'escapeshellarg_call', args[0])
            print new_escapeshellarg_call
        elif line.startswith('ret:escapeshellarg'):
            proc, args, result = parse_ret(line)
            new_escapeshellarg_ret = (' '.join(args), 'escapeshellarg_return', result)
            print new_escapeshellarg_ret
    
        elif line.startswith('call:setcookie'):
            proc, args = parse_fn(line)
            new_setcookie_call = (' '.join(args), 'setcookie_call', args[0])
            print new_setcookie_call
        elif line.startswith('ret:setcookie'):
            proc, args, result = parse_ret(line)
            new_setcookie_ret = (' '.join(args), 'setcookie_return', result)
            print new_setcookie_ret
    
        elif line.startswith('call:fsockopen'):
            proc, args = parse_fn(line)
            new_fsockopen_call = (' '.join(args), 'fsockopen_call', args[0])
            print new_fsockopen_call
        elif line.startswith('ret:fsockopen'):
            proc, args, result = parse_ret(line)
            new_fsockopen_ret = (' '.join(args), 'fsockopen_return', result)
            print new_fsockopen_ret
    
        elif line.startswith('call:passthru'):
            proc, args = parse_fn(line)
            new_passthru_call = (' '.join(args), 'passthru_call', args[0])
            print new_passthru_call
        elif line.startswith('ret:passthru'):
            proc, args, result = parse_ret(line)
            new_passthru_ret = (' '.join(args), 'passthru_return', result)
            print new_passthru_ret
    
        elif line.startswith('call:getmyuid'):
            proc, args = parse_fn(line)
            new_getmyuid_call = (' '.join(args), 'getmyuid_call', args[0])
            print new_getmyuid_call
        elif line.startswith('ret:getmyuid'):
            proc, args, result = parse_ret(line)
            new_getmyuid_ret = (' '.join(args), 'getmyuid_return', result)
            print new_getmyuid_ret
    
        elif line.startswith('call:fileatime'):
            proc, args = parse_fn(line)
            new_fileatime_call = (' '.join(args), 'fileatime_call', args[0])
            print new_fileatime_call
        elif line.startswith('ret:fileatime'):
            proc, args, result = parse_ret(line)
            new_fileatime_ret = (' '.join(args), 'fileatime_return', result)
            print new_fileatime_ret
    
        elif line.startswith('call:chown'):
            proc, args = parse_fn(line)
            new_chown_call = (' '.join(args), 'chown_call', args[0])
            print new_chown_call
        elif line.startswith('ret:chown'):
            proc, args, result = parse_ret(line)
            new_chown_ret = (' '.join(args), 'chown_return', result)
            print new_chown_ret
    
        elif line.startswith('call:pathinfo'):
            proc, args = parse_fn(line)
            new_pathinfo_call = (' '.join(args), 'pathinfo_call', args[0])
            print new_pathinfo_call
        elif line.startswith('ret:pathinfo'):
            proc, args, result = parse_ret(line)
            new_pathinfo_ret = (' '.join(args), 'pathinfo_return', result)
            print new_pathinfo_ret
    
        elif line.startswith('call:file_get_contents'):
            proc, args = parse_fn(line)
            new_file_get_contents_call = (' '.join(args), 'file_get_contents_call', args[0])
            print new_file_get_contents_call
        elif line.startswith('ret:file_get_contents'):
            proc, args, result = parse_ret(line)
            new_file_get_contents_ret = (' '.join(args), 'file_get_contents_return', result)
            print new_file_get_contents_ret
