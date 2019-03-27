#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def test1():
    for i in range(3):
        print(i)

    print()
    for i in [1, 2, 3]:
        print(i)

    print()
    s = 'Python'
    for i, c in enumerate(s):
        print(i, c)

    print()
    for i, v in enumerate(range(3)):
        print(i, v)

    print()
    L = ['ann', 'bob', 'joe', 'john', 'mike']
    for i, v in enumerate(L):
        print(i, v)

    print()
    T = ('ann', 'bob', 'joe', 'john', 'mike')
    for i, v in enumerate(T):
        print(i, v)


def test2():
    print()
    T = ('ann', 'bob', 'joe', 'john', 'mike')
    for i, v in enumerate(sorted(T)):
        print(i, v)
    for i, v in enumerate(sorted(T, reverse=True)):
        print(i, v)

    print()
    T = ('ann', 'bob', 'joe', 'john', 'mike')
    for i, v in enumerate(reversed(T)):
        print(i, v)


def test3():
    # 同时迭代多个
    chars = 'abcdefghijklmnopqrstuvwxyz'
    nums = range(1, 27)
    for c, n in zip(chars, nums):
        print(c, n)


def test4():
    print('\ntest4')

    phonebook1 = {'ann': 6575, 'bob': 8982, 'joe': 2598, 'zoe': 1225, 'ann': 6585}
    for key in phonebook1:
        print(key, phonebook1[key])

    print()
    for key, value in phonebook1.items():
        print(key, value)


def main():
    test1()
    test2()
    test3()
    test4()


if __name__ == "__main__":
    main()
