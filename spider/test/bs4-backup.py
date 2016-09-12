__author__ = 'xray'
# coding: utf8
import bs4
# print bs4
from bs4 import BeautifulSoup

# 根据HTML网页字符串,创建 BeautifulSoup 对象
soup = BeautifulSoup(
    html_doc,
    'html.parser',
    from_encoding='utf8'
)
# HTML文儅字符串
# HTML解析器
# HTML文儅的編碼
# ？ 輸入法 ，繁體字

# 搜索節點(find_all,find)
##
soup.find_all('a')
##
soup.find_all('a', href = '/view/123.html')

re = 're'

soup.find_all('a', href = re.compile(r'/view/\d+\.html'))
##
soup.find_all('div', class_ = 'abc', string='Pthon')

# 訪問節點
##
node.name
##
node['href']
##
node.get_text()