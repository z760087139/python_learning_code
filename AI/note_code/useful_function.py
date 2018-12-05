
import numpy as np
import matplotlib.pyplot as plt

# sigmoid function
def sig_func(x):
    return 1/ (1 + np.exp(-5*x))

x = np.arange(-5 , 5 , 0.1)
y = sig_func(x)
plt.plot(x,y)
plt.show()

# 阶跃函数
def setp_function(x):
    return (np.array(x>0,dtype=np.int))
# x = np.arange(-5 , 5, 0.1)
y = setp_function(x)
plt.plot(x,y)
plt.show()
    
# ReLU函数
def relu(x):
    return np.maximum(0,5*x)
# x = np.arange(-5 , 5, 0.1)
y = relu(x)
plt.plot(x,y)
plt.show()


# 输出层函数
# 回归问题一般用恒等   分类问题一般用softmax，但是指数函数存在溢出问题。 可以对指数 a - c ，保持结果不变的情况下减少指数值
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

#  恒等函数 即直接输出

# 求导函数    因为计算机会忽略10**-5 一下小数，所以无法使用真实的求导
def numerical_diff(f,x):
    h = 1e-4
    return (f(x+h)-f(x-h))/(2*h)

# 求导之后，如何根据导数得到切线
def tangent_line(f, x):
    d = numerical_diff(f, x)
    print(d)
    y = f(x) - d*x
    return lambda t: d*t + y

