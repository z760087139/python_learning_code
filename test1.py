class part1(object):
    def __init__(self,name):
        self.name = name
        self.other = 1
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
        tmp_result = cls.func2(a)
        k = cls(str(tmp_result))
        result = cls.func1(cls,cls.other)
        return str(result)



class part2(part1):
    def func1(self,a):
        a += 1
        return a
    @classmethod
    def func2(cls,a):
        a += 10
        return a



b = part2.use_func2(1)
print(b)
