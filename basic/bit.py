#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def test1():
    a = 60 # 0011 1100
    b = 13 # 0000 1101
    print(f'a = {a}')
    print(f'b = {b}')

    # 0000 1100
    print(f'a & b = {a & b}') # 12

    # 0011 1101
    print(f'a | b = {a | b}') # 61

    # 0011 0001
    print(f'a ^ b = {a ^ b}') # 49

    # 1100 0011
    print(f'~a = {~a}')

    print(f'1 << 10 = {1 << 10}') # 1024


def main():
    test1()


if __name__ == "__main__":
    main()
