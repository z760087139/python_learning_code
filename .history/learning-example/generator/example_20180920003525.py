# -- coding: utf-8 --

#自定义类的迭代器
class func1(object):
    def __init__(self):
        self.curr = 1
        self.prev = 0
    
    def __iter__(self):
        return self
#python 3
    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value
#python 2
    def next(self):
        return self.__next__()

a = func1()
b = iter(a)  # same as a.__iter__()  

#generate
#yield is returning a generate 
def func2(n):
    x = 0
    while x < n :
        yield x   
        x += 1

# generate can use in for loopo or using next()
for i in func2(5):
    print i 

c = func2(5)
print c.next()
# same as :
# for i in c:
#     print i
