# coding:utf8
__author__ = 'xray'
import urllib2
import cookielib

url = "https://rollbar.com/docs/"

print '第一种方法'
response1 = urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())

print '第二种方法'
request = urllib2.Request(url)
request.add_header("user-agent", "Mozilla/5.0")
response2 = urllib2.urlopen(request)
print response2.getcode()
print response2.read()

print '第三种方法'
cj = cookielib.CookiJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print response3.getcode()
print cj
print response3.read()