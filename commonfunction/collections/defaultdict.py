#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
使用dict时，如果引用的Key不存在，就会抛出KeyError。
如果希望key不存在时，返回一个默认值，就可以用defaultdict。
除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
"""

from collections import defaultdict


def test1():
    dd = defaultdict(lambda: 'N/A')
    dd['key1'] = 'abc'
    print(dd['key1'])
    print(dd['key2'])


def main():
    test1()


if __name__ == "__main__":
    main()
