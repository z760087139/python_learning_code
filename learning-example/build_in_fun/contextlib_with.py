# contextlib 在3.x版本增加了相当多的函数
# python2 只有contextmanager,closing

# contextmanager用法
# 与with 对比
# with:
# with 语句块想要返回的as 内容需要在 __enter__语句部分实现
# 结束时执行的语句在 __exit__ 部分实现
class Par(object):
    def __init__(self,db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.conn.close()
        if exc_val:
            raise

db = 'name'
with Par(db) as conn:
    cursor = conn.cursor()

# contextmanager:
# 通过yield 返回函数的结果给as 后的对象，执行完with 后的语句块后继续执行yield后续代码
# yield 前的部分相当于__enter__   yield 后的相当于 __exit__
from contextlib import contextmanager
@contextmanager
def file_open(path):
    try :
        f_obj = open(path,'w')
        yield f_obj
    except OSError:
        print('We had an error')
    finally:
        print('Closing file')
        f_obj.close()

# closing


path  = 'text.txt'
with file_open(path) as obj:
    obj.write('Testing context managers')

# 重定向标准输出   将屏幕内容输出到文件中
# 普通方式:
import sys
file_path = 'test.txt'
with open(file_path,'w') as obj:
    sys.stdout = obj
    # some output command
    help(sum)

# contextlib 方式  python3.x：
from contextlib import redirect_stdout
file_path = 'test.txt'
with open(file_path,'w') as fobj:
    with redirect_stdout(fobj):
        help(sum)

