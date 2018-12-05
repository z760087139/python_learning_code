import traceback
# traceback.print_exc()打印异常信息到标准错误，就像没有获取一样，
# traceback.format_exc()将同样的输出获取为字符串。你可以向这些函数
# 传递各种各样的参数来限制输出，或者重新打印到像文件类型的对象。
def make_raise():
    print('make rasie')
    raise Exception('rasie!')
def func_1():
    try : 
        print('func1')
        print('call make rasie')
        make_raise()
    except:
        raise Exception('change!')

def func_2():
    try :
        print('func2')
        print('call func1')
        # raise Exception('rasie!!')
        func_1()
    except Exception as e :
        print(traceback.format_exc())
    print('finish')
func_2()