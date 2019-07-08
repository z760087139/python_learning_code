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

k = Lazy()
print('-'*30)
print(k.num)
print('-'*30)
print(k.__dict__)
print('-'*30)
print(k.foo)
print('-'*30)
print(k.__dict__)

# __new__(cls[, ...])

# 1. __new__ 是在一个对象实例化的时候所调用的第一个方法
# 2. 它的第一个参数是这个类，其他的参数是用来直接传递给 __init__ 方法
# 3. __new__ 决定是否要使用该 __init__ 方法，因为 __new__ 可以调用其他类的构造方法或者直接返回别的实例对象来作为本类的实例，如果 __new__ 没有返回实例对象，则 __init__ 不会被调用
# 4. __new__ 主要是用于继承一个不可变的类型比如一个 tuple 或者 string

# __init__(self[, ...])

# 构造器，当一个实例被创建的时候调用的初始化方法

# __del__(self)

# 析构器，当一个实例被销毁的时候调用的方法

# __call__(self[, args...])

# 允许一个类的实例像函数一样被调用：x(a, b) 调用 x.__call__(a, b)

# __len__(self)

# 定义当被 len() 调用时的行为

# __repr__(self)

# 定义当被 repr() 调用时的行为

# __str__(self)

# 定义当被 str() 调用时的行为

# __bytes__(self)

# 定义当被 bytes() 调用时的行为

# __hash__(self)

# 定义当被 hash() 调用时的行为

# __bool__(self)

# 定义当被 bool() 调用时的行为，应该返回 True 或 False

# __format__(self, format_spec)

# 定义当被 format() 调用时的行为
