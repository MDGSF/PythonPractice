#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def factorial(n):
    return 1 if n == 1 else n * factorial(n - 1)


def main():
    print(factorial(5))


if __name__ == "__main__":
    main()
