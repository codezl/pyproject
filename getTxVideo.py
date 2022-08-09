#!/usr/bin/python
# a pyhone of video resolve for TXX
# 学习资料

import re
from urllib3 import request
# 外部包
import requests
from bs4 import BeautifulSoup


baseUrl = 'https://v.qq.com/x/search/?q='
parseUrl = 'https://jx.aidouer.net/?url='
videoBaseUrl = 'https://v.qq.com/x/cover'


def searchList(name):
    url = baseUrl + name
    session = requests.session()
    res = session.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'lxml')
    vl = soup.find_all(attrs={'class': 'result_title'})
    vl2 = soup.find_all('a', href=re.compile('https://v.qq.com/x/cover/'))
    resultItemV = soup.find_all(attrs={'class': 'result_item_v'})

    # print(resultItemV)
    realUrls = []

    item = {}
    desc = {}
    # info = {}
    infos = []
    for vitem in resultItemV:
        # 搜索结果图片
        vpic = vitem.select('.figure_pic')
        # print(vpic)
        item['pic'] = vpic[0]['src']
        # 名字、全称
        vtitle = vitem.select('.result_title')
        print(vtitle[0])
        item['title'] = vtitle[0].text
        # 跳转播放链接，要重定向（跳转后地址会变化，使用获取重定向地址方法）
        item['searchUrl'] = vtitle[0].select('a')[0]['href']

        # 其它基本信息
        resultInfo = vitem.select('.result_info')
        infoItem = resultInfo[0].select('.info_item')
        # print(infoItem[-1].select('.desc_text')[0].text)
        # desc['name'] = infoItem[-1].select('.label')[0].text
        desc['name'] = '简介'
        desc['desc'] = infoItem[-1].select('.desc_text')[0].text
        infos.append(desc)
        # 删除最后一个简介
        del infoItem[-1]
        for i in infoItem:
            # print('\n')
            # print(i)
            # print('\n')
            # python也不能在外部定义要加入数组的元素，否则会因为引用指针导致所有匀速为最后添加的元素
            info = {}
            info['name'] = i.select('.label')[0].text
            info['content'] = i.select('.content')[0].text
            infos.append(info)
        print(infos)
    for i in vl2:
        ele = {}
        # print(i['href'])
    for i2 in vl:
        # print("这是i2\n")
        # print(i2)
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


if __name__ == "__main__":
    searchList("斗罗大陆")
