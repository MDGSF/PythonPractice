#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from collections import Counter


def test1():
    c = Counter()
    for ch in 'programming':
        c[ch] = c[ch] + 1
    print(c)


def main():
    test1()


if __name__ == "__main__":
    main()
