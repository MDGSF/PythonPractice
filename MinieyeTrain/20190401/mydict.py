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
        self.t = table.Table(**kwargs)

    def get(self, key, default=None):
        value = self.t.get(key)
        if value is None:
            return default
        else:
            return value

    def set(self, key, value):
        self.t.insert(key, value)

    def update(self, other):
        self.t.update(other.t)

    def values(self):
        pass

    def keys(self):
        pass

    def items(self):
        pass

    def __str__(self):
        return self.t.__str__()


def main():
    a = MyDict(name="huangjian")
    print(a)

    print(a.get("name"))

    a.set("name", "jianhuang")
    print(a.get("name"))

    b = MyDict()
    b.set("name", "jian")
    b.set("id", 1)
    a.update(b)
    print(a)


if __name__ == "__main__":
    main()
