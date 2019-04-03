#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def test1():
    a = [1, 2, 3]
    b = a
    b += [1, 2, 3]
    print(a, b)
    print(id(a), id(b))
    # [1, 2, 3, 1, 2, 3] [1, 2, 3, 1, 2, 3]
    # 140520021163912 140520021163912


def test2():
    a = [1, 2, 3]
    b = a
    b = b + [1, 2, 3]
    print(a, b)
    print(id(a), id(b))
    # [1, 2, 3] [1, 2, 3, 1, 2, 3]
    # 140520021163912 140519993018888


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
