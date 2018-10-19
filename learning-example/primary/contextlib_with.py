# 重定向标准输出   将屏幕内容输出到文件中
# 1:
import sys
file_path = 'test.txt'
with open(file_path,'w') as obj:
    sys.stdout = obj
    # some output command
    help(sum)



