# -*- coding: utf-8 -*-
import base64
import encodings.utf_8
import io
import os
import cv
import cv2
# 转码
import chardet
import codecs

import numpy as np
from PIL import Image
from fastapi import FastAPI
from starlette.responses import FileResponse, HTMLResponse, StreamingResponse

from get90V import resBody, getRewriteUrl
from get90V import resolveTxSelectVideo, exchangePlayUrl
from django.http.response import HttpResponse
from Smiles2img import smlies2ImgBs64,smlies2ImgBs642
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
    return imgBs4
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


@app.get('/smi2base642')
def smi2base642(smi):
    smis = [smi]
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "examsystem.settings")
    bs64 = smlies2ImgBs64(smis)
    dcbs64 = base64.b64decode(bs64)
    # dcbs64 = bs64.decode('UTF-8')
    image = io.BytesIO(dcbs64)
    # img = image.open(image)

    # ------
    img = smlies2ImgBs642(smis)
    # out = io.BytesIO()
    out = io.FileIO(img)
    img.save(out, format="png")
    # image = io.BytesIO(dcbs64)

    with open(dcbs64, "rb") as f:
        image_stream = f.read()
        image_stream = base64.b64encode(image_stream)

    return HttpResponse(content=open(out.read(), mode='rb'), content_type='image/png')
    return 1


@app.get('/img2')
def getByte(smi):
    smis = [smi]
    img = smlies2ImgBs642(smis)
    img_bytes = io.BytesIO()
    img_file = io.FileIO()
    # 将图片数据存入字节流管道， format可以按照具体文件的格式填写
    img.save(img_bytes, format="png")
    # 从字节流管道中获取二进制
    image_bytes = img_bytes.getvalue()
    image = Image.open(io.BytesIO(image_bytes), mode='r')
    img_stream = img_bytes.read()
    img_stream = base64.b64encode(img_stream)
    # img = image.open(image)
    # img.show()

    # 转为矩阵
    image = image.crop([8, 8, 120, 120])
    image = np.asarray(image)
    # 对数组的图片格式进行编码
    success, encoded_image = cv2.imencode(".jpg", image)
    # 将数组转为bytes
    byte_data = encoded_image.tobytes()

    # 使用fileIO --- 无效
    # img.save(out, format='png')
    out = io.FileIO(img_bytes.getvalue())
    fileO = open(out.read(), mode='rb', encoding='UTF-8')

    # 修改编码
    # with open('文件路径', mode='r') as f:
    #     text = f.read()
    #
    # with open('文件路径', mode='w', encoding='utf-8') as f:
    #     f.write(text)

    # source_encoding = chardet.detect(content)['encoding']

    print(byte_data)
    # return FileResponse(fileO.read(), filename='123.png')
    return StreamingResponse(fileO.read(), media_type="image/png")
    # return HttpResponse(content=fileO.read(), content_type='image/png')


# 返回html页面
@app.get("/html")
def user():
    url = 'http://localhost:8082/img?request=1'
    # url = """data:image/png;base64,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"""
    url1 = url+"123"
    print(url1)
    html_content = """
    <html>
        <body>
            <p style="color:red">HTMLResponse的用法</P>
            <h3>还可以显示图片</h3>
            <img src=\"""" + url + """\" style="width:100px;height:100px;" />
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)


# 使用模返回html render_template
# @app.route('/display/<id>')
# def display(id):
#     test = BlobDataTestor()
#     data = test.get_pic_data(id=id)
#     img_stream = base64.b64encode(data).decode()
#     print(img_stream)
#     return render_template('new_picture.html', img_stream=img_stream)


def return_img_stream(image_loca_path): #向前端显示图片时使用，把图片转换成数据流
    image_stream = ''
    # with open(image_loca_path,"r",encoding="UTF-8") as f: # 图片格式有问题
    with open(image_loca_path, "rb") as f:
        image_stream = f.read()
        image_stream = base64.b64encode(image_stream)
    return image_stream


def resDto(data, code, msg):
    res = {'code': code, 'msg': msg, 'data': data}
    return res


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app,
                host="0.0.0.0",
                port=8082,
                workers=1)
