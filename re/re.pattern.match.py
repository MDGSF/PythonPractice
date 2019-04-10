#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Pattern.match(string[, pos[, endpos]])
"""

import re


def test1():
    """
    match 匹配的时候，是从字符串的起始位置开始匹配的。
    """
    pattern = re.compile("o")

    # No match as "o" is not at the start of "dog".
    match = pattern.match("dog")
    print(match)  # None

    # Match as "o" is the 2nd character of "dog".
    match = pattern.match("dog", 1)
    print(match)  # <_sre.SRE_Match object; span=(1, 2), match='o'>


def test2():
    print('\ntest2')
    pattern = re.compile("dog")
    match = pattern.match("dog, I have a dog.")
    print(match) # <_sre.SRE_Match object; span=(0, 3), match='dog'>

    match = pattern.match("I have a dog.")
    print(match) # None


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
