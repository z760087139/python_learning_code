# 有效调用__getattribute__ 获取属性，没有发现则调用__getattr__

class Lazy(object):
    def __init__(self):
        self.num = 1
    def __getattribute__(self,name):
        print('__getattribute__(%s)' % name)
        return super().__getattribute__(name)
    def __setattr__(self,name,value):
        print(f'__setattr__{name},{value}')
        super().__setattr__(name,value)
    def __getattr__(self,name):
        print('__getattr__(%s)' % name)
        default_value = 10
        # setattr(self,name,default_value)
        self.__dict__[name] = default_value
        return default_value
    # def func1(self):
    #     print('func1')
    # def func2(self):
    #     print('func2')
    # def __setitem__(self,name,value):
        # print('Calling __setitem__()')

k = Lazy()
print('-'*30)
print(k.num)
print('-'*30)
print(k.__dict__)
print('-'*30)
print(k.foo)
print('-'*30)
print(k.__dict__)
# print('-'*30)
# k['b'] = 'c'
# print('-'*30)
# print(k.__dict__)
