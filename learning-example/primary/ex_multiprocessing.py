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

# 进程之间通信可以使用Queue
# 但是如果使用了进程池Pool,需要使用专门的Manager().Queue()
# q = Queue
# q.get() q.put() q.empty() q.full()

from multiprocessing import Pool
from datetime import datetime
import time
def func(i):
    start = datetime.now().strftime('%T')
    print('%s is start,%s' % (str(i),start))
    time.sleep(2)
    end = datetime.now().strftime('%T')
    print('%s is end,%s' % (str(i),end))

if __name__=='__main__':
    pool =Pool(3)
    for i in range(2):
        pool.apply_async(func,args=(i,))
    pool.close()
    pool.join()
    print('something')