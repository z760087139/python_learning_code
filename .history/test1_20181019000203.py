class part1(object):
    # @classmethod
    def create(self,par1):
        return self.func1(par1)

    def func1(self,b):
        b += 2
        return b

class part2(part1):
    def func1(self,a):
        a += 1
        return a

b = part2().create(1)
print(b)
