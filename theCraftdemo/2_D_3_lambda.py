#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def _is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def test1():
    # 给函数取个别名

    year_leap_bool = _is_leap
    print(year_leap_bool)
    print(year_leap_bool(100))

    print(id(year_leap_bool))
    print(id(_is_leap))

    print(type(year_leap_bool))
    print(type(_is_leap))


def add(x, y):
    return x + y


def test2():
    print('\ntest2')

    print(add(3, 5))

    add_2 = lambda x, y: x + y
    print(add_2(3, 5))


# 返回一个 lambda 函数
def make_incrementor(n):
    return lambda x: x + n


def test3():
    print('\ntest3')

    # f 就是返回的 lambda 函数
    f = make_incrementor(42)
    print(f(0))
    print(f(1))

    print(f)
    print(id(f))
    print(id(make_incrementor))


def double_it(n):
    return n * 2


def test4():
    print('\ntest4')

    a_list = [1, 2, 3, 4, 5, 6]

    b_list = list(map(double_it, a_list))
    print(b_list)

    c_list = list(map(lambda x: x * 2, a_list))
    print(c_list)


def test5():
    print('\ntest5')

    phonebook = [
        {
            'name': 'john',
            'phone': 9876
        },
        {
            'name': 'mike',
            'phone': 5603
        },
        {
            'name': 'stan',
            'phone': 6898
        },
        {
            'name': 'eric',
            'phone': 7898
        }
    ]

    print(phonebook)
    print(list(map(lambda x: x['name'], phonebook)))
    print(list(map(lambda x: x['phone'], phonebook)))


def test6():
    print('\ntest6')
    a_list = [1, 3, 5]
    b_list = [2, 4, 6]
    print(list(map(lambda x, y: x * y, a_list, b_list)))


def test7():
    print('\ntest7')
    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    pairs.sort(key=lambda p: p[1])
    print(pairs)


def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()


if __name__ == "__main__":
    main()
