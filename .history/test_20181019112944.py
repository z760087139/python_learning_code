class P1 (object):
    def __init__(self,name):
        self.name = name

    @classmethod
    def create(cls,line):
        name = cls.line_split(line)['name']
        return cls(name)

class P2(P1):
    @classmethod
    def line_split(cls,line):
        result = {}
        result['name'] = line
        result['other'] = 1
        return result

k = P2.create('a')
print(k)