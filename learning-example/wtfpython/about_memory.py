# -*- coding:utf-8 -*-
# 由于 Cpython 在编译优化时, 某些情况下会尝试使用已经存在的不可变对象而不是每次都创建一个新对象. 
# (这种行为被称作字符串的驻留[string interning])
    # 字符串在编译时被实现 ('wtf' 将被驻留, 但是 ''.join(['w', 't', 'f'] 将不会被驻留)
    # 字符串中只包含字母，数字或下划线时将会驻留
    # 常量折叠(constant folding) 是 Python 中的一种 窥孔优化(peephole optimization) 技术. 
        # 这意味着在编译时表达式 'a'*20 会被替换为 'aaaaaaaaaaaaaaaaaaaa' 以减少运行时的时钟周期. 
        # 只有长度小于 20 的字符串才会发生常量折叠
ex_1_a = 'same'
ex_1_b = 'same'
ex_1_a is ex_1_b  # True

ex_1_c = 'same?'
ex_1_d = 'same?'
ex_1_c is ex_1_d  # False

