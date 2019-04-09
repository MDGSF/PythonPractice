#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import msgpack


def test1():
    f = open('test.jpg', 'rb')
    imgData = f.read()

    stu1 = {
        'id': 1,
        'name': 'ping',
        'imgrawdata': imgData
    }
    print('stu1 =', stu1['id'], stu1['name'])

    msg = msgpack.packb(stu1, use_bin_type=True)
    print(type(msg))
    print(len(msg))

    stu2 = msgpack.unpackb(msg, raw=False)
    print('stu2 =', stu2['id'], stu2['name'])

    newf = open('newImage.jpg', 'wb')
    newf.write(stu2['imgrawdata'])
    newf.close()

    f.close()


def main():
    test1()


if __name__ == "__main__":
    main()
