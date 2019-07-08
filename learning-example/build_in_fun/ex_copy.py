# copy,deepcopy都会创建新的地址
# 但是普通子对象的地址重复（估计是节省空间）
# copy,deepcopy区别在于复杂的子对象地址
# deepcopy的复杂型子对象地址与源子对象地址不同
# 但copy的复杂型子对象地址与源数据保持一致 
# (看最后的numbers[2][1]='k')
# 另外，若子对象赋予的新值与源数据赋予的新值一致，会出现地址一致的情况(如省略部分的例子)


import copy

numbers = [1,2,[1,2,3]]
n_num = numbers
c_num = copy.copy(numbers)
d_num = copy.deepcopy(numbers)

print('numbers is %s' % id(numbers))
print('n_num is %s' % id(n_num))
print('c_num is %s' % id(c_num))
print('d_num is %s' % id(d_num))
print('numbers[0] is %s' % id(numbers[0]))
print('n_num[0] is %s' % id(n_num[0]))
print('c_num[0] is %s' % id(c_num[0]))
print('d_num[0] is %s' % id(d_num[0]))
print('numbers[1] is %s' % id(numbers[1]))
print('n_num[1] is %s' % id(n_num[1]))
print('c_num[1] is %s' % id(c_num[1]))
print('d_num[1] is %s' % id(d_num[1]))
print('numbers[2] is %s' % id(numbers[2]))
print('n_num[2] is %s' % id(n_num[2]))
print('c_num[2] is %s' % id(c_num[2]))
print('d_num[2] is %s' % id(d_num[2]))

numbers[1] = 'k'
print('----------------numbers[1]=k------------------')
print('numbers[1] is %s' % id(numbers[1]))
print('n_num[1] is %s' % id(n_num[1]))
print('c_num[1] is %s' % id(c_num[1]))
print('d_num[1] is %s' % id(d_num[1]))

c_num[1] = 'c'
print('----------------c_num[1]=k------------------')
print('numbers[1] is %s' % id(numbers[1]))
print('n_num[1] is %s' % id(n_num[1]))
print('c_num[1] is %s' % id(c_num[1]))
print('d_num[1] is %s' % id(d_num[1]))

# 如果子对象值相同，地址会相同
c_num[1] = 'k'
if c_num[1] is  numbers[1]:
    print('True')
# print('----------------c_num[1]=k------------------')
# print('numbers[1] is %s' % id(numbers[1]))
# print('n_num[1] is %s' % id(n_num[1]))
# print('c_num[1] is %s' % id(c_num[1]))
# print('d_num[1] is %s' % id(d_num[1]))

d_num[1] = 'd'
print('----------------d_num[1]=k------------------')
print('numbers[1] is %s' % id(numbers[1]))
print('n_num[1] is %s' % id(n_num[1]))
print('c_num[1] is %s' % id(c_num[1]))
print('d_num[1] is %s' % id(d_num[1]))

numbers[2][1] = 'k'
print('----------------numbers[2][1]=k------------------')
print(numbers)
print(c_num)
print(d_num)
print('numbers[2] is %s' % id(numbers[2]))
print('c_num[2] is %s' % id(c_num[2]))
print('d_num[2] is %s' % id(d_num[2]))

# ----------------result---------------------------
# numbers is 3064167050632
# n_num is 3064167050632
# c_num is 3064166945032
# d_num is 3064167050120
# numbers[0] is 140717592597536
# n_num[0] is 140717592597536
# c_num[0] is 140717592597536
# d_num[0] is 140717592597536
# numbers[1] is 140717592597568
# n_num[1] is 140717592597568
# c_num[1] is 140717592597568
# d_num[1] is 140717592597568
# numbers[2] is 3064167096776
# n_num[2] is 3064167096776
# c_num[2] is 3064167096776
# d_num[2] is 3064166988488
# ----------------numbers[1]=k------------------
# numbers[1] is 3064120120968
# n_num[1] is 3064120120968
# c_num[1] is 140717592597568
# d_num[1] is 140717592597568
# ----------------c_num[1]=k------------------
# numbers[1] is 3064120120968
# n_num[1] is 3064120120968
# c_num[1] is 3064119986528
# d_num[1] is 140717592597568
# ----------------d_num[1]=k------------------
# numbers[1] is 3064120120968
# n_num[1] is 3064120120968
# c_num[1] is 3064119986528
# d_num[1] is 3064120033552
# ----------------numbers[2][1]=k------------------
# [1, 'k', [1, 'k', 3]]
# [1, 'c', [1, 'k', 3]]
# [1, 'd', [1, 2, 3]]
# numbers[2] is 2890348646920
# c_num[2] is 2890348646920
# d_num[2] is 2890348545224