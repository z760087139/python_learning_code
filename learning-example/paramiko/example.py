# paramiko 1.7+
# get connect using user/password SSH
import paramiko

host = '192.168.23.130'
user = 'root'
password = 'zeng123+'
# paramiko log
paramiko.util.log_to_file('syslogin.log')
# create a client
ssh = paramiko.SSHClient()
# get client key :
# ssh.load_host_keys()
# if system do not save any host keys or is using to connect to an unkown host
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# connect
ssh.connect(hostname=host, username=user, password = password)
# command
stdin, stdout, stderr = ssh.exec_command('free -m')
# print result
print stdout.read()
# if more input is needed
# such as "su - root"
# stdin,stdout,stderr = ssh.exec_command('su - root')
# stdin.write('password')
# stdin.flush()
# stdout.read()

# close connect
ssh.close()


# using transport
trans = paramiko.Transport(('192.168.23.130',22))
trans.connect(username='root',password='zeng123+')
ssh = paramiko.SSHClient()
ssh._transport = trans
stdin.stdout,stderr = ssh.exec_command('free -m')
print(stdout.read().decode())
# open channel
session = trans.open_session()
session.invoke_shell()
session.recv()
session.send('ls -l /tmp')
# close()
# trans.close()

# get_pty()
trans = paramiko.Transport(('192.168.2.129',22))
trans.start_client()
trans.auth_password(username='root',password='zeng123+')
channel.trans.open_session()
channel.get_pty()
channel.invoke_shell()
