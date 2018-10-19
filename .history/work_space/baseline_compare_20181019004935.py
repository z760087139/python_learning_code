# import re
class Db(object):
    def __init__(self):
        self.cfg_list = []
    # self.cfg_list = [Cfg,Cfg,Cfg]

# class Cfg(object):
#     def __init__():
#         self.paras = {}

#     @classmethod
#     def create(cls,path1,path2):
#        # get name
#         for line in path1:
#             # name = line.split(',')
#             self.paras[name] = Para(name)
#             self.paras[name].input_sit(line)
#         for line in path2:
#             if not self.paras.get(name):
#                 self.paras[name] = Para(name)
#             self.paras[name].input_ecc(line)
                

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
        name,value1,value2 = cls.split_func(cls,line1,line2)
        cls.input_sit(cls,value1)
        cls.input_ecc(cls,value2)
        k = cls(name)
        # k.input_ecc(line1)
        # k.input_sit(line2)
        return k 
        
        

class Para_Set(Para):
    def split_func(self,line1,line2):
        # name1 = line1.split(',')[0]
        # value1 = {}...
        name1 = 'a'
        value1 = line1
        value2 = line2
        return name1,value1,value2

# class Para_Space(Para):
#     def split_func(self,line1,line2):
#         # name1 = line1.split(',')[0]
#         # value1 = {}...
#         name1 = 'a'
#         value1 = line1
#         value2 = line2
#         return name1,value1,value2
#  ... 



def func(names,values):
    workers = []
    for group in zip(names,values):
        name,value = group
        workers.append(Cfg(name).input_sit(value))
    return workers

# names =  ['A','B','C']
# values = [1,2,3]
# test = func(names,values)
# print(test)

b = Para_Set.create('a','b')
print(b)