#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# bin(x)
#   Convert an integer number to a binary string prefixed with “0b”.


def test1():
    # 0b11
    print(bin(3))

    # 0b1010
    print(bin(10))

    # -0b1010
    print(bin(-10))


def test2():
    # 如果不想要 0b 这个前缀，可以用 format 或者 f-string

    # 0b1110 1110
    print(format(14, '#b'), format(14, 'b'))

    # 0b1110 1110
    print(f'{14:#b}', f'{14:b}')


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
