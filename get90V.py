#!/usr/bin/python
# -*- coding: UTF-8 -*-

# a py file for get 90 tv
import os
import re

import requests
from bs4 import BeautifulSoup

url = 'https://v.qq.com/x/search/?q=%E6%96%97%E7%BD%97%E5%A4%A7%E9%99%86&stag=0&smartbox_ab='
parseUrl = 'https://jx.parwix.com:4433/player/?url='

def cUrl():
    pass


def resBody():
    session = requests.session()
    res = session.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'lxml')
    vl = soup.find_all(attrs={'class': 'result_title'})
    vl2 = soup.find_all('a', href=re.compile('https://v.qq.com/x/cover/'))
    realUrls = []
    for i in vl2:
        print(i['href'])
        print(i)
    for i2 in vl:
        # print(i2)
        ele = {}
        if len(i2.select('.hl')) > 0:
            # print(i2.select('.hl')[0].text)
            ele['name'] = i2.select('.hl')[0].text
        if len(i2.select('a')) > 0:
            print('链接:'+str(i2.select('a')[0]['href']))
            realUrl = parseUrl+str(i2.select('a')[0]['href'])
            print(realUrl)
            ele['url'] = realUrl
            realUrls.append(ele)
    return realUrls
    # print(vl2)
    pass


def saveFile():
    # fo = open('test2.txt', 'a')
    # print(fo.name)
    # print(fo.mode)
    # print(fo.closed)
    # print(fo.encoding)
    # fo.closed
    # os.rename('test2.txt', 'newtest.txt')
    pass


def removeFile():
    os.remove('newtest.txt')


def newDir():
    os.mkdir('dir')


if __name__ == "__main__":
    urls = resBody()
    print(urls)
