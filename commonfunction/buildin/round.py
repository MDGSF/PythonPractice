#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# https://docs.python.org/3/library/functions.html#round


def main():
    f = 1.23456
    print(f)
    print(round(f)) # 取整数
    print(round(f, 2)) # 保留 2 位精度
    print(round(f, 3)) # 保留 3 位精度


if __name__ == "__main__":
    main()
