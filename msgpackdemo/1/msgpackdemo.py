#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import msgpack


def test1():
    stu1 = {
        'id': 1,
        'name': 'ping'
    }
    print('stu1 =', stu1)

    msg = msgpack.packb(stu1)
    print(type(msg))
    print(len(msg))
    print(msg)

    stu2 = msgpack.unpackb(msg, use_list=False, encoding='utf-8')
    print('stu2 =', stu2)


def main():
    test1()


if __name__ == "__main__":
    main()
