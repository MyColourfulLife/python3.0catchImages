#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import imghdr
import tkinter as tk
import os
from urllib import request
import shutil
import threading
import logging
q = threading.Lock()
class HtmlOutputer(object):

    def __init__(self,text = None):
        self.datas = []
        self.basePath = os.path.dirname(__file__)
        self.basePath = os.path.join(self.basePath,'images')
        self.x = 1
        self.text = text

    def collect_data(self,new_data):
        if new_data is None:
            return
        self.datas.append(new_data)

    def output_html(self):
        file = open('output.html','w')
        file.write('<html>')
        file.write('<body>')
        for data in self.datas:
            file.write(data['url'])
            file.write(data['title'].encode('utf-8'))
            file.writelines(data['lists'])
            file.write("<br>")

        file.write('</body>')
        file.write('</html>')
        file.close()


    def _downloadImage(self,imgurls):
        if imgurls is None or len(imgurls) == 0:
            return
        for url in imgurls:
            path = os.path.join(self.basePath, '%s.png' % self.x)
            opener = request.build_opener()
            opener.addheaders = [('User-Agent',
                                 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")]
            request.install_opener(opener)
            try:
                request.urlretrieve(url,path)
            except BaseException as e:
                logging.exception(e)
                print('HTTP error：', url)
            if self.x > 100:
                print ('done')
                return
            expand = os.path.splitext(path)[1]
            if expand == '.png':
                self.text.insert(2.0, '正在下载第%d张图片\r\n' % self.x)

                self.x += 1
                # if imghdr.what(path):
                #   #  q.acquire()
                #     print ('正在下载第%d张图片' % self.x)
                #     self.x += 1
                #    # q.release()
                # else:
                #     os.remove(path)
        print ('done')


    def downloadImages(self):
        shutil.rmtree(self.basePath,True)
        os.mkdir(self.basePath)
        tempSet = set()
        for data in self.datas:
            tempSet = tempSet | data['lists']
        try:
            self._downloadImage(tempSet)
        except BaseException as e:
            logging.exception(e)
        print(self.basePath)
        os.system('start %s' % self.basePath)

    def openFilePath(self):
        os.system('start %s' % self.basePath)
