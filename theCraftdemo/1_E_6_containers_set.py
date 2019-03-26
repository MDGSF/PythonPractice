#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def test1():
    primes = {2, 3, 5, 7, 11, 13, 17}
    print(type(primes), primes)

    a = {}  # 这个是空的字典
    print(type(a), a)

    b = set()  # 这个是空的 set
    print(type(b), b)


def test2():
    print()

    a = "abcabcdeabcdbcdef"
    b = range(10)
    c = [1, 2, 2, 3, 3, 1]
    d = ('a', 'b', 'e', 'b', 'a')
    print(set(a))
    print(set(b))
    print(set(c))
    print(set(d))


def test3():
    print()

    a = "abcabcdeabcdbcdef"
    b = {x for x in a if x not in 'abc'}
    print(b)


def test4():
    print()

    admins = {'Moose', 'Joker', 'Joker'}
    moderators = {'Ann', 'Chris', 'Jane', 'Moose', 'Zero'}

    print(admins)
    print(moderators)
    print('Joker' in admins)
    print('Joker' in moderators)

    # 并集
    print(admins | moderators)

    # 交集 in both admins and moderators
    print(admins & moderators)

    # 差集, in admins but not in moderators
    print(admins - moderators)

    # 对称差集 in admins or moderators but not both
    print(admins ^ moderators)


def test5():
    print('\ntest5')

    admins = {'Moose', 'Joker', 'Joker'}
    moderators = {'Ann', 'Chris', 'Jane', 'Moose', 'Zero'}

    # 并集
    print(admins.union(moderators))

    # 交集
    print(admins.intersection(moderators))

    # 差集
    print(admins.difference(moderators))

    # 对称差集
    print(admins.symmetric_difference(moderators))


def test6():
    # 去重

    print('\ntest6')

    l = [1, 1, 1, 2, 3, 3, 3]
    new_list = list(set(l))
    print(new_list)


def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()


if __name__ == "__main__":
    main()
