#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def factorial(n):
    return 1 if n == 1 else n * factorial(n - 1)


def test1():
    print(factorial(5))


def main():
    test1()


if __name__ == "__main__":
    main()
