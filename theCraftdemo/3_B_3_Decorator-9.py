#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
装饰带有参数的函数
"""


def trace(func):
    def wrapper(*args, **kwargs):
        print(f"Trace: You've called a function: {func.__name__}(),"
              f"with args: {args}; kwargs: {kwargs}")
        original_result = func(*args, *kwargs)
        print(f"Trace: {func.__name__}{args} returned: {original_result}")
        return original_result

    return wrapper


@trace
def say_hi(greeting, name=None):
    return greeting + '! ' + name + '.'


def main():
    print(say_hi('Hello', 'Jack'))


if __name__ == "__main__":
    main()
