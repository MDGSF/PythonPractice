#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def counter(start, stop):
    while start <= stop:
        yield start
        start += 1


def test1():
    for i in counter(101, 105):
        print(i, end=', ')
    print()


def test2():
    print('\ntest2')

    even = (e for e in range(10) if not e % 2)
    print(type(even))
    for e in even:
        print(e, end=', ')
    print()

    odd = [o for o in range(10) if o % 2]
    print(type(odd))
    for o in odd:
        print(o, end=', ')
    print()

    odd = {o for o in range(10) if o % 2}
    print(type(odd))
    for o in odd:
        print(o, end=', ')
    print()


def test3():
    print('\ntest3')

    # 计算 0~9 之间，所有偶数的和
    sum_of_even = sum(e for e in range(10) if not e % 2)
    print(sum_of_even)


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
