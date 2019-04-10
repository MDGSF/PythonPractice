#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re


def str2int(strint):
    int32_max = pow(2, 31) - 1
    int32_min = -pow(2, 31)
    pattn = re.compile(r'^[-+]?[0-9]+')
    result = re.findall(pattn, strint.strip())
    if len(result) == 0:
        return 0
    t = int(result[0])
    if t > int32_max:
        return int32_max
    elif t < int32_min:
        return int32_min
    return t


def test1():
    print(str2int("42"))
    print(str2int("   -42"))
    print(str2int("4193 with words"))
    print(str2int("words and 987"))
    print(str2int("-91283472332"))


def main():
    test1()


if __name__ == "__main__":
    main()
