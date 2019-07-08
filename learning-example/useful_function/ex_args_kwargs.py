# * 常见用法
# 1. * 和 ** 向函数传递参数
# 2. * 和 ** 捕获被传递到函数中的参数
# 3. * 接受只包含关键字的参数
# 4. * 元组解包时捕获项
# 5. * 迭代项解压到列表/元组
# 6. **字典解压到其他字典

# def func(**kwargs) 将末尾部分用 a = 1 形式的传参以字典形式保存起来  kwargs = {}
# def func(*args) 将位置参数以外部分，非 a = 1 形式传参的 以 元组形式保存   args = ()

# dict_a = {'a':1,'b':2,'2':3}
# tup_a = ('a','b','c')
# func(**dict_a)  实际是将 dict_a 拆分成 a = 1, b =2 , '2' = 3 的形式传到 func中。用这种形式传参需要注意变量名对应关系
# func(*tup_a)   实际是将tup_a 拆分成 'a','b','c' 作为位置参数输入。 注意传入是的位置参数数量是否对应
# func(*ditc_a)  实际是将dict_a.keys() 作为位置参数传入，不常用


# 用作传参时：
# 星号将 可迭代对象拆分 并分别作为函数参数传参
# 调用函数时， *运算符可用于将一个迭代项解压到函数调用的参数中：
a_list = ['apple','banana','lemon']
# print(a[0],a[1],a[2]) 等价于
print(*a_list)

# 将一个数组转置
b_list = [
    [1,4,7],
    [2,5,8],
    [3,6,9]
    ]
def transpose_list(lists):
    return [
        list(x)
        for x in zip(*lists)
    ]
new_b_list = transpose_list(b_list)

# 用作接收参数时
# * 捕获传递给函数的位置参数，捕获后存储在一个元组中
from random import randint
def roll(*dice):
    retrun sum(randint(1,die) for die in dice)
roll(6,6)

# ** 捕获关键字，捕获后存储在一个字典中
def tag(tag_name,**kwargs):
    attri_list = [
        '{name}="{value}"'
        for name,value in attri_list.items()
    ]
    return '<{tag_name}'


dict_a = {'a': 1, 'b': 2}
tup_a = ('a','b','c')
def func_1(**kwargs):
    try:
        print('**kwargs - print kwargs with func_1(**dict_a) :\n%s' % kwargs)
        # print('**kwargs - print **kwargs with func_1(**dict_a) :\n%s' % **kwargs)
    except Exception as e:
        print('**kwargs - print kwargs with func_1(dict_a) will raise error\n')
        print(repr(e))


def func_2(**kwargs):
    print('**kwargs - print kwargs with func_2(c = 1,d = 2):\n%s' % kwargs)

def func_3(**kwargs):
    print(*kwargs)
    test = **kwargs
def func_3(**args):



def func2(c,b,a):
    print(c)
    print(b)
    print(a)