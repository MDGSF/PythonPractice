#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# filter() 把传入的函数依次作用于每个元素，然后根据返回值是 True 还是 False 决定保留还是丢弃该元素。

import math

def test1():
    # 过滤出奇数
    print(list(filter(lambda n: n % 2 == 1, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

    # 过滤掉空字符串
    print(list(filter(lambda s: s and s.strip(), ['a', '', 'B', None, 'C', ' '])))

    # 过滤出 1~100 中平方根是整数的数字
    print(list(filter(lambda x: math.sqrt(x) % 1 == 0, range(1, 101))))


def main():
    test1()


if __name__ == "__main__":
    main()
