#!/usr/bin/python
# -*- coding: UTF-8 -*-
# a pyhone of video resolve for TXX
# 学习资料

import re
from urllib3 import request
# 外部包
import requests
from bs4 import BeautifulSoup
from common.Utils import getRewriteUrl, getBs4Res


baseUrl = 'https://v.qq.com/x/search/?q='
parseUrl = 'https://jx.aidouer.net/?url='
videoBaseUrl = 'https://v.qq.com/x/cover/'


def searchList(name):
    url = baseUrl + name
    session = requests.session()
    res = session.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'lxml')
    resultItemV = soup.find_all(attrs={'class': 'result_item_v'})

    # print(resultItemV)
    realUrls = []

    itemList = []
    for vitem in resultItemV:
        item = {}
        desc = {}
        # info = {}
        infos = []
        # 搜索结果图片
        vpic = vitem.select('.figure_pic')
        # print(vpic)
        item['pic'] = vpic[0]['src']
        # 名字、全称
        vtitle = vitem.select('.result_title')
        # print(vtitle[0])
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
            # python也不能在外部定义要加入数组的元素，否则会因为引用指针导致所有匀速为最后添加的元素
            info = {}
            info['name'] = i.select('.label')[0].text
            info['content'] = i.select('.content')[0].text
            infos.append(info)
        # print(infos)
        # 视情况放入第一集链接（有些结果无剧集列表）
        playlist = vitem.select('._playlist')[0].select('.item')
        print(playlist)
        playUrls = []
        # for index in range(1, len(playlist)):
        # 获取搜索结果中的播放列表主要信息装入数组(可以等用户点击播放后再分析播放页查看)
        for playI in playlist:
            playItem = {}
            detail = playI.select('a')[0]
            playItem['url'] = detail['href']
            playItem['index'] = detail.text
            # print(playItem)
            playUrls.append(playItem)

        # 加入一条搜索结果到数组
        item['infos'] = infos
        item['playUrls'] = playUrls
        itemList.append(item)

    print(itemList)
    return itemList


# 点击搜索结果播放时，如果是点击剧集列表的链接则不需要（有些结果无剧集列表）
# 获取剧集连接的重定向连接、重定向到第一集
def rewriteUrl(url):
    return getRewriteUrl(url)


# 当用户第一次进入播放页时，获取播放页中的播放列表信息
# 根据重定向地址，解析网页获取剧集
def getPlayListByPage(playUrl):
    # 测试地址:斗罗大陆第一集
    playUrl = 'https://v.qq.com/x/cover/m441e3rjq9kwpsc/m00253deqqo.html'
    soup = getBs4Res(playUrl)
    # 获取到侧边栏 剧集
    episodeList = soup.select('.episode-list')[0]
    # mainTab = episodeList.select('.episode-list__main-tab')
    bTab = episodeList.select(".b-tab")[0]
    bTabItem = bTab.select('.b-tab__item')
    episodeItem = episodeList.select('.episode-item')
    print(episodeItem)
    pass


if __name__ == "__main__":
    # searchList("斗罗大陆")
    getPlayListByPage('')
