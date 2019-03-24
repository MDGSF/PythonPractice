#!/usr/bin/env python

# map(function, iterable, ...)¶
#
#     Return an iterator that applies function to every item of iterable, yielding the results. If additional iterable arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel. With multiple iterables, the iterator stops when the shortest iterable is exhausted. For cases where the function inputs are already arranged into argument tuples, see itertools.starmap().

def f(x):
    return x * x


def main():
    # map 把函数 f 作用在列表的每一个元素上，返回一个迭代器 Iterator
    # list 把迭代器计算出来，返回一个列表 result.
    result = list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(result)


if __name__ == "__main__":
    main()
