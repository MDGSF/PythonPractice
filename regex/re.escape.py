#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
re.escape(pattern)
"""

import re
import string


def test1():
    print(re.escape('python.exe'))


def test2():
    legal_chars = string.ascii_lowercase + string.digits + "!#$%&'*+-.^_`|~:"
    print(re.escape(legal_chars))


def test3():
    operators = ['+', '-', '*', '/', '**']
    print('|'.join(map(re.escape, sorted(operators, reverse=True))))


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
