# -*- coding:utf-8 -*-
import datetime
import os
import re
import psutil
import wmi

user = 
conn = wmi.WMI(computer=ipaddress, user=user, password=password)


# 需要删除的进程名
ps_name_list = ['iexplore.exe','chrome.exe','ctihuaweiexe.exe','EBeeper.exe','SimpleEventServer.exe']
# 查找并删除进程
for ps in psutil.process_iter():
    if ps.name() in ps_name_list:
        ps.terminate()

# 获取当前时间
current_time = datetime.datetime.now()
# 输入文件夹路径
log_dir = input('full directory path:')
# 获取目录下文件名
filelist = os.listdir(directory)

# 正则文件名称 并找出最近接当前时间的文件
file_pa = re.compile(r'')
file_pa_name = []
file_pa_time = []
for _,name in enumerate(filelist):
    ma = re.search(file_pa,name)
    if ma :
        file_pa_name.append(name)
        str_time = ma.group('name')
        time = datetime.datetime.strptime(str_time)
        file_pa_time.append(abs(time-current_time))
file_name = file_pa_name.index(min(file_pa_time))

# 正则内容
with open(file_name) as f:
    ..
