from multiprocessing import Process
import ex_name

if __name__ == '__main__':
    print('main start')
    k = Process(target=ex_name.outer)
    k.start()
    k.join()
    print('main end')


# from multiprocessing import Process,Pool
# import time
# import os 

# def outer():
#     print('start')
#     pool = Pool(2)
#     print('outer name : %s' % __name__)
#     print('outer id: %s' % os.getpid())
#     print('outer pid : %s' % os.getppid())
#     k = 10
#     print(k)
#     print(__name__)
#     # if __name__ == '__mp_main__':
#     #     for x in range(0,3):
#     #         pool.apply_async(inner)
#     #     pool.close()
#     #     pool.join()
#     print(k)

# def inner():
#     print('inner')
#     print('inner name: %s ' % __name__)
#     print('inner id: %s' % os.getpid())
#     print('inner pid : %s' % os.getppid())
#     time.sleep(5)
#     k = 5
#     print('inner end')

# if __name__ == '__main__':
#     print('main start')
#     k = Process(target=outer)
#     k.start()
#     k.join()
#     print('main end')
