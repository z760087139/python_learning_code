import numpy as np
# 创建数组
A = np.array([[1,2],[3,4]])
print(A)

# 广播   只能广播一维数组
B = np.array([[1,2]])
print(A*B)

# 查看数组结构
A.shape  # return (rows,columns)

# 访问元素
X = np.array([[1,2],[3,4],[5,6]])
# 取第N行  0开始  
n = 1
print(X[n])
# N行M列
m = 1
print(X[n][m])

# 转一维数组   (不是列表)
Y = X.flatten()
print(Y)
# 同时取多个元素
Y[np.array([2,3])]

X[np.array([ [0,2] , [1,0] ] )]


# e 的表示方式
# np.exc(x)  = e 的 x 次方

# 点积  np.dot(x,y)  
x = np.array([[1,2],[3,4],[5,6]])
y = np.array([4,5])
z = np.dot(x,y)

a = {'a': 1}
b = {'b': 1}
x = np.array([a,b])

# 取随机数组
random_array = np.random.choice(6000,10) #从0到5999 随机取10个数
