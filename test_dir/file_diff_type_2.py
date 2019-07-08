import re
import datetime
start_time = datetime.datetime.now()
a_file_path = 'a1.txt'
b_file_path = 'b1.txt'
coding = 'ascii'
pa = re.compile(r'(\x1b)?(?P<u>.*?)\x1b')
with open(a_file_path,'rb') as f:
    # 获取文件中的集合 和 保留每一行第一个字段值到list
    # 正则表达式
    # 预计返回集合 set_a
    set_a = set()
    # list_a = []
    for line in f:
        # 需要知道文件编码 ascii/utf-8/unicode....
        # python 正则需要str 类型，decode 之后正则获取第一个\x1b间隔的内容，分组名u
        k = pa.search(line.decode(coding)).group('u')
        # 加到集合中
        set_a.add(k)
        # list_a.append(k)

with open('result.txt','wb') as r:
    with open(b_file_path,'rb') as f:
        for line in f:
            k = pa.search(line.decode(coding)).group('u')
            if k not in set_a:
                r.write(line)
        f.close()
    r.close()
end_time = datetime.datetime.now()

delta_time = end_time - start_time
print(delta_time)
