import time
import random
import multiprocessing as mp
import os
def test_func(name):
    for i in range(5):
        print(name)
        time.sleep(random.randrange(3,6))
    print('done')
# name = 'doing'

def start_thread(name): 
    k = mp.Process(target =test_func,args=(name,) )
    k.start()
    k.join()
    print('done')

print('pid :%s' % os.getpid())
print('start')