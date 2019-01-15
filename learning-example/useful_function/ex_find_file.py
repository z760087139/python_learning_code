# -*- coding:utf-8 -*-
import datetime
import os
import re

# 获取当前时间
current_time = datetime.datetime.now()
# 输入文件夹路径
directory = input('full directory path:')
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
