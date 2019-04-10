#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
re.findall(pattern, string, flags=0)
"""

import re


def test1():
    result = re.findall(r'\w+', 'Words, words, words')
    print(result) # ['Words', 'words', 'words']


def test2():
    result = re.findall(r'(go)+', 'google, gogogle, gogogo')
    print(result) # ['go', 'go', 'go']


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
