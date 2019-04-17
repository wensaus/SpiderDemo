# -*- coding: utf-8 -*-
__time__ = '2019-04-16 10:58'
__author__ = 'Wensau'

import time
import requests
from bs4 import BeautifulSoup


def get_timestamp():
    t = time.time()
    return int(t)


def get_baidu():
    url = 'http://news.baidu.com/'
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) '
                            'AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/73.0.3683.103 Safari/537.36'}
    baidu = requests.get(url=url, headers=header)
    return baidu.content.decode('utf8')


def get_news_url():
    ret = BeautifulSoup(get_baidu())
    urls = []
    for x in ret.find_all('div', class_='hotnews'):
        for y in x.find_all('a'):
            urls.append((y['href']))
    return urls


def get_news_title():
    ret = BeautifulSoup(get_baidu())
    titles = []
    for y in ret.find_all('div', class_='hotnews'):
        for y in y.find_all('a'):
            titles.append(y.text)
    return titles


def get_new_body(url):
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) '
                            'AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/73.0.3683.103 Safari/537.36'}
    html_body = requests.get(url=url, headers=header)
    ret = BeautifulSoup(html_body.content)
    text = []
    for m in ret.find_all('p'):
        text.append(m.text)
    return text
