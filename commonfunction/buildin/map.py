#!/usr/bin/env python

# map(function, iterable, ...)
#     Return an iterator that applies function to every item of iterable, yielding the results. If additional iterable arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel. With multiple iterables, the iterator stops when the shortest iterable is exhausted. For cases where the function inputs are already arranged into argument tuples, see itertools.starmap().

def f(x):
    return x * x


def test1():
    # map 把函数 f 作用在列表的每一个元素上，返回一个迭代器 Iterator
    # list 把迭代器计算出来，返回一个列表 result.
    result = list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(result)


def test2():
    # 转换为数字
    result = list(map(int, '12345'))
    print(result)


def test3():
    # 可以传多个 iterables
    result = list(map(lambda x, y: (x ** y, x + y), [1, 2, 3], [1, 2, 3]))
    print(result)


def test4():
    # Stops when the shortest iterable is exhausted.
    result = list(map(lambda x, y: (x ** y, x + y), [1, 2, 3], [1, 2]))
    print(result)


def test5():
    # origin 不会改变
    origin = ['adam', 'LISA', 'barT']
    result = list(map(lambda s: s.title(), origin))
    print(origin)
    print(result)


def main():
    test1()
    test2()
    test3()
    test4()
    test5()


if __name__ == "__main__":
    main()
