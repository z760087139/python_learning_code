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

class Para(object):
    def __init__(self,name):
        self.name = name
        self.diff = 0

    def input_sit(self,value):
        self.sit = value

    def input_ecc(self,value):
        self.ecc = value

    def diff_func(self):
        try : 
            if self.sit == self.ecc:
                self.diff = 1
            else:
                self.diff = 2    
        except NameError as e:
            if 'sit' in str(e):
                return 3
            elif 'ecc' in str(e):
                return 4
            else :
                raise
        except :
            raise
    
    def get_name(self):
        return self.name

    def get_sit(self,value):
        return self.sit
    
    def get_ecc(self,value):
        return self.ecc

    def get_diff(self):
        return self.diff

    @classmethod
    def create(cls,line1,line2):
        name1,value1,value2 = cls.split_func(cls,line1,line2)
        k = cls(name)
        k.input_ecc(line1)
        k.input_sit(line2)
        return k 
        
        

class Para_Set(Para):
    def split_func(self,line1,line2):
        # name1 = line1.split(',')[0]
        # value1 = {}...
        name1 = 'a'
        value1 = line1
        value2 = line2
        return name1,value1,value2


b = Para_Set.create('a','b')
print(b)