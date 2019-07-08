# -*- coding:UTF-8 -*-
# subprocess 用来执行其他的可执行程序的，即执行外部命令。(ex_subprocess)
# multiprocessing用来执行python的函数，他启动的进程会重新加载父进程的代码。(ex_multiprocessing.py)
import subprocess

# 3个基本方法
subprocess.call(['ls','-l'])
# 返回执行状态
subprocess.check_call()
# 返回状态码 否则异常
subprocess.check_output('ls -l',shell=True)
# 返回执行结果 否则异常

# 原方法
subprocess.Popen('ls -l',shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
# 可选传参内容
# args shell 命令，字符串或者列表。
# bufsize 缓存策略，0 = 不缓存  >1 = 缓冲区大小 <0 = 系统默认缓冲策略
# stdin,stdou,stderr  标准输入，输出，错误句柄
# preexec_fn 子进程运行前调用的可执行对象
# close_fds 如果设置为True ,除了 0,1,2以外的文件描述符都会在子进程执行前被关闭
# shell 以shell形式执行
# cwd 如果不是None 则在执行子进程前更改当前目录
# env 设置子进程的环境变量  如果env=None ，继承父进程环境。env != None ，值必须是映射对象
# universal_newlines 若为True，stdin,stdout,stderr会被文件流打开，否则为二进制流打开
# startupinfo,creationflags  Windows下有效，传递给createprocess函数，设置子进程外观，优先级

# subprocess.Popen类方法
# Popen.poll() 检查子进程是否已结束，没结束返回None，结束后返回状态码
# Popen.wait(timeout=None) 等待子进程结束，返回状态码。timeout 抛出TimeoutExpired异常
# Popen.communicate(input=None,timeout=None) 进程交互使用，发送数据到stdin，从stdout,
#       stderr读取数据，直到文件末尾 
#       input必须是字符串，返回的是(stdout_data,stderr_data)的元组
# Popen.send_signal(signal) 发送信号给子进程
# Popen.terminate() 停止子进程
# Popen.kill() 杀死子进程