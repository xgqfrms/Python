__author__ = 'xray'

# coding: gbk
from wiki_baike import url_manager, html_downloader, html_parser, html_outputer\



class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()  # url管理器
        self.downloader = html_downloader.HtmlDownloader()  # url下载器
        self.parser = html_parser.HtmlParser()  # 解析器
        self.outputer = html_outputer.HtmlOutputer()  # 输出器

    def craw(self, root_url):
        count = 1  # 记录当前爬取的是第几个url
        self.urls.add_new_url(root_url)  # 将入口url添加进url管理器
        while self.urls.has_new_url():  # url管理器中有待爬取的
            try:
                new_url = self.urls.get_new_url()  # 获取待爬取的url
                print 'craw %d:%s' % (count, new_url)
                html_cont = self.downloader.download(new_url)  # 用下载器下载url页面保存到hrml——cont中
                new_urls, new_data = self.parser.parse(new_url, html_cont)  # 解析器获得新的url管理器
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)  # 收集数据
                print new_data['title']
                if count == 10:
                    break
                count += 1

            except Exception, e:
                print e
                print 'craw failed'
        self.outputer.output_html()  # 输出收集好的数据
        print 'ok'
if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)  # 启动爬虫
