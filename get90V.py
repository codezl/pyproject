#!/usr/bin/python
# -*- coding: UTF-8 -*-

# a py file for get 90 tv
import os
import re

import requests
from bs4 import BeautifulSoup
from urllib import request

url = 'https://v.qq.com/x/search/?q=%E6%96%97%E7%BD%97%E5%A4%A7%E9%99%86&stag=0&smartbox_ab='
parseUrl = 'https://jx.aidouer.net/?url='
txVidBaseUrl = 'https://v.qq.com/x/cover'


def cUrl():
    pass


def getRes(baseurl):
    session = requests.session()
    res = session.get(baseurl)
    res.encoding = 'utf-8'
    return res


def resBody(url1):
    session = requests.session()
    res = session.get(url1)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'lxml')
    vl = soup.find_all(attrs={'class': 'result_title'})
    vl2 = soup.find_all('a', href=re.compile('https://v.qq.com/x/cover/'))
    realUrls = []
    for i in vl2:
        print(i['href'])
        print(i)
    for i2 in vl:
        print(i2)
        ele = {}
        if len(i2.select('.hl')) > 0:
            # print(i2.select('.hl')[0].text)
            # ele['name'] = i2.select('.hl')[0].text
            ele['name'] = i2.text
        if len(i2.select('a')) > 0:
            print('链接:' + str(i2.select('a')[0]['href']))
            # realUrl = parseUrl+str(i2.select('a')[0]['href'])
            realUrl = str(i2.select('a')[0]['href'])
            print(realUrl)
            ele['url'] = realUrl
            realUrls.append(ele)
    return realUrls
    # print(vl2)
    pass


# 解析tx
def resolveTxSelectVideo(vUrl):
    # res = getRes('https://v.qq.com/x/cover/mzc00200js3mdvw/q00354i139r.html')
    rewriteUrl = getRewriteUrl(vUrl)
    res = getRes(rewriteUrl)
    soup = BeautifulSoup(res.text, 'lxml')
    listItem = soup.find_all('div', {'class': 'episode-item-rect--number'})
    # print(listItem)
    playUrls = []
    if (len(listItem)) == 0:
        return '未找到数据'
    for item in listItem:
        # print(repr(item.select('span')[0].text))
        playUrl = {}
        playUrl['num'] = item.select('span')[0].text
        playUrl['url'] = txVidBaseUrl + '/' + item['data-cid'] + '/' + item['data-vid'] + '.html'
        # print(playUrl)
        playUrls.append(playUrl)
    # print(playUrls)
    return playUrls


# 获取重定向地址（有些搜索结果点击之后跳转的是重定向地址）
def getRewriteUrl(baseUrl=""):
    # 重定向地址
    # 如果有代理要加代理地址
    # headers = {'User-Agent': 'xx代理'}
    # session = requests.session()
    # res = session.get('https://v.qq.com/x/cover/mzc00200js3mdvw/q00354i139r.html')
    res = requests.get(baseUrl)
    print('重定向1'+res.url)
    return res.url


def getRewriteUel2(baseUrl):
    # 下面方法拿到结果不正确，无效
    rwurl = request.urlopen('https://v.qq.com/x/cover/mzc00200js3mdvw/q00354i139r.html')
    # rwurl = request.urlopen(baseUrl)
    print('重定向2' + rwurl.geturl() + '\n')
    return rwurl.geturl()


# 以下是关于vip解析地址的方法
# 将视频播放地址转换成解析地址
def exchangePlayUrl(baseUrl, vipUrl):
    # vipPlayUrl = vipUrl + baseUrl
    # 暂时用同一个地址
    return parseUrl+baseUrl


def saveFile():
    fo = open('test2.txt', 'a')
    print(fo.name)
    print(fo.mode)
    print(fo.closed)
    print(fo.encoding)
    fo.closed
    os.rename('test2.txt', 'newtest.txt')
    pass


def removeFile():
    os.remove('newtest.txt')


def newDir():
    os.mkdir('dir')


if __name__ == "__main__":
    urls = resBody('https://v.qq.com/x/search/?q=%E6%96%97%E7%BD%97%E5%A4%A7%E9%99%86&stag=0&smartbox_ab=')
    print(urls)
    # resolveTxSelectVideo('https://v.qq.com/x/cover/m441e3rjq9kwpsc') # 没.html结尾时会警告
    getRewriteUrl('https://v.qq.com/x/cover/m441e3rjq9kwpsc.html')
    resolveTxSelectVideo('https://v.qq.com/x/cover/m441e3rjq9kwpsc.html')
