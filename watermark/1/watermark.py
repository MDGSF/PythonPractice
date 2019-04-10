#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
rgba: red, green, blue, alpha
"""
from io import StringIO
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
import random


def AddImgWaterMark():
    img = Image.open('test.jpg')
    logo = Image.open('penguin.png')

    layer = Image.new('RGBA', img.size, (255, 255, 255, 0))
    layer.paste(logo, (img.size[0] - logo.size[0], img.size[1] - logo.size[1]))

    img_after = Image.composite(layer, img, layer)
    img_after.show()
    img_after.save('newImage.png')


def AddWaterMarkV1(imgName, newImgName, text, font, fontsize):
    image = Image.open(imgName)
    font = ImageFont.truetype(font, fontsize)

    layer = image.convert('RGBA')

    text_overlay = Image.new('RGBA', layer.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay)

    text_size_x, text_size_y = image_draw.textsize(text, font=font)

    text_xy = (layer.size[0] - text_size_x, layer.size[1] - text_size_y)

    image_draw.text(text_xy, text, font=font, fill=(255, 255, 255, 100))

    after = Image.alpha_composite(layer, text_overlay)
    after.save(newImgName)


def AddWaterMarkV2(imgName, newImgName, text, font, fontsize):
    image = Image.open(imgName)
    font = ImageFont.truetype(font, fontsize)

    layer = image.convert('RGBA')

    text_overlay = Image.new('RGBA', layer.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay)

    text_size_x, text_size_y = image_draw.textsize(text, font=font)

    text_xy = ((layer.size[0] - text_size_x) // 2, layer.size[1] - text_size_y)

    image_draw.text(text_xy, text, font=font, fill=(255, 255, 255, 100))

    after = Image.alpha_composite(layer, text_overlay)
    after.save(newImgName)


def AddWaterMarkV3(imgName, newImgName, text, font, fontsize):
    image = Image.open(imgName)
    font = ImageFont.truetype(font, fontsize)

    layer = image.convert('RGBA')

    text_overlay = Image.new('RGBA', layer.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay)

    text_size_x, text_size_y = image_draw.textsize(text, font=font)

    cury = 0
    dx = layer.size[0] - text_size_x
    dy = layer.size[1] - text_size_y
    print(layer.size[0], layer.size[1], text_size_x, text_size_y, dx, dy)
    while cury < layer.size[1]:
        curx = random.randrange(10, 200)
        while curx < layer.size[0]:
            text_xy = (curx, cury)
            image_draw.text(text_xy, text, font=font, fill=(255, 255, 255,
                                                            18))
            curx += random.randrange(text_size_x * 2, text_size_x * 3)
        cury += random.randrange(text_size_y * 4, text_size_y * 5)

    after = Image.alpha_composite(layer, text_overlay)
    after.save(newImgName)


def AddWaterMarkV4(imgData, suffix, watermarks):
    originImage = Image.open(BytesIO(imgData))
    rgbaImage = originImage.convert('RGBA')

    maxsize = max(rgbaImage.size[0], rgbaImage.size[1])
    fontsize = maxsize // 40
    print(f'maxsize = {maxsize}, fontsize = {fontsize}')

    for wm in watermarks:
        font = ImageFont.truetype(wm['font'], fontsize)
        wmImage = Image.new('RGBA', rgbaImage.size, (255, 255, 255, 0))
        wmImageDrawer = ImageDraw.Draw(wmImage)

        text_size_x, text_size_y = \
            wmImageDrawer.textsize(wm['text'], font=font)

        if wm['type'] == 1:
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
                    curx += random.randrange(text_size_x * 2, text_size_x * 3)
                cury += random.randrange(text_size_y * 4, text_size_y * 5)
        elif wm['type'] == 2:  # 左上角
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
        rgbaImage.save(t, format=suffix, quality=80)
        return t
    elif suffix == 'jpg' or suffix == 'jpeg':
        jpgImage = Image.new("RGB", rgbaImage.size, (255, 255, 255))
        jpgImage.paste(rgbaImage,
                       mask=rgbaImage.split()[3])  # 3 is the alpha channel
        jpgImage.save(t, format='JPEG', quality=100)
        return t
    else:
        rgbaImage.save(t, format='png', quality=80)
        return t


def test4():
    """
    1000*1000 fontsize: 20
    3000*2000 fontsize: 100
    """
    f = open('test.jpg', 'rb')
    imgData = f.read()

    wm1 = {
        "type": 1,
        "text": '中国 minieye watermark',
        "font": 'msyh.ttf',
        "fontsize": 20,
        "rgba": [255, 255, 255, 18]
    }

    wm2 = {
        "type": 2,
        "text": 'Minieye 左上角',
        "font": 'msyh.ttf',
        "fontsize": 20,
        "rgba": [255, 255, 255, 100]
    }

    wm3 = {
        "type": 3,
        "text": 'Minieye 左下角',
        "font": 'msyh.ttf',
        "fontsize": 20,
        "rgba": [255, 255, 255, 100]
    }

    wm4 = {
        "type": 4,
        "text": 'Minieye 右上角',
        "font": 'msyh.ttf',
        "fontsize": 20,
        "rgba": [255, 255, 255, 100]
    }

    wm5 = {
        "type": 5,
        "text": 'Minieye 右下角',
        "font": 'msyh.ttf',
        "fontsize": 60,
        "rgba": [255, 255, 255, 100]
    }

    watermarks = [wm1, wm2, wm3, wm4, wm5]

    imgWMData = AddWaterMarkV4(imgData, 'jpg', watermarks)
    imgWMFile = open('newImage.jpg', 'wb')
    imgWMFile.write(imgWMData.getvalue())
    imgWMFile.close()

    f.close()


def test1():
    text = '中国深圳 minieye watermark'
    AddWaterMarkV1('test.jpg', 'newImage.png', text, 'chinese.msyh.ttf', 20)


def test2():
    text = '中国深圳 minieye watermark'
    AddWaterMarkV2('test.jpg', 'newImage.png', text, 'chinese.msyh.ttf', 20)


def test3():
    text = '中国深圳 minieye watermark'
    AddWaterMarkV3('test.jpg', 'newImage.png', text, 'msyh.ttf', 20)


def main():
    test4()


if __name__ == "__main__":
    main()
