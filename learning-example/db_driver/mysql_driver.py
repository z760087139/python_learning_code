
import mysql.connector
import mysql.connector.pooling

cnx = mysql.connector.connect(user='scott', password='password',
                              host='127.0.0.1',
                              database='employees')
# cnx.close()

# OPTIONS:
# user                      (username*)		    The user name used to authenticate with the MySQL server.
# password                  (passwd*)		    The password to authenticate the user with the MySQL server.
# database                  (db*)		        The database name to use when connecting with the MySQL server.
# host	                    127.0.0.1	        The host name or IP address of the MySQL server.
# port	                    3306	            The TCP/IP port of the MySQL server. Must be an integer.
# unix_socket		                            The location of the Unix socket file.
# auth_plugin		                            Authentication plugin to use. Added in 1.2.1.
# use_unicode	            True	            Whether to use Unicode.
# charset	                utf8	            Which MySQL character set to use.
# collation	                utf8_general_ci	    Which MySQL collation to use.
# autocommit	            False	            Whether to autocommit transactions.
# time_zone		                                Set the time_zone session variable at connection time.
# sql_mode		                                Set the sql_mode session variable at connection time.
# get_warnings	            False	            Whether to fetch warnings.
# raise_on_warnings	        False	            Whether to raise an exception on warnings.
# connection_timeout        (connect_timeout*)	Timeout for the TCP and Unix socket connections.
# client_flags		                            MySQL client flags.
# buffered	                False	            Whether cursor objects fetch the results immediately after executing queries.
# raw	                    False	            Whether MySQL results are returned as is, rather than converted to Python types.
# consume_results	        False	            Whether to automatically read result sets.

# execute a prepared statement
# prepared cursor is a class
cursor = cnx.cursor(prepared=True)

# execute a SQL
sql1 = 'select * from test.test1 where id = %s' 
id1 = 123
cursor.execute(sql1,id1)
# cursor.fetchall()
# cursor.fetchone()
# cnx.commit()

# get dictionary
dict_cur = cnx.cursor(dictionary=True)
# insert 
# execut many
sql2 = 'insert into test.test1 (name,number) values(%s,%s)'
par2 = [('asdf',321),('zxcv',213)]
cursor.executmany(sql2,par2)
# cnx.commit()

#execut as python format
sql3 = 'insert into test.test1 (name,number) values(%(name)s,%(number)s)'
par3 = {'name':'fds','number':312}
cursor.excute(sql3,par3)
# cnx.commit()

# input datetime
# input_day = datetime.datetime.now().date() + timedelta(day=1)
# data = {'insert_timestamp':input_day}

# create connection pool
dbconfg = {
    "database": "test",
    "user":     "joe",}
mypool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "mypool",
                                                      pool_size = 3,
                                                      **dbconfig)

#close
cursor.close()
cnx.close()