#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def a_decorator(func):
    def wrapper():
        print('We can do sth. before a func is called...')
        func()
        print('... and we can do sth. after it is called...')

    return wrapper() # 这里执行完了，返回


def a_func():
    print("Hi, I'm a_func!")


def main():
    a_func()

    result = a_decorator(a_func)
    print('result =', result)

    # 输出:
    # Hi, I'm a_func!
    # We can do sth. before a func is called...
    # Hi, I'm a_func!
    # ... and we can do sth. after it is called...
    # result = None



if __name__ == "__main__":
    main()
