# to set environ in python
import os
for key,value in os.environ.items():
    print('%s : %s' % (key,value))

# os.environ is a dict, stored the env variables
# to change ORACLE_SID:
os.environ['ORACLE_SID'] = 'test'
os.popen('echo $ORACLE_SID').read() # > test