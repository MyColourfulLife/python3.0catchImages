#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from urllib import request

class HtmlDownLoader(object):
    def download(self, new_url):
        if new_url is None:
            return
        reg = request.Request(new_url)
        reg.add_header('User-Agent',"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
        response = request.urlopen(reg)
        if response.getcode() != 200:
            return None
        return response.read()