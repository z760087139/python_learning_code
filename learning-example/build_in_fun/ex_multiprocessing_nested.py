import multiprocessing as mp
from multiprocessing import Pool,Manager
import time
import os 

def step_1():
    list_1 = [[1,2],[3,4]]
    processes = [
        mp.Process(target=step_5,args=(i,))
        for i in list_1
    ]
    for i in processes:
        i.start()
    print(mp.active_children())
    time.sleep(10)
    print(f'before is_alive:\n{os.popen("ps -ef|grep python").read()}')
    for i in processes:
        i.is_alive()
    time.sleep(5)
    print(f'called is_alive:\n{os.popen("ps -ef|grep python").read()}')
    time.sleep(5)
    for i in processes:
        i.join()
    print(f'called join:\n{os.popen("ps -ef|grep python").read()}')
    


def step_6():
    list_1 = [[1,2],[3,4]]
    pool_6 = Pool(2)
    for i in list_1:
        pool_6.apply(step_5,args=(i,))
    pool_6.close()
    pool_6.join()


def step_2(infos):
    processes = [
        mp.Process(target=step_3,args=(i,))
        for i in infos
    ]
    for i in processes:
        i.start()
    for i in processes:
        i.join()

def step_5(infos):
    def k(**i):
        print(f'i:{i}')
    def f(infos,*args,**kwargs):
        print(f'infos:{infos}')
        print(f'type(infos):{type(infos)}' )
        print(f'args:{args}' )
        print(f'kwargs:{kwargs}' )
    pool = Pool(2)
    for i in infos:
        pool.apply_async(step_3,args=(i,),callback=k,error_callback=f)
    pool.close()
    pool.join()

def step_3(infos):
    if infos ==4:
        kkk.get()
    time.sleep(5)
    print(f'{infos} is finish')
    return a=10,b=11

def step_4():
    print('finish')

if __name__=='__main__':
    step_1()