# 类的继承和@classmethod 的用法
# @classmethod 实际上是针对  "类对象"  用的方法
# @classmethod 实际上是针对  "类对象"  用的方法
# @classmethod 实际上是针对  "类对象"  用的方法
# 普通的def函数是针对  "类的实例" 用的方法
# 
# @classmethod 一般用途 ：
# 1.通过类对象的方法返回该类的实例  
# 2.需要在实例化前使用部分类的方法
#  
# 注意一下例子
class part1(object):
    def __init__(self,name):
        self.name = name

    @classmethod
    def create(cls,par1):
        k = cls.func1(cls,par1)
        b = cls('a')
        cls.result = b.func1(k)
        return b 

    def func1(self,b):
        b += 3
        return b

class part2(part1):
    def func1(self,a):
        a += 1
        return a

b = part2.create(1)
print(b)
# 运行结果
# b有两个属性 result = 3 和 name = a
c = part2.create(20)
print(c)
# 到该步骤
# b.name = a, b.result = 22, c.result= 22  b.result 发生变化 因为当前result 是类part2.result  part2.result 因为c调用create发生变化
b.result = 6
print(b)
# 到该步骤
# b.name = a, b.result = 6, c.result=22  b.result 发生变化 当前b.result已不是part2.result
a = part2.create(10)
print(a)
# 到该步骤
# b.name = a, b.result = 6, c.result=12 ,a.result=12 c.result 发生变化 当前c.result和a.result相同,都是part2.result

# 关于@classmethod语法
class part3(object)