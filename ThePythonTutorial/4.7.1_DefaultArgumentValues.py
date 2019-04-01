#!/usr/bin/env python
# -*- coding: UTF-8 -*-

i = 5


def f1(arg=i):
    print(arg)


i = 6


def test1():
    f1()


def f2(a, L=[]):
    L.append(a)
    return L


def test2():
    print(f2(1))
    print(f2(2))
    print(f2(3))


def f3(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


def test3():
    print(f3(1))
    print(f3(2))
    print(f3(3))


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
