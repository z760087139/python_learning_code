import numpy as np
import matplotlib.pyplot as plt

# 生成 x,y 数据
x = np.arange(0 , 6 , 0.1)
y = np.sin(x)

# plt.plot(x,y)
# plt.show()

# plot样式
plt.plot(x ,y ,linestyle = '--' ,label = 'sin')   #linestyle 虚线  label 线标题
plt.xlabel ('x')  # x 轴名
plt.ylabel ('y')  # y 轴名
plt.title ('x-y,sin') # 标题名
plt.legend()
plt.show()