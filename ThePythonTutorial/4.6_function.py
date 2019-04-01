#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


def test1():
    fib(2000)


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


def test2():
    f100 = fib2(100)
    print(f100)


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
