#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from collections import Iterable
import types


def fn():
    pass


class Animal:
    def __init__(self):
        pass


class Dog(Animal):
    pass


class Husky(Dog):
    pass


a = Animal()
d = Dog()
h = Husky()


def test1():
    print(type([1, 2, 3]))
    print(type((1, 2, 3)))
    print(type(123))
    print(type(123.45))
    print(type('str'))
    print(type(None))
    print(type(abs))
    print(type(a))

    print(type([1, 2, 3]) == list)
    print(type((1, 2, 3)) == tuple)
    print(type({1, 2, 3}) == set)
    print(type({"huangjian": 1}) == dict)
    print(type(123) == int)
    print(type(123.45) == float)
    print(type('str') == str)
    print(type(fn) == types.FunctionType)
    print(type(abs) == types.BuiltinFunctionType)
    print(type(lambda x: x) == types.LambdaType)
    print(type(x for x in range(10)) == types.GeneratorType)


def test2():
    print('\ntest2')
    print(isinstance(h, Husky))  # True
    print(isinstance(h, Dog))  # True
    print(isinstance(h, Animal))  # True

    print(isinstance(d, Husky))  # False

    print(isinstance('a', str))  # True
    print(isinstance(123, int))  # True
    print(isinstance(b'a', bytes))  # True

    # 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
    print(isinstance([1, 2, 3], (list, tuple)))  # True
    print(isinstance((1, 2, 3), (list, tuple)))  # True


def test3():
    print('\ntest3')
    print(isinstance('abc', Iterable))
    print(isinstance([1, 2, 3], Iterable))
    print(isinstance((1, 2, 3), Iterable))
    print(isinstance({1, 2, 3}, Iterable))
    print(isinstance({"huangjian": 1}, Iterable))
    print(isinstance(1, Iterable))
    print(isinstance(1.2, Iterable))


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
