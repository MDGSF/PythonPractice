#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def test1():
    print('\ntest1')

    x = 10
    y = 1
    result = x if x > y else y
    print(result)


def max2(x, y):
    return x if x > y else y


def test2():
    print('\ntest2')
    print(max2(10, 20))
    print(max2(2, 1))


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
