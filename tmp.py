def foo():
    print(f'before globals: {globals().keys()}')
    print(f'before locals: {locals().keys()}')
    exec('y = 1 + 1')
    print(f'after globals: {globals().keys()}')
    print(f'after locals: {locals().keys()}')

foo()