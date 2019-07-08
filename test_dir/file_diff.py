# python 3

# '\x1b'分隔的第一个字段 存在文件 a 但不存在文件 b 的内容写到result.txt中

import re 
import linecache

# 获取文件中的集合 和 保留每一行第一个字段值到list
def get_set(file_path):
    # 正则表达式
    pa = re.compile(r'(\x1b)?(?P<u>.*?)\x1b')
    with open(file_path,'rb') as f1:
        # 预计返回集合 set_a
        set_a = set()
        list_a = []
        for line in f1:
            # 需要知道文件编码 ascii/utf-8/unicode....
            # python 正则需要str 类型，decode 之后正则获取第一个\x1b间隔的内容，分组名u
            k = pa.search(line.decode(coding)).group('u')
            # 加到集合中
            set_a.add(k)
            # 或者保存当前第一个字段的值,用于后面回差索引用,如果差异少的话可以直接遍历文件查
            list_a.append(k)
        f1.close()
    return set_a,list_a

# 根据差集，读取文件中的该行内容
def get_line(file_path,list_b,diff_set):
    while diff_set:
        k = diff_set.pop()
        yield linecache.getline(file_path,list_b.index(k)+1)
# 文件编码
coding = 'ascii'
# 文件路径 绝对路径
a_file_path = 'F:\\code\\dmm_mail\\a1.txt'
b_file_path = 'F:\\code\\dmm_mail\\b1.txt'
# 获取集合a, b内容
set_a,list_a = get_set(a_file_path)
set_b,_ = get_set(b_file_path)
# 存在a中，但不存在b中的差集
diff_set = set_a - set_b
# 将内容写到result.txt中
with open('result.txt','wb') as f:
    num = len(diff_set)
    cur_num = 0
    while diff_set:
        # 每 5% 打印一次进度
        cur_num += 1
        if (cur_num / num) * 100 % 5 == 0:
            print(cur_num/num)
        k = diff_set.pop()
        f.write(linecache.getline(a_file_path,list_a.index(k)+1).encode(coding))
    f.close()

