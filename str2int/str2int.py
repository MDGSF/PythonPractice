#!/usr/bin/env python

from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9}


def char2num(c):
    return DIGITS[c]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


def main():
    result = str2int("12345")
    print(result)


if __name__ == "__main__":
    main()
