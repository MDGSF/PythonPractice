#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class MyStack:
    def __init__(self, *args):
        self.innerList = []

    def append(self, x):
        self.innerList.append(x)

    def remove(self, x):
        self.remove(x)

    def pop(self):
        pass

    def index(self, x):
        pass

    def __len__(self):
        pass

    def __eq__(self, other):
        pass

    def __str__(self):
        pass


def test_mylist():
    a = MyStack(1, 2, 3)
    assert len(a) == 3

    x = a.pop()
    assert x == 3

    a.append(4)
    print(a)
    # [1, 2, 4]

    a.remove(2)
    print(a)
    # [1, 4]

    i = a.index(4)
    assert i == 2

    b = MyStack(1, 4)
    c = MyStack(4, 1)
    assert a == b
    assert b != c


def main():
    test_mylist()


if __name__ == "__main__":
    main()
