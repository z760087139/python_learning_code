import json
import datetime
# make json object:
pydata = {'data':[1,2,3,4,5],'time':datetime.datetime.now().strftime('%F')}
jdata = json.dumps(pydata)

# if pydata has chinese string
# jdata = json.dumps(pydata,ensure_ascii=False)

# read json object:

redata = json.loads(jdata)  
