# -*- coding: utf-8 -*-

from fastapi import FastAPI
from starlette.responses import FileResponse, HTMLResponse, StreamingResponse

from get90V import resBody, getRewriteUrl
from get90V import resolveTxSelectVideo, exchangePlayUrl
from django.http.response import HttpResponse
from Smiles2img import smlies2ImgBs64
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


@app.get("/v/getVipUrl")
def getVipUrl(playId: str = ''):
    # url = 'https://v.qq.com/x/cover/' + playId + '.html'
    playId = playId + '.html'
    vipUrl = exchangePlayUrl(playId, "")
    return resDto(vipUrl, 200, 'ok')


# 最终解决，只要链接返回图片流，直接使用浏览器时是下载，但是如果放到html的img标签中加载就会显示土拍你
# 由此考虑可以使用返回html的形式返回图片
# 确实可以，看下面的html方法
@app.get('/img')
def getVlist(request):
    path = r"C:\Users\ll\Desktop\店铺组合图.png"
    fileOpen = open(path, mode='rb')
    import base64
    imgBs4 = base64.b64encode(fileOpen.read()).decode()
    # return imgBs4
    # 不写入名字会直接下载attachment下载
    # res = HttpResponse(content=fileOpen.read(), content_type='image/png',
    #                    headers={
    #                             'Content-Disposition': "attachment;fileName=123.png"},
    #                    )
    # 不能设置header
    # res = HttpResponse(content=fileOpen.read(), content_type='image/png',
    #                    headers={
    #                        'Content-Disposition': "inline;fileName=123.png"},
    #                    )
    res = HttpResponse(content=fileOpen, content_type='image/png')
    # res.headers = {}
    return res
    # return StreamingResponse(fileOpen.read())
    return StreamingResponse(fileOpen, media_type="image/png")
    # pass
    #
    # return FileResponse(fileOpen.read(), filename='123.png')
    return FileResponse(r"C:\Users\ll\Desktop\店铺组合图.png", media_type="image/png", filename='111')


@app.get('/smi2base64')
def smi2base64(smi):
    smis = [smi]
    return smlies2ImgBs64(smis)


# 返回html页面
@app.get("/html")
def user():
    html_content = """
    <html>
        <body>
            <p style="color:red">HTMLResponse的用法</P>
            <h3>还可以显示图片</h3>
            <img src="http://localhost:8082/img?request=1" style="width:100px;height:100px;" />
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)


def resDto(data, code, msg):
    res = {'code': code, 'msg': msg, 'data': data}
    return res


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app,
                host="0.0.0.0",
                port=8082,
                workers=1)
