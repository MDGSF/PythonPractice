#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Pattern.fullmatch(string[, pos[, endpos]])
"""

import re


def test1():
    """
    fullmatch 要整个字符串完全匹配才行
    """
    pattern = re.compile("o[gh]")

    # No match as "o" is not at the start of "dog".
    match = pattern.fullmatch("dog")
    print(match) # None

    # No match as not the full string matches.
    match = pattern.fullmatch("ogre")
    print(match) # None

    match = pattern.fullmatch("doggie", 1, 3)
    print(match) # <_sre.SRE_Match object; span=(1, 3), match='og'>


def main():
    test1()


if __name__ == "__main__":
    main()
