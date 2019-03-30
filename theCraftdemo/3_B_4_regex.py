#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
https://docs.python.org/3/library/re.html
https://regex101.com/
https://regexper.com/
"""


import re


def test1():
    str = 'The quick brown fox jumps over the lazy dog'
    pattn = re.compile(r'\wo\w')
    result = re.findall(pattn, str)
    print(result)


def main():
    test1()


if __name__ == "__main__":
    main()
