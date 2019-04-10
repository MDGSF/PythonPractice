#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Pattern.search(string[, pos[, endpos]])
"""

import re


def test1():
    pattern = re.compile("d")
    match = pattern.search("dog")  # Match at index 0
    print(match)  # <_sre.SRE_Match object; span=(0, 1), match='d'>

    # No match; search doesn't include the "d"
    match = pattern.search("dog", 1)
    print(match)  # None


def test2():
    """
    search 只匹配到了第一个符合的就结束了，没有继续匹配第二个 dog
    """
    print('\ntest2')
    pattern = re.compile("dog")
    match = pattern.search("dog, I have a dog")
    print(match) # <_sre.SRE_Match object; span=(0, 3), match='dog'>
    print(match.group()) # dog


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
