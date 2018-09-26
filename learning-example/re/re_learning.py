import re
key = """select * from (select dbid,alias from account) a,
dbid b where a.alias = (select alias from table3) 
and b.alias = (select alias from table4)"""
p1 = re.compile(r'(?is)(Select.*?from)')
p2 = re.compile(r'(?is)(select.*?from).*?(select.*?from)')
m1 = re.findall(p1,key)
m2 = re.findall(p2,key)
print m1
print m2 
