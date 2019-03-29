#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def bottle(n):
    if n == 0: return "no more bottles of beer"
    if n == 1: return "one bottle of beer"
    return str(n) + " bottles of beer"


def main():
    for i in range(100, 0, -1):
        print(bottle(i), "on the wall,")
        print(bottle(i) + ".")
        print("Take one down, pass it around,")
        print(bottle(i - 1), "on the wall.")


if __name__ == "__main__":
    main()
