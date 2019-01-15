# -*- coding:utf-8 -*-
# 1. 调用其他 module 的简单、不可变的对象，无法使用引用方式。即修改module_1.mod1_var 无法改变k值 example 1
# 2. 调用 module 中的函数，如果不适用 global 定义全局变量，无法修改 module_1.mod1_var 的值。 example 1
# 3. module 中的函数，使用的 global 全局变量，仅对 module 而言全局 example 1
# 4. module 中使用主函数的变量，会抛出未定义的报错 example 1
# 5. 对层 module 的导入，与上述规则相同 exapmle 2 3
# 6. 对于复杂的数据结构，变量只指向第一层对象的内存地址，因此对象属性的内存地址发生改变，变量的指向也不会改变 example 4
# 7. 在函数中引用的是相同的id，但是因为复杂对象的关系，即使修改也不会改变这个变量的id，
#    因此即使是调用module的函数修改test_list或者在 module 修改 module.test_list，都会将结果反映到变量中。（因为对应id下的属性发生变化）
# 8. 如果是类对象，适用第6,7点内容，可以在实例化后作为复杂对象使用。如 example 6 在module 2 定义，实例化的对象base_c
#    在main 和 module 引用，指向相同的id，并在main中进行 base_c.data 的值修改，会同时适用到各个引用的地方
# 9. 按照第8点的内容，如果多进程或者多线程进行相同的指针内容修改，可能导致争用和数据错乱
from module import module_1
from module import module_2

# # example 1
# k = module_1.mod1_var
# print('k id : %s' % id(k))
# print('var id : %s' % id(module_1.mod1_var))
# print('change var')
# # if global mod1_var in function module_1.change_var()
# module_1.change_var()
# print('k id : %s' % id(k))
# print('var id : %s' % id(module_1.mod1_var))
# print('var : %s' % module_1.mod1_var)
# module_1.mod1_var = 'break'
# print('new var : %s' % id(module_1.mod1_var))
# module_1.change_var()
# print('new var : %s' % id(module_1.mod1_var))

# # example 2
# print('-'*30)
# b = module_1.mod2_var
# print('b id : %s' % id(b))
# print('mod1_mod2_var id : %s' % id(module_1.mod2_var))
# print('change var2')
# # not global mod2_var in function module_2.change_var2() 
# module_1.change_var2()
# print('b id : %s' % id(b))
# print('mod1_mod2_var id : %s' % id(module_1.mod2_var))

# # example 3
# print('-'*30)
# print('b id : %s' % id(b))
# print('mod1_mod2_var id : %s' % id(module_1.mod2_var))
# print('change var2')
# module_1.change_var3()
# print('b id : %s' % id(b))
# print('mod1_mod2_var id : %s' % id(module_1.mod2_var))

def print_id(test_list):
    print('id(list) in print function :%s' % id(test_list))
    id_list = [id(x) for x in test_list]
    print('id list %s:' % id_list)

# example 4
# test_list = [1,2,3,4]
# print('id(list): %s' % id(test_list))
# print_id(test_list)

# print('-'*30)
# print('new list')

# print('id(list): %s' % id(test_list))
# print_id(test_list)

# example 5
# test_list = module_1.test_list
# print('id(test_list) :%s' % id(test_list))
# print_id(test_list)
# print('id(module_1.test_list) : %s' % id(module_1.test_list))
# print_id(module_1.test_list)

# print('-'*30)
# print('change list_var')
# module_1.change_list_1(test_list)
# print('id(test_list) :%s' % id(test_list))
# print_id(test_list)
# print('id(module_1.test_list) : %s' % id(module_1.test_list))
# print_id(module_1.test_list)

# print('-'*30)
# print('change list_var')
# module_1.change_list_2()
# print('id(test_list) :%s' % id(test_list))
# print_id(test_list)
# print('id(module_1.test_list) : %s' % id(module_1.test_list))
# print_id(module_1.test_list)

# example 6
base_c = module_2.base_c
print('Class id :%s' % id(base_c))
print('moduele_base id : %s' % id(module_1.base_c))
print('-'*30)
base_c.data_init()
print('Class id :%s' % id(base_c))
print('moduele_base id : %s' % id(module_1.base_c))
print('Class : %s' % base_c.data)
print('Class : %s' % module_1.base_c.data)
module_2.get_var()

test_base = module_2.TestC()
test_base.data_init()