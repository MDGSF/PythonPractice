#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib import parse, request
import msgpack

def test1():
    f = open('test.jpg', 'rb')
    imgData = f.read()

    data = {
        "imgrawdata": imgData,
        "suffix": "jpg",
        "watermarks": [
            {
                "type": 1,
                "text": '中国 minieye watermark',
                "fontsize": 20,
                "rgba": [255, 0, 0, 100]
            },
            {
                "type": 2,
                "text": 'Minieye 左上角',
                "fontsize": 20,
                "rgba": [255, 255, 255, 100]
            },
            {
                "type": 3,
                "text": 'Minieye 左下角',
                "fontsize": 20,
                "rgba": [255, 255, 255, 100]
            },
            {
                "type": 4,
                "text": 'Minieye 右上角',
                "fontsize": 20,
                "rgba": [255, 255, 255, 100]
            },
            {
                "type": 5,
                "text": 'Minieye 右下角',
                "fontsize": 20,
                "rgba": [255, 255, 255, 100]
            }
        ]
    }

    mpData = msgpack.packb(data, use_bin_type=True)
    print(len(mpData))

    url = 'http://127.0.0.1:5001/api/v1/watermark'
    req = request.Request(url=url, data=mpData, method='POST')
    result = request.urlopen(req)

    imgWMFile = open('newImage.jpg', 'wb')
    imgWMFile.write(result.read())
    imgWMFile.close()

    f.close()


def main():
    test1()


if __name__ == "__main__":
    main()
