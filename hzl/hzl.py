# import paramiko

# user = 'dddxadmin'
# pswd = 'worlord123@123'
# host = '192.168.23.129'
# user = 
# ssh = paramiko.SSHClient()

import wmi

ipaddress = '192.168.23.129'
user = 'dddxadmin'
conn = wmi.WMI(computer=ipaddress, user=user, password='test')