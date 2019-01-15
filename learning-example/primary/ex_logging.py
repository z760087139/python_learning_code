import logging
import time
# logging 主要包括下面几个类
# logging.Logger    
# logging.Formatter
# logging.Handler
# 其余还有 logging.Filter,logging.LogRecord

# logging 等级
# debug < info < warning < error < critical

# 日志等级设置 NOTSET 为所有等级都显示
# logging.basicConfig(level=logging.NOTSET) 
# logging.setLevel() 也可以

# 日志打印
# logging.debug('some info')

# 日志格式
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# 实际使用时需要创建logger
# loggername = 'name'
# logger = logging.getLogger(loggername)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
# 创建handler 输出到文件
name_time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
log_name = name_time.join('.log')
fh = logging.FileHandler(log_name,mode='w')
fh.setLevel(logging.DEBUG)
# 创建handler 输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# 输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# 将handler 加到 logger
logger.addHandler(fh)
logger.addHandler(ch)
# 日志打印
logger.debug('debug level info')  # 不会记录到文件中，因为logger等级是info
# logger 只发送info等级或以上的  handler记录debug或以上的数据 
logger.info('info level info')
# 异常出入
# try: ...
# except Exception,e:
#   logger.error('message',exc_info=True)


# 输出格式
# %(levelno)s：打印日志级别的数值
# %(levelname)s：打印日志级别的名称
# %(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
# %(filename)s：打印当前执行程序名
# %(funcName)s：打印日志的当前函数
# %(lineno)d：打印日志的当前行号
# %(asctime)s：打印日志的时间
# %(thread)d：打印线程ID
# %(threadName)s：打印线程名称
# %(process)d：打印进程ID
# %(message)s：打印日志信息

# 消息等级  用于设置等级时用，或者用logging.INFO等代替
# Level	     Numeric value
# CRITICAL	 50
# ERROR	     40
# WARNING	 30
# INFO	     20
# DEBUG	     10
# NOTSET	  0