from decimal import Decimal
from random import random
from typing import Union

from flask import Flask, Response, request, render_template
import os
from paddleocr import PaddleOCR, draw_ocr
from pydantic import BaseModel
from urllib3 import response

app = Flask(__name__)


def ocrdemo():
    # Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
    # 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
    img_path = 'D:\\springDown\\111.jpeg'
    result = ocr.ocr(img_path, cls=True)
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            print(line)

    # 显示结果
    from PIL import Image
    result = result[0]
    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf')
    im_show = Image.fromarray(im_show)
    im_show.save('result.jpg')


ALLOW_EXTENSIONS = ['png', 'jpg', 'jpeg']
UPLOAD_FOLDER = ''
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[-1] in ALLOW_EXTENSIONS


class Res(BaseModel):
    state: int = 200
    msg: str = "success"
    data: Union[float, str, None]


@app.route("/photo/upload", methods=['POST', "GET"])
def uploads():
    if request.method == 'POST':
        # 获取post过来的文件名称，从name=file参数中获取
        file = request.files['file']
        if file and allowed_file(file.filename):
            print(file.filename)
            # secure_filename方法会去掉文件名中的中文
            # file_name = secure_filename(file.filename)
            # 保存图片
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            ocr = PaddleOCR(use_angle_cls=True,
                            lang="ch")  # need to run only once to download and load model into memory
            result = ocr.ocr(app.config['UPLOAD_FOLDER'] + file.filename, cls=True)
            os.remove(app.config['UPLOAD_FOLDER'] + file.filename)
            print("长度" + str(result))
            ocrRes = []
            for idx in range(len(result)):
                res = result[idx]
                for line in res:
                    tup = line[1]
                    print("内容:"+tup[0]+',评分:'+str(tup[1])+"\n")
                    ocrRes.append(tup[0])
            return ocrRes
        else:
            return "格式错误，请上传jpg/png格式文件"
    return render_template('up_img_index.html')


def scanLuckyMoney(file: object) -> object:
    """

    :rtype: object
    """
    if file and allowed_file(file.filename):
        print(file.filename)
        # secure_filename方法会去掉文件名中的中文
        # file_name = secure_filename(file.filename)
        # 保存图片
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        ocr = PaddleOCR(use_angle_cls=True,
                        lang="ch")  # need to run only once to download and load model into memory
        result = ocr.ocr(app.config['UPLOAD_FOLDER'] + file.filename, cls=True)
        os.remove(app.config['UPLOAD_FOLDER'] + file.filename)
        print("长度" + str(result))
        ocrRes = []
        for idx in range(len(result)):
            res = result[idx]
            for line in res:
                tup = line[1]
                print("内容:" + tup[0] + ',评分:' + str(tup[1]) + "\n")
                ocrRes.append(tup[0])
        return ocrRes
    else:
        return "格式错误，请上传jpg/png格式文件"


@app.route("/scan/luckyMoney", methods=['POST'])
def scanLucky():
    file = request.files['file']
    res = scanLuckyMoney(file)

    resBody = Res()
    # 扫描到福字
    if '福' in str(res):
        resBody.data = Decimal(random()).quantize(Decimal("0.00"))
    else:
        resBody.msg = 'fail'
        resBody.state = 404
    return resBody.json()


@app.get('/refresh')
def rf():
    resp = response.HTTPResponse
    resp.headers()
    pass


# 识别文字并返回
def scanImg2Word(file: object) -> object:
    """

    :rtype: object
    """
    if file and allowed_file(file.filename):
        # secure_filename方法会去掉文件名中的中文
        # file_name = secure_filename(file.filename)
        # 保存图片
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        ocr = PaddleOCR(use_angle_cls=True,
                        lang="ch")  # need to run only once to download and load model into memory
        result = ocr.ocr(app.config['UPLOAD_FOLDER'] + file.filename, cls=True)
        os.remove(app.config['UPLOAD_FOLDER'] + file.filename)
        resStr = ''
        for idx in range(len(result)):
            res = result[idx]
            for line in res:
                tup = line[1]
                resStr = resStr+tup[0]
        return resStr
    else:
        return "格式错误，请上传jpg/png格式文件"


# 识别文字并将识别率最高的返回
def maxScoreScanImg2Word(file: object) -> object:
    """

    :rtype: object
    """
    if file and allowed_file(file.filename):
        # secure_filename方法会去掉文件名中的中文
        # file_name = secure_filename(file.filename)
        # 保存图片
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        ocr = PaddleOCR(use_angle_cls=True,
                        lang="ch")  # need to run only once to download and load model into memory
        result = ocr.ocr(app.config['UPLOAD_FOLDER'] + file.filename, cls=True)
        os.remove(app.config['UPLOAD_FOLDER'] + file.filename)
        print("长度" + str(result))
        ocrRes = []
        oldScore = 0
        nowScore = 0
        maxTup = ()
        for idx in range(len(result)):
            res = result[idx]
            for line in res:
                tup = line[1]
                nowScore = tup[1]
                if nowScore > oldScore:
                    maxTup = tup
                    oldScore = nowScore
                # print("内容:" + tup[0] + ',评分:' + str(tup[1]) + "\n")
                # sorted(tup, key=lambda t: t[1])
                # ocrRes.append(tup[0])
        return maxTup
    else:
        return "格式错误，请上传jpg/png格式文件"


@app.route("/ocr/img2word", methods=['POST', "GET"])
def img2word():
    if request.method == 'POST':
        # 获取post过来的文件名称，从name=file参数中获取
        file = request.files['file']
        res = scanImg2Word(file)
        return str(res)
    return render_template('up_img_index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8082, debug=True)
    # ocrdemo()
