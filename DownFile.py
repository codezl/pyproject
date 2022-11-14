#!/usr/bin/python
#encoding:utf-8
import urllib3
import os

def Schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print('%.2f%%' % per)


def down():
    url = 'http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2'
    #local = url.split('/')[-1]
    local = os.path.join('/data/software','Python-2.7.5.tar.bz2')
    urllib3.urlretrieve(url, local, Schedule)


def down2():
    import requests
    print("downloading with requests")
    url = 'http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2'
    r = requests.get(url)
    with open("demo3.zip", "wb") as code:
        code.write(r.content)


def down3():
    import urllib3
    print("downloading with urllib2")
    url = 'http://.pythontab.com/test/demo.zip'
    f = urllib3.urlopen(url)
    data = f.read()
    with open("demo2.zip", "wb") as code:
        code.write(data)

if __name__ == "__main__":
    down2()