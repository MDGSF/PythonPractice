#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from collections import namedtuple


def test1():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print(p.x, p.y)
    print(isinstance(p, Point))
    print(isinstance(p, tuple))


def test2():
    Circle = namedtuple('Circle', ['x', 'y', 'r'])
    c = Circle(1, 2, 3)
    print(c)


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
