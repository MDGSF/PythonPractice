#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# https://docs.python.org/3/library/functions.html#bool
# https://docs.python.org/3/library/stdtypes.html#truth

# class bool([x])
#   Return a Boolean value, i.e. one of True or False.


def test1():
    print(bool(0))
    print(bool(0.0))
    print(bool(''))
    print(bool(None))
    print(bool([]))
    print(bool({}))
    print(bool(()))
    print(bool(set()))
    print(bool(range(0)))
    print(bool(False))


def test2():
    print(bool(100))
    print(bool(100.99))
    print(bool('huangjian'))
    print(bool([1, 2, 3]))
    print(bool({1, 2, 3}))
    print(bool((1, 2, 3)))
    print(bool({"a": 1}))
    print(bool(range(10)))
    print(bool(True))


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
