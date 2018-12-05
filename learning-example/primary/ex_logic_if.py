k = 0
print(k)
k |= 1
pritn(k)
k |= 2
print(k)
k |= 3
print(k)

# using:
k = 0
if flag_1 = True:
    k|=1
if flag_2 = True:
    k|=2
if flag_3 = True:
    k|=4
type = {
    0:'type0'
    1:'type1',
    2:'type2',
    3:'type1+type2',
    4:'type3',
    5:'type1+type3',
    6:'type2+type3',
    7:'type1+type2+type3'
    }
return (type[k])