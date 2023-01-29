# 获取旧的行政地区代码
import re
from array import array
from typing import List

import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, Body
from pydantic import BaseModel

from MysqlConn import conn

app = FastAPI()
desUrl = 'https://www.mca.gov.cn/article/sj/xzqh/1980/1980/201911180950.html'


def getRes(url):
    session = requests.Session()
    res = session.get(url)
    res.encoding = 'utf-8'
    return res


def resolveBody():
    now_conn = sqlConn()
    cur = now_conn.cursor()
    res = getRes(desUrl)
    soup = BeautifulSoup(res.text, 'lxml')
    bd1 = soup.find_all('tr', style=re.compile('mso-height-source:userset;height:15.4pt'))
    # print(bd1)
    countData = 0
    for i in bd1:
        bd2 = i.select('td')
        # print(bd2[1])
        # print(bd2[2])
        ex = insertOldSql(bd2[2].text, bd2[1].text, '')
        cur.execute(ex)
        if '0000' in bd2[1]:
            pass
        for n in bd2:
            nstr = str(n)
            if '省' in nstr or '自治区' in nstr or '行政区' in nstr:
                countData = countData + 1
                print(bd2[1].text)
                print(bd2[2].text)
    print(countData)
    cur.close()
    now_conn.close()


def sqlConn():
    return conn('localhost', 3306, 'root', 'root', 'test')


def insertOldSql(cityname, citycode, belongcity):
    sqlEx = 'insert into old_district_info(`name`, `citycode`,`belong_city`) ' \
            'values(\''+cityname+'\',\''+citycode+'\',\''+belongcity+'\')'
    return sqlEx


def insertNewSql(cityname, citycode, address, belongcity, is_old):
    # 拼接sql语句时如果有数字类型要转成str字符类型
    sqlEx = 'insert into district_info(`name`, `address`, `district_code`,`belong_district`, is_old) ' \
            'values(\''+cityname+'\',\''+address+'\',\''+citycode+'\',\''+belongcity+'\',\''+str(is_old)+'\')'
    return sqlEx


class Item(BaseModel):
    districtList: list


@app.post("/insert")
# 使用fastapi自带的List[int] 需要指定类型，使用python自带的list不用
def insertNew(item: Item):
    print(item.districtList)
    now_conn = sqlConn()
    cur = now_conn.cursor()
    for i in item.districtList:
        # print(i['cityName'])
        ex = insertNewSql(i['cityName'], i['code'], i['address'], i['belongDistrict'], i['isOld'])
        # 避免重复插入设置唯一键或者验证
        cur.execute(ex)
    cur.close()
    now_conn.close()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app=app,
        host="0.0.0.0",
        port=8880,
        workers=1
    )
    # resolveBody()
    # pass
