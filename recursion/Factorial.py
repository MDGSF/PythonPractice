#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# n 的阶乘
# n! = n * (n-1) * (n-2) ... * 3 * 2 * 1

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def main():
    print(factorial(5))


if __name__ == "__main__":
    main()
