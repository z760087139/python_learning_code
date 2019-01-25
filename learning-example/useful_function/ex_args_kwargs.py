# def func(**kwargs) 将末尾部分用 a = 1 形式的传参以字典形式保存起来  kwargs = {}
# def func(*args) 将位置参数以外部分，非 a = 1 形式传参的 以 元组形式保存   args = ()

# dict_a = {'a':1,'b':2,'2':3}
# tup_a = ('a','b','c')
# func(**dict_a)  实际是将 dict_a 拆分成 a = 1, b =2 , '2' = 3 的形式传到 func中。用这种形式传参需要注意变量名对应关系
# func(*tup_a)   实际是将tup_a 拆分成 'a','b','c' 作为位置参数输入。 注意传入是的位置参数数量是否对应
# func(*ditc_a)  实际是将dict_a.keys() 作为位置参数传入，不常用

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