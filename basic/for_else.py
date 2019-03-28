#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# for 和 while 循环后面可以跟上 else，如果是循环里面调用了 break，则该 else 不会被执行。

# Loop statements may have an else clause;
# it is executed when the loop terminates through exhaustion of the list (with for) or when the condition becomes
# false (with while),
# but not when the loop is terminated by a break statement.
# This is exemplified by the following loop, which searches for prime numbers:

def test1():
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n // x)
                break
        else:
            print(n, 'is a prime number')


def test2():
    print('\ntest2')
    i = 0
    while i < 10:
        i += 1
    else:
        print('i = ', i)


def test3():
    print('\ntest3')
    i = 0
    while i < 10:
        if i > 5:
            break
        i += 1
    else:
        print('else i = ', i) # 这里不会被执行到，因为在 while 循环中 break 了
    print('end i = ', i)


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
