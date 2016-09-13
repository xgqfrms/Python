import urllib2

__author__ = 'xray'
# coding: utf8


class HtmlDownloader(object):
    def __init__(self):
        self

    def download(self, url):
        if url is None:
            return None

        response = urllib2.urlopen(url)
        if response.getcode() !=200:
            return None
        return response.read()