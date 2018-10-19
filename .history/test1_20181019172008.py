class part1(object):
    def __init__(self,name):
        self.name = name

    @classmethod
    def create(cls,par1):
        k = cls.func1(cls,par1)
        b = cls('a')
        cls.result = b.func1(k)
        return b 

    def func1(self,b):
        b += 3
        return b

class part2(part1):
    def func1(self,a):
        a += 1
        return a



b = part2.create(1)
print(b)
b.result = 6
print(b)
a = part2.create(10)
print(a)