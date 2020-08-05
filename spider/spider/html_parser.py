# coding:utf-8

from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):
  # DOM parser, HTML 解析器 html_parser
  def parse(self, page_url, html_cont):
    if page_url is None or html_cont is None:
      return
    # HTML 解析, bs4
    soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
    new_urls = self._get_new_urls(page_url, soup)
    new_data = self._get_new_data(page_url, soup)
    return new_urls, new_data
  #
  def _get_new_urls(self, page_url, soup):
    new_urls = set()
    # 正则表达式, re
    # view/123.htm
    links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
    for link in links:
      new_url = link['href']
      # URL 拼接, urlparse
      new_full_url = urlparse.urljoin(page_url, new_url)
      new_urls.add(new_full_url)
    return new_urls
  #
  def _get_new_data(self, page_url, soup):
    # dict 字典
    res_data = {}
    # URL
    res_data['url'] = page_url
    # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
    # title 标题
    title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
    res_data['title'] = title_node.get_text()
    # <div class="lemma-summary"
    # summary 摘要
    summary_node = soup.find('div', class_="lemma-summary")
    res_data['summary'] = summary_node.get_text()
    return res_data

