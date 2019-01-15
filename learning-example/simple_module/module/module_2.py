# use by ex_variables.py
mod2_var = 'mod2'

def change_var():
    global mod2_var
    mod2_var = 'new'

class TestC(object):
    def __init__(self):
        self.data = [3,2,1]

    def data_init(self):
        print(globals().keys())
        self.data = [1,2,3]

base_c = TestC()

def get_var():
    print(globals()['__name__'])
    print(locals())

new_base = TestC()
