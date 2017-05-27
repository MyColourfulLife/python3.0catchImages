#!/usr/local/bin/python
# -*- coding: utf-8 -*-

__author__="黄家树"
 
import html_downloader
import html_outputer
import html_parser
import url_manager
import urllib.parse
import urllib.error
import logging
from tkinter import messagebox

class SpiderMain(object):

    def __init__(self,text):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer(text)

    def craw(self,root_url,keyword):
        self.parser.keyword = keyword
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parser(new_url,html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                print ('craw ', count, new_url)
                if count == 5:
                    break
                count += 1
            except BaseException as error:
                logging.exception(error)
                print ('craw failed')

        # self.outputer.output_html()
        self.outputer.downloadImages()


def startCraw(keyword,text):
    # print('每次至多为您下载100张图片')
    # keyword = input('请输入要抓取的图片:')
    # if keyword is None:
    #     keyword = '图片'
    keyword = urllib.parse.quote(keyword)
    root_url = 'http://image.baidu.com/search/flip?tn=baiduimage&st=-1&ipn=r&ct=201326592&nc=1&lm=-1&cl=2&ie=utf-8&word=%s&ie=utf-8&istype=2&fm=se0' % keyword
    obj_spider = SpiderMain(text)
    obj_spider.craw(root_url, keyword)



# if __name__ == '__main__':
#     print ('每次至多为您下载100张图片')
#     keyword = input('请输入要抓取的图片:')
#     if keyword is None:
#         keyword = '图片'
#     keyword = urllib.parse.quote(keyword)
#     root_url = 'http://image.baidu.com/search/flip?tn=baiduimage&st=-1&ipn=r&ct=201326592&nc=1&lm=-1&cl=2&ie=utf-8&word=%s&ie=utf-8&istype=2&fm=se0' % keyword
#     obj_spider = SpiderMain()
#     obj_spider.craw(root_url,keyword)