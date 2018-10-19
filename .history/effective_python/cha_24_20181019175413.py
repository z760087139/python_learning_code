# 关于类继承，多态，@classmethod 构建对象
# 新知识点：

# 1.类继承，super()用法
# super() 函数是用于调用父类(超类)的一个方法。
# super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。

# python3 example:
class A:
    pass
class B(A):
    def add(self, x):
        super().add(x)

# python2 example:
class A(object):   # Python2.x 记得继承 object
    pass
class B(A):
    def add(self, x):
        super(B, self).add(x)

# instance:
class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print ('Parent')
    
    def bar(self,message):
        print ("%s from Parent" % message)
 
class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类B的对象 FooChild 转换为类 FooParent 的对象
        super(FooChild,self).__init__()    #相当于执行了父类FooParent.__init__()
        print ('Child')
        
    def bar(self,message):
        super(FooChild, self).bar(message)
        print ('Child bar fuction')
        print (self.parent)
 
if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')


# 2.MapReduce的拼接方式 & 类继承
class PathInputData():
    def __init__(self,path):
        self.path = path
    
    def read(self):
        return open(self.path).read()


class Worker(object):  #woker类
    def __init__(self,input_data):
        self.input_data = input_data
        self.result = None
    
    def map(self):
        raise NotImplementedError

    def reduce(self):
        raise NotImplementedError

class LineCountWorker(Worker):    #继承woker类，实际也是worker，统计并输出行数
    def map(self):                      # map属于多线程的工作部分，返回该工作流的结果
        data = self.input_data.read()   # 计划输入PathInputData类，并执行read()方法
        self.result = data.count('\n')

    def reduce(self,other):             # reduce用作多线程最后的统计
        self.result += other.result

# 拼接以上的类
# 输入地址，返回PathInputData的迭代器
def generate_inputs(data_dir):      
    import os 
    for name in os.listdir(data_dir)
        yield PathInputData(os.path.join(datra_dir,name))
# 创建worker列表
def create_workers(input_list):
    wokers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return wokers
# 多线程执行woker并统计结果
def execute(wokers):
    from threading import Thread
    threads = [Thread(target=w.map) fro w in workers]
    for thread in threads : thread.start()
    for thread in threads : thread.join()

    first,rest = wokers[0],wokers[1:]
    for worker in rest:
        first.reduce(worker)
    return first.result
# 最终拼接函数
def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)


# 本章要点
# 类的继承和@classmethod 的用法
# @classmethod 实际上是针对  "类对象"  用的方法
# @classmethod 实际上是针对  "类对象"  用的方法
# @classmethod 实际上是针对  "类对象"  用的方法
# 普通的def函数是针对  "类的实例" 用的方法
# 
# 例子查看ex_classmethod.py