# -*- coding: utf-8 -*-
import urllib2
import cookielib

url = 'http://blog.csdn.net/crazy1235'

# print '方式1'
#
# response1 = urllib2.urlopen(url)
# print response1.getCode()
# print len(response1.read())
# print response1.read()

print '方式2'

request = urllib2.Request(url)
request.add_header("user-agent", "Mozilla/5.0")
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())
print response2.read()

print '方式3'

cookieJar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print response3.getcode()
print len(response3.read())
print response3.read()
