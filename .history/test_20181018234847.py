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
        self.diff = False

    def input_sit(self,value):
        self.sit = value

    def input_ecc(self,value):
        self.ecc = value

    def diff_func(self):
        try : 
            if self.sit == self.ecc:
                self.diff = True
        except NameError as e:
            if 'sit' in str(e):
                return 4
            elif 'ecc' in str(e):
                return 5
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
        name1,value1,name2,value2 = cls.split_func(line1,line2)

class Para_Set(Para):
    def split_func(self,line1,line2):
        # name1 = line1.split(',')[0]
        # name2 = line2.split(',')[0]
        # value1 = {}...
        return name1,value1,name2,value2

    



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
name = 'A'
k = Para(name)
k.input_sit(1)
k.diff_func()
print(dir(k))