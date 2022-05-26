# a py file to get video in the network
import requests
from bs4 import BeautifulSoup



def cURL():
    headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
    r = requests.get('https://www.baidu.com/', headers)
    if r.status_code == 200:
        print('request success!\n')
        print(r.text+'\n')
        soup = BeautifulSoup(r.text, 'lxml')
        print('百度'+str(soup.find_all('a'))+'\n')
    else:
        print('request fail\n')


def login():
    headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
    # post请求
    data = {'users': 'abc', 'password': '123'}
    r = requests.post('https://www.weibo.com', data=data, headers=headers)
    print(r.status_code)
    print(r.text)


def sessionRes():
    headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
    # post请求
    data = {'users': 'abc', 'password': '123'}
    # 保持会话
    # 新建一个session对象
    sess = requests.session()
    # 先完成登录
    sess.post('maybe a login url', data=data, headers=headers)
    # 然后再在这个会话下去访问其他的网址
    sess.get('other urls')


def xmlAnalyze():
    html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    """
    # 选用lxml解析器来解析
    soup = BeautifulSoup(html, 'lxml')
    print('标题：'+str(soup.title)+'\n')
    print(soup.find_all('a'))
    print('标题'+soup.title.text+'\n')
    print(soup.find_all(attrs={'id': 'link1'}))
    print(soup.find_all('a', id='link2'))


def getGameName():
    # 页面url地址
    url = 'http://newgame.17173.com/game-list-0-0-0-0-0-0-0-0-0-0-1-2.html'

    # 发送请求，r为页面响应
    r = requests.get(url)

    # r.text获取页面代码
    # 使用lxml解析页面代码
    soup = BeautifulSoup(r.text, 'lxml')

    # 两次定位，先找到整个信息区域
    info_list = soup.find_all(attrs={'class': 'ptlist ptlist-pc'})

    # 在此区域内获取游戏名，find_all返回的是list
    tit_list = info_list[0].find_all(attrs={'class': 'tit'})

    # 遍历获取游戏名
    # .text可获取文本内容，替换掉文章中的换行符
    for title in tit_list:
        print(title.text.replace('\n', ''))


class Config:
    kd = '数据分析'
    referer = 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput='
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': referer,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/'
                      '537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}


class Spider:

    def __init__(self, kd=Config.kd):
        self.kd = kd
        self.url = Config.referer
        self.api = 'https://www.lagou.com/jobs/positionAjax.json'

        # 必须先请求referer网址
        self.sess = requests.session()
        self.sess.get(self.url, headers=Config.headers)

    def get_position(self, pn):
        data = {'first': 'true',
                'pn': str(pn),
                'kd': self.kd
                }
        # 向API发起POST请求
        r = self.sess.post(self.api, headers=Config.headers, data=data)
        print("拉钩返回"+str(r))
        # 直接.json()解析数据
        return r.json()['content']['positionResult']['result']

    def engine(self, total_pn):
        for pn in range(1, total_pn + 1):
            results = self.get_position(pn)
            for pos in results:
                print(pos['positionName'], pos['companyShortName'], pos['workYear'], pos['salary'])


def lagou():
    url = 'https://www.lagou.com/'
    heders = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/'
                      '537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    session = requests.session()
    r = session.get(url,  headers=heders)
    # print('请求拉钩'+str(r.text))
    soup = BeautifulSoup(r.text, 'lxml')
    list = soup.find_all(attrs={'class': 'friend-link'})
    for i in list:
        print(str(i)+'\n')
    # print(list)


if __name__ == "__main__":
    cURL()
    login()
    xmlAnalyze()
    getGameName()
    print('获取')
    lagou()
