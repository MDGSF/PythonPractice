#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def test1():
    i = iter("Python")
    print(type(i))

    s = iter((1, 2, 3, 4, 5))
    print(s)

    L = iter(['item 1', 'item 2', 3, 5])
    print(type(L))

    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    # print(next(i)) # 这里再调用，会有 StopIteration 错误


class Counter(object):
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        c = self.current
        self.current += 1
        return c


def test2():
    print('\ntest2')

    print(type(Counter))

    c = Counter(11, 20)
    print(next(c))
    print(next(c))
    print(next(c))

    for c in Counter(101, 105):
        print(c, end=', ')
    print()

    c = Counter(201, 203)
    while True:
        try:
            print(next(c), end=', ')
        except StopIteration:
            break
    print()


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
