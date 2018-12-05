import ibm_db
# conf = {'sid'...}
info = 'DATABASE={sid};HOSTNAME={ip};PROT={port};PROTOCOL=TCPIP;UID={user};PWD={password}'.format(**conf)
)
conn = ibm_db.connect(info,"","")
stmt = ibm_db.exec_immediate(conn,command)
tuple = ibm_db.fetch_tuple(stmt)
while tuple != False
    print tuple[0]
    print tuple[1] 
    tuple = ibm_db.fetch_tuple(stmt)


