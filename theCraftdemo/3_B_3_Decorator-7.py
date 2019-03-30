#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@a_decorator
def a_func():
    ...

等价于

def a_func():
    ...
a_func = a_decorator(a_func)

也就是 a_func 变成了 a_decorator(a_func) 的返回值了，
也就是 a_func 指向了 wrapper 这个内部函数了
所以 a_func() 执行的时候，就是执行 wrapper() 这个函数了。
"""


def a_decorator(func):
    def wrapper():
        print('We can do sth. before a func is called...')
        func()
        print('... and we can do sth. after it is called...')

    return wrapper  # 这里不执行就直接返回


@a_decorator
def a_func():
    print("Hi, I'm a_func!")


def main():
    a_func()

    # 输出:
    # We can do sth. before a func is called...
    # Hi, I'm a_func!
    # ... and we can do sth. after it is called...


if __name__ == "__main__":
    main()
