#!/usr/bin/env python
#-*- coding:utf-8 -*-

import tkinter as tk
import threading
import spider_main
import html_outputer

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.createUI()

    def createUI(self):
        self.title('嗨,见到你很高兴')
        # 说明Label
        self.infoTitleLable = tk.Label(self, text='欢迎使用图片获取工具')
        self.infoTitleLable.pack(pady='10')
        # 输入框
        e = tk.StringVar()
        self.textEntery = tk.Entry(self, textvariable=e)
        e.set('请输入图片关键字')
        self.textEntery.pack( pady='10')
        # 提交按钮
        self.commitButton = tk.Button(self, text='    提交    ',command=lambda : self.thread_it(self.downloadImages,self.textEntery.get(),self.text))
        self.commitButton.pack( pady='10')

        #
        self.openPath = tk.Button(self, text='打开文件目录',command = self.openFilePath)
        self.openPath.pack(side = tk.BOTTOM,pady='10')
        self.text = tk.Text()
        self.text.pack()
        self.text.insert(tk.END,'此处为下载进度显示框:\r\n')
    def openFilePath(self):
        outPut = html_outputer.HtmlOutputer()
        try:
            outPut.openFilePath()
        finally:
            pass

    def downloadImages(self,keyword,text):
        if keyword is None or keyword =="请输入图片关键字" or len(keyword) == 0:
            return
        text.delete(1.0,tk.END)
        self.text.insert(tk.END, '此处为下载进度显示框:\r\n')
        print('downloading',keyword)
        spider_main.startCraw(keyword,text)


    @staticmethod
    def thread_it(func,*args):
        t = threading.Thread(target=func,args=args)
        t.setDaemon(True)
        t.start()


app = Application()
width ,height= 600, 500
app.geometry('%dx%d+%d+%d'%(width,height,(app.winfo_screenwidth()-width)/2,(app.winfo_screenheight()-height)/2))
app.mainloop()
