#!/usr/bin/env python

# reduce 把一个函数作用在一个序列 [x1, x2, x3, ...] 上，这个函数必须接收两个参数，
# reduce 把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce


def add(x, y):
    return x + y


def test1():
    result = reduce(add, [1, 3, 5, 7, 9])
    print(result)


def test2():
    result = reduce(lambda x, y: x + y, [1, 3, 5, 7, 9])
    print(result)


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
