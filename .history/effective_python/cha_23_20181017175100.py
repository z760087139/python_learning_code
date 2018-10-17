# this chapter is about hook
# such as the hook in defaultdict,if you want to count the null ask
# but the most effective is the using about __call__()
# example 1:
import collections
def func_outer(default_value,dict,*args):
    count_num = 0
    def func_in(default_value):
        count_num += 1
        return default_value
    result = collections.defaultdict(func_in,dict)
    # try .. args
    return result,count_num
# this way you need to get the count_num in function


# example 2:
import collections
class func_default():
    def __init__(self,default_value):
        self.count_num = 0
        self.value = default_value
    def __call__(self):
        self.count_num += 1 
        return (self.value)

#this way you can get hte count_num whenever you want
# 
# example 2 output:   
# 
default_value = 1
dict = {'red':1,'blue':2}
func = func_default(default_value)
print func.count_num
result = collections.defaultdict(func,dict)
count = func.count_num
print func.count_num
result['k']
print result
print func.count_num