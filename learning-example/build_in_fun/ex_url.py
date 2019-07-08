import urllib
import urllib2

url = 'http://www.baidu.com'
# GET 
req = urllib2.Request(url)
res_data = urllib2.urlopen(req)
res = res_data.read()

# POST
test_data = {'user':111}
test_data_urlcode = urllib.urlencode(test_data)
req = urllib2.Request(url = requrl,data = test_data_urlencode)
res_data = urllib2.urlopen(req)
res = res_data.read()

# cookie
import cookielib
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
res = opener.open('http://www.baidu.com')
for item in cookie:
    print ('name = ' + item.name)
    print ('value = '+ item.value)

