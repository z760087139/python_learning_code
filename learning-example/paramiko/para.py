# connect function:
connect(hostname, port=22, username=None, password=None, pkey=None,
 key_filename=None,timeout=None, allow_agent=True, look_for_keys=True, 
compress=False, sock=None, gss_auth=False,gss_kex=False, 
gss_deleg_creds=True, gss_host=None, banner_timeout=None)

Parameters
hostname (str) – the server to connect to
port (int) – the server port to connect to
username (str) – the username to authenticate as (defaults to the current local username)
password (str) – a password to use for authentication or for unlocking a private key
pkey (.PKey) – an optional private key to use for authentication
key_filename (str) – the filename, or list of filenames, of optional private key(s) to try for authentication
timeout (float) – an optional timeout (in seconds) for the TCP connect
allow_agent (bool) – set to False to disable connecting to the SSH agent
look_for_keys (bool) – set to False to disable searching for discoverable private key files in ~/.ssh/
compress (bool) – set to True to turn on compression
sock (socket) – an open socket or socket-like object (such as a Channel) to use for communication to the target host
gss_auth (bool) – True if you want to use GSS-API authentication
gss_kex (bool) – Perform GSS-API Key Exchange and user authentication
gss_deleg_creds (bool) – Delegate GSS-API client credentials or not
gss_host (str) – The targets name in the kerberos database. default: hostname
banner_timeout (float) – an optional timeout (in seconds) to wait for the SSH banner to be presented.
Raises	
BadHostKeyException – if the server’s host key could not be verified
AuthenticationException – if authentication failed
SSHException – if there was any other error connecting or establishing an SSH session
socket.error – if a socket error occurred while connecting


# exec_command function
exec_command(command, bufsize=-1, timeout=None, get_pty=False)
Execute a command on the SSH server. A new Channel is opened and the requested command is executed. The command’s input and output streams are returned as Pythonfile-like objects representing stdin, stdout, and stderr.

Parameters	command (str) – the command to execute
bufsize (int) – interpreted the same way as by the built-in file()function in Python
timeout (int) – set command’s channel timeout. SeeChannel.settimeout.settimeout
Returns	the stdin, stdout, and stderr of the executing command, as a 3-tuple
Raises	SSHException:if the server fails to execute the command