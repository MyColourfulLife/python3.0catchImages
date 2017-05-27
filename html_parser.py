#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import re
import urllib.parse

from bs4 import BeautifulSoup


class HtmlParser(object):
    def __init__(self):
        self.keyword = ''

    def parser(self, new_url, html_content):
        if new_url is None or html_content is None:
            return
        soup = BeautifulSoup(html_content,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(new_url,soup)
        new_data = self._get_new_data(new_url,soup,html_content)
        return new_urls,new_data

    def _get_new_urls(self, page_url, soup):

        # <div id="page">
        new_urls = set()
        baseUrl = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%s&' % self.keyword
        links = soup.find('div', id='page').find_all('a')
        for link in links:
            new_url = link['href']
            p = urllib.parse.urlparse(new_url)
            qsl = urllib.parse.parse_qsl(p.query)

            pnValue = ""
            gsmValue = ""
            for key,value in qsl:
                if key == "pn":
                   pnValue = value
                elif key == 'gsm':
                    gsmValue = value

            new_full_url = baseUrl + 'pn=%s' % str(pnValue) + 'gsm=%s' % str(gsmValue)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, new_url, soup,html_content):
        data = {}
        data['url'] = new_url

        titile_node = soup.find('title')
        data['title'] = titile_node.get_text()

        r = re.compile(r'(http:[^\s]*?\.jpg)')
        #python3 要decode一下
        html_content = html_content.decode('utf-8')
        result = r.findall(html_content)
        # result = re.findall(r,html_content)
        lists = set(result)
        data['lists'] = lists
        return data
