class Db(object):
    def __init__(self):
        self.cfg_list = []
    # self.cfg_list = [Cfg,Cfg,Cfg]

class Cfg(object):
    def __init__(self,name):
        self.name = name

    # def input_sit(self,value):
    #     if self.sit = value :


    # def get_diff(self):

class Para(object):
    def __init__(self,name):
        self.name = name
        self.diff = False

    def input_sit(self,value):
        self.sit = value

    def input_ecc(self,value):
        self.ecc = value

    def get_sit(self,value):
        return self.sit
    
    def get_ecc(self,value):
        return self.ecc

    def diff_func(self):
        if self.sit not in locals() :
            print(locals())

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
dir(k)