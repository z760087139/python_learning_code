from contextlib import contextmanager

@contextmanager
def demo():
    print '这里的代码相当于__enter__里面的代码'
    yield 'i ma value'
    print '这里的代码相当于__exit__里面的代码'

with demo() as value:
    print  value