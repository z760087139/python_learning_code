# use by ex_variables.py
from module import module_2

def func_mod1():
    return module_2

mod1_var = 'k'

def change_var():
    # make mod1_var global
    global mod1_var
    print(id(mod1_var))
    mod1_var = 'new'
    # NameError : 'k' is not defined
    # global k 
    # print('k :%s' % k)
    # print('k id :%s' % id(k))

mod2_var = module_2.mod2_var

def change_var2():
    """
    just change module_1.mod2_var to 'mod1_new'
    and print module_1.mod2_var,module_2.mod2_var 's id
    """
    mod2_var = 'mod1_new'
    print('module_1.mod2_var : %s' % mod2_var)
    print('module_1.mod2_var id : %s' % id(mod2_var))
    print('module_2.mod2_var id : %s' % id(module_2.mod2_var))

def change_var3():
    """
    use module_2.change_var function to change global module_2.mod2_var
    and print module_1.mod2_var and module_2.mod2_var 
    """
    module_2.change_var()
    print('module_1.mod2_var id : %s' % id(mod2_var))
    print('module_2.mod2_var id : %s' % id(module_2.mod2_var))

test_list = [1,2,3,4]

def change_list_1(data):
    data[1] = 'K'


def  change_list_2():
    test_list[1]='B'

base_c = module_2.base_c