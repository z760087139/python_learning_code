import numpy as np

"""
AND gate 
X1   X2   Y
---- ---- ----
0    0    0
1    0    0           
0    1    0
1    1    1

NAND gate 
X1   X2   Y
---- ---- ----
0    0    1
1    0    1   
0    1    1
1    1    0

OR gate
X1   X2   Y
---- ---- ----
0    0    1
1    0    1   
0    1    1
1    1    0

XOR gate
X1   X2   Y
---- ---- ----
0    0    0
1    0    1   
0    1    1
1    1    0


"""
# AND gate
def AND(x1,x2):
    x = np.array([x1 , x2])
    w = np.array([0.5 , 0.5])
    b = -0.7
    if np.sum(w*x)+b <= 0:
        return 0
    else:
        return 1

# NAND gate
def NAND(x1,x2):
    x = np.array([x1 , x2])
    w = np.array([-0.5 , -0.5])   # w 和 b 取负值
    b = 0.7
    if np.sum(w*x) + b <= 0:
        return 0
    else :
        return 1 

# OR gate
def OR (x1 , x2):
    x = np.array([x1 , x2])
    w = np.array([0.5 , 0.5])   # b 小于任意一个 w
    b = -0.2
    if np.sum(w*x) + b <= 0:
        return 0
    else :
        return 1 

# XOR gate
def XOR (x1, x2):
    s1 = OR(x1,x2)
    s2 = NAND(x1, x2)
    if AND(s1,s2):
        return 1
    else :
        return 0

