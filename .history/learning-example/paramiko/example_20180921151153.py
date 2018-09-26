# paramiko 1.7+
# get connect using user/password
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
# close connect
ssh.close()


