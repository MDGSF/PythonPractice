#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def do_something():
    print("This is a hello from do_something().")


def test1():
    # 没有 return 的函数，默认返回 None。
    # None 如果放在 if 中，就是 False。
    print(do_something())


# 根据闰年的定义：
#   年份应该是 4 的倍数；
#   年份能被 100 整除但不能被 400 整除的，不是闰年。
# 所以，相当于要在能被 4 整除的年份中，排除那些能被 100 整除却不能被 400 整除的年份。
def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0 and year % 400 != 0:
            leap = False
    return leap


# cpython/Lib/datetime.py
def _is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def test2():
    print('\ntest2')
    for i in range(1, 100):
        if is_leap(i) != _is_leap(i):
            print(i, is_leap(i), _is_leap(i))
            break
    else:
        print('is_leap is the same with _is_leap')


def fib_between(start, end):
    r = []
    a, b = 0, 1
    while a < end:
        if a >= start:
            r.append(a)
        a, b = b, a + b
    return r


def test3():
    print('\ntest3')
    print(fib_between(100, 10000))


def be_careful(a, b):
    a = 2
    b[0] = "What?"
    print('be_careful a =', a)
    print('be_careful b =', b)


def test4():
    print('\ntest4  ')
    a = 1
    b = [1, 2, 3]
    be_careful(a, b)
    print('a =', a)
    print('b =', b)


def main():
    test1()
    test2()
    test3()
    test4()


if __name__ == "__main__":
    main()
