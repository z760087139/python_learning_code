class part1(object):
    def __init__(self,name):
        self.name = name
    @classmethod
    def create(cls,a):
        k = cls.func1(cls,a)
        b = cls('a')
        cls.result = b.func1(k)
        return b 
    def func1(self,b):
        b += 3
        return b
    @classmethod
    def use_func2(cls,a):
        cls.



class part2(part1):
    def func1(self,a):
        a += 1
        return a
    @classmethod
    def func2(cls,a):
        a += 10
        return a



b = part2.create(1)
print(b)
c = part2.create(20)
print(c)
b.result = 6
print(b)
a = part2.create(10)
print(a)