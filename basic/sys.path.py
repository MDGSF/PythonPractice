#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys


def main():
    print('__file__ = ', __file__)

    print('os.path.abspath(__file__) = ', os.path.abspath(__file__))

    print('os.path.dirname(os.path.abspath(__file__)) = ',
          os.path.dirname(os.path.abspath(__file__)))

    _src_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print('src_path', _src_path)

    # 模块 A 要调用模块 B，如果路径不对的话，只要把模块 B 的路径加入 sys.path 就可以了。
    print(sys.path)


if __name__ == "__main__":
    main()
