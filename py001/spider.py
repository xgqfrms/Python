__author__ = 'xray'
import re
import requests

# read html code
# f = open('html\\source.txt', 'r')
f = open('source.txt', 'r')
# read URL

html = f.read()
f.close()

# match pictures
pic_url = re.findall('img src="(.*?)" class="lessoning"', html, re.S)
# http://a1.jikexueyuan.com/home(.*?).jpg
i = 0
for each in pic_url:
    print 'now downloading:' + each
    pic = requests.get(each)
    fp = open('pic\\' + str(i) + '.jpg', 'wb')
    fp.write(pic.content)
    fp.close()
    i += 1