__author__ = 'xray'
# coding: utf8
import bs4
import re
# print bs4
from bs4 import BeautifulSoup

# 根据HTML网页字符串,创建 BeautifulSoup 对象
soup = BeautifulSoup(
    html_doc,
    'html.parser',
    from_encoding='utf8'
)
# HTML文档字符串
# HTML解析器
# HTML文档的编码
# ？ 输入法 ，繁体字

# 搜素节点(find_all,find)
##
soup.find_all('a')
##
soup.find_all('a', href='/view/123.html')

re = 're'

soup.find_all('a', href=re.compile(r'/view/\d+\.html'))
##
soup.find_all('div', class_='abc', string='Python')

# 访问节点
##
node = 'node'
node.name = soup.find_all('a', href=re.compile(r'/view/\d+\.html')) 
##
node['href'] = soup.find_all('a', href=re.compile(r'/view/\d+\.html'))
##
node.get_text()
