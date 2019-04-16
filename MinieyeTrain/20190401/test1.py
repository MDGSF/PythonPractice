#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
import table
import random


def timeDeco(func):
    def wrapper(*args, **kwargs):
        MilliTime = lambda: int(round(time.time() * 1000))
        startTime = MilliTime()
        original_result = func(*args, *kwargs)
        endTime = MilliTime()
        useTime = endTime - startTime
        print(f'{func.__name__}, startTime = {startTime}, '
              f'endTime = {endTime}, '
              f'useTime = {useTime}ms')
        return original_result

    return wrapper


@timeDeco
def test1():
    a = {}
    for i in range(100000):
        num = random.randrange(1, 100000)
        a[num] = num


@timeDeco
def test2():
    a = table.Table()
    for i in range(100000):
        num = random.randrange(1, 100000)
        a[num] = num


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
