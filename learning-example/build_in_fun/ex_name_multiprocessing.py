from multiprocessing import Pool
def mp_exe():
    exec('a = 3',{},locals())
    exec('b = 3')
    exec('c = 3',{})
    print(f'locals:{locals()}')
    print(f'globals:{globals().keys()}')
    print('star printing:')
    try:
        print(a)
    except Exception as e:
        print(str(e))
    try:
        print(b)
    except Exception as e:
        print(str(e))
    try:
        print(c)
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    pool = Pool(2)
    for i in range(1):
        pool.apply_async(mp_exe)
    pool.close()
    pool.join()