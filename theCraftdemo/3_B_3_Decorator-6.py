#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def a_decorator(func):
    def wrapper():
        print('We can do sth. before a func is called...')
        func()
        print('... and we can do sth. after it is called...')

    return wrapper # 这里不执行就直接返回


def a_func():
    print("Hi, I'm a_func!")


def main():
    a_func()

    result = a_decorator(a_func)
    print('result =', result) # 这里的 result 就是返回的内部 wrapper 函数

    # 输出:
    # Hi, I'm a_func!
    # result = <function a_decorator.<locals>.wrapper at 0x7f601ec132f0>



if __name__ == "__main__":
    main()
