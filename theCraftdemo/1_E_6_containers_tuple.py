#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def test1():
    a = 1, 2, 3  # 不建议这种写法
    b = (1, 2, 3)
    print(a)
    print(b)
    print(a == b)


def test2():
    print()

    # a 是元组
    a = 2,
    print(a)

    # b 是数字
    b = 2
    print(b)

    # c 是数字
    c = (2)
    print(c)
    print(type(c))

    # d 是元组
    d = (2,)
    print(d)
    print(type(d))


def test3():
    print()

    a = (1,)
    print(a)
    print(id(a))

    a += (3, 5)
    print(a)
    print(id(a))  # id 并不相同 —— 实际上是在内存中另外新创建了一个元组……


def test4():
    print()

    # tuple 占用的内存比 list 小
    n = 10000
    a = range(n)
    b = tuple(a)
    c = list(a)
    print(a.__sizeof__())
    print(b.__sizeof__())
    print(c.__sizeof__())


def main():
    test1()
    test2()
    test3()
    test4()


if __name__ == "__main__":
    main()
