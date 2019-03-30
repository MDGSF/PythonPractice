#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# sum(iterable[, start])
# Sums start and the items of an iterable from left to right and returns the
#  total.
# start defaults to 0.
# The iterable’s items are normally numbers,
# and the start value is not allowed to be a string.


def test1():
    l = [1, 2, 3]
    print(sum(l))

    print(sum(l, 10))


def test2():
    print('\ntest2')

    # 计算 0~9 之间，所有偶数的和
    sum_of_even = sum(e for e in range(10) if not e % 2)
    print(sum_of_even)


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
