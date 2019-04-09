#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
rgba: red, green, blue, alpha
"""

from PIL import Image, ImageDraw, ImageFont
import random


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
    while cury < dy:
        curx = random.randrange(10, 200)
        while curx < dx:
            text_xy = (curx, cury)
            image_draw.text(text_xy, text, font=font, fill=(255, 255, 255, 18))
            curx += random.randrange(text_size_x * 2, text_size_x * 3)
        cury += random.randrange(text_size_y * 4, text_size_y * 5)

    after = Image.alpha_composite(layer, text_overlay)
    after.save(newImgName)


def AddImgWaterMark():
    img = Image.open('test.jpg')
    logo = Image.open('penguin.png')

    layer = Image.new('RGBA', img.size, (255, 255, 255, 0))
    layer.paste(logo, (img.size[0] - logo.size[0], img.size[1] - logo.size[1]))

    img_after = Image.composite(layer, img, layer)
    img_after.show()
    img_after.save('newImage.png')


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
    test3()


if __name__ == "__main__":
    main()
