# coding:utf8

__author__ = 'xgqfrms'
__editor__ = 'vscode'
__version__ = '1.0.1'
__copyright__ = """
  Copyright (c) 2012-2050, xgqfrms; mailto:xgqfrms@xgqfrms.xyz
"""

# Python 2.7 version
import urllib2

# Python 3.7 version
# import urllib

import cookielib

# url = "https://rollbar.com/docs/"

# url = "https://cdn.xgqfrms.xyz/json/"

# url = "http://cdn.xgqfrms.xyz/json/"

url = 'http://baike.baidu.com/view/21087.htm'

# urllib2.HTTPError: HTTPs Error 403: Forbidden

# HTTPs Error 403: Forbidden

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
