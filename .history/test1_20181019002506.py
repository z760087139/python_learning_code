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
        b += 2
        return b

class part2(part1):
    def func1(self,a):
        a += 1
        return a

b = []
for k in range(0,10):
    b.append(part2.create(1))
print(b)
