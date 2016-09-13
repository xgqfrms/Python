__author__ = 'xray'
# coding: utf8
from bs4 import BeautifulSoup
import re, urlparse


class HtmlParser(object):
    # def __init__(self):
    #     self

    def get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/view/\d+\.html'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls


    def get_new_data(self, page_url, soup):
        res_data = {}
        #
        res_data['url'] = page_url
        #
        title_node = soup.find('dd', class_='LemmaWgt-LemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()
        #
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self.get_new_urls(page_url, soup)
        new_data = self.get_new_data(page_url, soup)
        return new_urls, new_data

