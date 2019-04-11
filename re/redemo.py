#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re


def test1():
    """
    匹配一个被单引号或者是双引号括起来的字符串。
    """
    pattern = re.compile(r'(?P<quote>[\'\"]).*?(?P=quote)')
    match = pattern.match('"huangjian"')
    if match is not None:
        print(match.group())


def main():
    test1()


if __name__ == "__main__":
    main()
