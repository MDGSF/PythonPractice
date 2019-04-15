#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys

try:
    import table
except:
    _src_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print('src_path', _src_path)
    sys.path.append(_src_path)


class MyDict():
    def __init__(self, **kwargs):
        pass

    def get(self, key, default=None):
        pass

    def set(self, key, value):
        pass

    def update(self, other):
        pass

    def values(self):
        pass

    def keys(self):
        pass

    def items(self):
        pass

    def __str__(self):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
