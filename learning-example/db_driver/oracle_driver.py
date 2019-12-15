import cx_Oracle
host = '192.168.3.120/orclpdb'
pool = cx_Oracle.SessionPool(
    'bbs',
    'zeng123',
    host,
    encoding='utf-8',
    min=2,
    max=5,
    getmode=cx_Oracle.SPOOL_ATTRVAL_WAIT
)

conn = pool.acquire()
cursor = conn.cursor()
sql = 'select 1 from dba_tables'
cursor.execute(sql)
record = cursor.fetchall()
print(record)

