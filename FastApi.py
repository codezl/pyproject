# -*- coding: utf-8 -*-

from fastapi import FastAPI
from get90V import resBody, getRewriteUrl
from get90V import resolveTxSelectVideo
app = FastAPI()


@app.get('/test/a={a}/b={b}')
def calculate(a: int = None, b: int = None):
    c = a + b
    res = {"res": c}
    return res


@app.get('/v/q={name}')
def getVsearch(name: str = ''):
    url = 'https://v.qq.com/x/search/?q='+name+'&stag=0&smartbox_ab='
    return resBody(url)


# 根据剧集换取列表（txx）
@app.get("/v/getList/playId={playId}")
def getTxPlayList(playId: str = ''):
    # 变量名字要和{}中的名字一致
    # 'https://v.qq.com/x/cover/m441e3rjq9kwpsc.html'
    url = 'https://v.qq.com/x/cover/' + playId + '.html'
    print('拼接地址'+url)
    # res = resolveTxSelectVideo(url)
    return resolveTxSelectVideo(url)


@app.get('')
def getVlist():
    pass


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app,
                host="0.0.0.0",
                port=8082,
                workers=1)