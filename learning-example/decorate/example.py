# -- coding: utf-8 --
#########################
# simple example
result = []
def foo1(get_string):
    def foo2(func):
        def foo3(*args,**kwargs):
            a = func(*args,**kwargs)
            result.append(a)
        return foo3
    print('%s' % get_string)
    return foo2

@foo1('start:')
def func(*args,**kwargs):
    print('right')
    return args[0]

############
#
# run
#
# func(1)
# func(2,3)
# print result
############

################
# decorate in decorate

def A(funE_decorated_by_C):
    def redecorated_E(str):
        return funE_decorated_by_C(str)+' > redecorated by A'
    return redecorated_E

def C(funE):
    def decorated_E(str):
        return funE(str)+' > decorated by C'
    return decorated_E
###############
# run
# @A
# @C
# def E(str):
#     return str
################

#################
# decorate in class and use from other module
import decorate_class
a = decorate_class.test_class()
########################
# run
# a.func(1,2,3)
########################


