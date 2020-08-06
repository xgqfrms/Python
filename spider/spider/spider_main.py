# coding:utf8

# 导入整个模块
import logging

import url_manager
import html_downloader
import html_parser
import html_outputer
# import url_manager, html_downloader, html_parser, html_outputer

# 导入部分模块
# from spider import url_manager
# from spider import html_downloader
# from spider import html_parser
# from spider import html_outputer

# import group modules
# from spider import url_manager, html_downloader, html_parser, html_outputer

# from url_manager import UrlManager
# from html_downloader import HtmlDownloader
# from html_parserimport HtmlParser
# from html_outputer import HtmlOutputer


class SpiderMain(object):
  # 构造函数 初始化
  def __init__(self):
    # urls 管理
    self.urls = url_manager.UrlManager()
    # html 下载
    self.downloader = html_downloader.HtmlDownloader()
    # html 解析
    self.parser = html_parser.HtmlParser()
    # html 输出结果
    self.outputer = html_outputer.HtmlOutputer()
  # function
  def craw(self, root_url):
    # 计数
    count = 1
    self.urls.add_new_url(root_url)
    while self.urls.has_new_url():
      try:
        new_url = self.urls.get_new_url()
        print 'craw %d:%s' %(count,new_url)
        html_cont = self.downloader.download(new_url)
        new_urls,new_data = self.parser.parse(new_url,html_cont)
        self.urls.add_new_urls(new_urls)
        self.outputer.collect_data(new_data)
        print new_data['title']
        #
        if count == 10:
          break
        count = count + 1
      # except Exception, e:
      except Exception as e:
        logging.exception(e)
        print 'craw failed' + e
    self.outputer.output_html()
    print 'finished'

# main 程序的入口
if __name__ == '__main__':
  # 实例化
  obj_spider = SpiderMain()
  root_url = 'http://baike.baidu.com/view/21087.htm'
  # 启动 crawler
  obj_spider.craw(root_url)
