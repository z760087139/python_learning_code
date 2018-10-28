# -*- coding:UTF-8 -*-
# subprocess 用来执行其他的可执行程序的，即执行外部命令。(ex_subprocess)
# multiprocessing用来执行python的函数，他启动的进程会重新加载父进程的代码。(ex_multiprocessing.py)

import multiprocessing as mp
import ex_multiprocessing_import as mi
name = 'doing'
k = mp.Process(target=mi.test_func,args=(name,) )
k.start()
k.join()
print('child finish')
# mi.start_thread(name)
