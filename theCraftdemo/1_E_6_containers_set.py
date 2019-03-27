#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def test1():
    print('\ntest1')

    primes = {2, 3, 5, 7, 11, 13, 17}
    print(type(primes), primes)

    a = {}  # 这个是空的字典
    print(type(a), a)

    b = set()  # 这个是空的 set
    print(type(b), b)


def test2():
    print('\ntest2')

    a = "abcabcdeabcdbcdef"
    b = range(10)
    c = [1, 2, 2, 3, 3, 1]
    d = ('a', 'b', 'e', 'b', 'a')
    print(set(a))
    print(set(b))
    print(set(c))
    print(set(d))


def test3():
    print('\ntest3')

    a = "abcabcdeabcdbcdef"
    b = {x for x in a if x not in 'abc'}
    print(b)


def test4():
    print('\ntest4')

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


def test7():
    print('\ntest7')

    a = {1, 2, 3}
    b = {1, 2, 3}
    c = {1, 2, 3, 4}
    d = {7, 8, 9}
    print('a =', a)
    print('b =', b)
    print('c =', c)
    print('d =', d)

    print('a == b', a == b)  # a 和 b 相等
    print('a != c', a != c)  # a 和 b 不相等

    # a 和 d 不重合，即 a & d == None
    print('a.isdisjoint(d)', a.isdisjoint(d))

    # a 是 b 的子集，即 a <= b
    print('a.issubset(b)', a.issubset(b))
    print('a.issubset(c)', a.issubset(c))

    # a 是 c 的真子集，即 a < c
    print('a < b', a < b)  # False
    print('a < c', a < c)  # True

    # 超集，b >= a, c >= a
    print('b.issubset(a)', b.issubset(a))
    print('c.issuperset(a)', c.issuperset(a))

    # 真超集，c > a
    print('b > a', b > a)  # False
    print('c > a', c > a)  # True


def test8():
    print('\ntest8')

    a = {1, 2, 3, 4, 5}
    print(a)

    a.add(1)
    print(a)

    a.add(100)
    print(a)

    # 如果不存在，会抛出 KeyError
    a.remove(100)
    print(a)

    # 如果不存在，什么都不做
    a.discard(1)
    a.discard(200)
    print(a)

    # 随机 pop 一个元素出来
    t = a.pop()
    print(t)
    print(a)

    # 清空
    a.clear()
    print(a)


def test9():
    print('\ntest9')

    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    print(a)
    print(b)

    # 把 b 中的所有元素加入 a
    a.update(b)
    print(a)
    print(b)


def test10():
    print('\ntest10')

    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    print(a)
    print(b)

    # 更新 a ，保留同时存在于 a 和 b 中的元素
    a.intersection_update(b)
    print(a)
    print(b)


def test11():
    print('\ntest11')

    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    print(a)
    print(b)

    # 更新 a ，删除在 b 中存在的元素
    a.difference_update(b)
    print(a)
    print(b)


def test12():
    print('\ntest12')

    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    print(a)
    print(b)

    # set.symmetric_difference_update(_other_)
    # 更新 set, 只保留存在于 set 或 other 中的元素，但不保留同时存在于 set 和 other 中的元素
    a.symmetric_difference_update(b)
    print(a)
    print(b)


def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    test10()
    test11()
    test12()


if __name__ == "__main__":
    main()
