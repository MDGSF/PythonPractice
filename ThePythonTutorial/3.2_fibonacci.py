#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def main():
    a, b = 0, 1
    while a < 10:
        print(a, end=',')
        a, b = b, a + b
    print()


if __name__ == "__main__":
    main()
