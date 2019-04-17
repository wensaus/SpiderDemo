# -*- coding: utf-8 -*-
__time__ = '2019-04-16 17:12'
__author__ = 'Wensau'

import time
import requests
from bs4 import BeautifulSoup


def get_timestamp():
    t = time.time()
    return int(t)


def get_baidu_pic():
    url = 'http://news.baidu.com/widget?id=PicWall&t=' + str(get_timestamp())
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) '
                            'AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/73.0.3683.103 Safari/537.36'}
    baidu = requests.get(url=url, headers=header)
    return baidu.content.decode('utf8')


def get_pic_title():
    ret = BeautifulSoup(get_baidu_pic())
    pic_title = []
    for x in ret.find_all('div', class_='image-list-wrapper'):
        for y in x.find_all('a'):
            if y.text != '':
                pic_title.append(y.text)
    return pic_title


def get_pic_url():
    ret = BeautifulSoup(get_baidu_pic())
    pic_url = []
    for x in ret.find_all('div', class_='image-list-wrapper'):
        for y in x.find_all('a'):
            for z in y.find_all('img'):
                pic_url.append(z['src'])
    return pic_url
