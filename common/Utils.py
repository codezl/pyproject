# a utils py file
# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup


# 获取
def getRewriteUrl(baseUrl=""):
    # 重定向地址(选择搜素的地址时要使用)
    # 如果有代理要加代理地址
    # headers = {'User-Agent': 'xx代理'}
    # session = requests.session()
    # res = session.get('https://v.qq.com/x/cover/mzc00200js3mdvw/q00354i139r.html')
    res = requests.get(baseUrl)
    print('重定向1'+res.url)
    return res.url


def getBs4Res(url):
    session = requests.session()
    res = session.get(url)
    res.encoding = 'utf-8'
    bs4Res = BeautifulSoup(res.text, 'lxml')
    return bs4Res


def postBs4Res():
    pass


