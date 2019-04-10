#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from flask import Flask
from flask import request
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import random
import msgpack

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/v1/watermark', methods=['POST'])
def APIAddWaterMarkV1():
    rawdata = request.get_data()
    msg = msgpack.unpackb(rawdata, raw=False)
    imgWMData = AddWaterMarkV1(msg['imgrawdata'],
                               msg['suffix'],
                               msg['watermarks'])
    return imgWMData.getvalue(), 200


def AddWaterMarkV1(imgData, suffix, watermarks):
    fontpath = '/usr/share/fonts/msyh.ttf'

    originImage = Image.open(BytesIO(imgData))
    rgbaImage = originImage.convert('RGBA')

    print('image (x,y) =', rgbaImage.size[0], rgbaImage.size[1])

    for wm in watermarks:
        if wm['type'] == 1:

            maxsize = max(rgbaImage.size[0], rgbaImage.size[1])
            fontsize = maxsize // 80
            print(f'maxsize = {maxsize}, fontsize = {fontsize}')
            if "fontsize" in wm.keys():
                if wm['fontsize'] > 0:
                    fontsize = wm['fontsize']

            font = ImageFont.truetype(fontpath, fontsize)
            wmImage = Image.new('RGBA', rgbaImage.size, (255, 255, 255, 0))
            wmImageDrawer = ImageDraw.Draw(wmImage)

            text_size_x, text_size_y = \
                wmImageDrawer.textsize(wm['text'], font=font)

            print('text  (x,y) =', text_size_x, text_size_y)

            rangestart = rgbaImage.size[0] // 6
            rangeend = rgbaImage.size[0] // 5
            if rangestart < text_size_x:
                rangestart += text_size_x
                rangeend += text_size_x

            cury = 0
            while cury < rgbaImage.size[1]:
                curx = random.randrange(10, 200)
                while curx < rgbaImage.size[0]:
                    wmImageDrawer.text((curx, cury),
                                       wm['text'],
                                       font=font,
                                       fill=(wm['rgba'][0],
                                             wm['rgba'][1],
                                             wm['rgba'][2],
                                             wm['rgba'][3]))
                    curx += random.randrange(rangestart, rangeend)
                cury += random.randrange(text_size_y * 4, text_size_y * 5)
        else:

            maxsize = max(rgbaImage.size[0], rgbaImage.size[1])
            fontsize = maxsize // 40
            print(f'maxsize = {maxsize}, fontsize = {fontsize}')
            if "fontsize" in wm.keys():
                if wm['fontsize'] > 0:
                    fontsize = wm['fontsize']

            font = ImageFont.truetype(fontpath, fontsize)
            wmImage = Image.new('RGBA', rgbaImage.size, (255, 255, 255, 0))
            wmImageDrawer = ImageDraw.Draw(wmImage)

            text_size_x, text_size_y = \
                wmImageDrawer.textsize(wm['text'], font=font)

            print('text  (x,y) =', text_size_x, text_size_y)

            if wm['type'] == 2:  # 左上角
                wmImageDrawer.text((0, 0),
                                   wm['text'],
                                   font=font,
                                   fill=(wm['rgba'][0],
                                         wm['rgba'][1],
                                         wm['rgba'][2],
                                         wm['rgba'][3]))
            elif wm['type'] == 3:  # 左下角
                dy = rgbaImage.size[1] - text_size_y
                wmImageDrawer.text((0, dy),
                                   wm['text'],
                                   font=font,
                                   fill=(wm['rgba'][0],
                                         wm['rgba'][1],
                                         wm['rgba'][2],
                                         wm['rgba'][3]))
            elif wm['type'] == 4:  # 右上角
                dx = rgbaImage.size[0] - text_size_x
                wmImageDrawer.text((dx, 0),
                                   wm['text'],
                                   font=font,
                                   fill=(wm['rgba'][0],
                                         wm['rgba'][1],
                                         wm['rgba'][2],
                                         wm['rgba'][3]))
            elif wm['type'] == 5:  # 右下角
                dx = rgbaImage.size[0] - text_size_x
                dy = rgbaImage.size[1] - text_size_y
                wmImageDrawer.text((dx, dy),
                                   wm['text'],
                                   font=font,
                                   fill=(wm['rgba'][0],
                                         wm['rgba'][1],
                                         wm['rgba'][2],
                                         wm['rgba'][3]))

        rgbaImage = Image.alpha_composite(rgbaImage, wmImage)

    t = BytesIO()
    if suffix == 'png':
        rgbaImage.save(t, format=suffix, quality=95)
        return t
    elif suffix == 'jpg' or suffix == 'jpeg':
        jpgImage = Image.new("RGB", rgbaImage.size, (255, 255, 255))
        jpgImage.paste(rgbaImage,
                       mask=rgbaImage.split()[3])  # 3 is the alpha channel
        jpgImage.save(t, format='JPEG', quality=95)
        return t
    else:
        rgbaImage.save(t, format='png', quality=95)
        return t


def main():
    app.run(debug=True, host="127.0.0.1", port=5001)


if __name__ == "__main__":
    main()
