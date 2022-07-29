# -*- coding: utf-8 -*-

from fastapi import FastAPI
from get90V import resBody, getRewriteUrl, resolveTxSelectVideo

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


@app.get('')
def getVlist():
    pass


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app,
                host="0.0.0.0",
                port=8080,
                workers=1)