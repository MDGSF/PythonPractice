#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys

try:
    import list
except:
    _src_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print('src_path', _src_path)
    sys.path.append(_src_path)


class MyStack:
    def __init__(self, *args):
        self.l = list.List()
        for i in args:
            self.l.PushBack(i)

    def append(self, x):
        self.l.PushBack(x)

    def remove(self, x):
        e = self.l.Front()
        while e is not None:
            if e.value == x:
                self.l.Remove(e)
                break
            e = e.Next()

    def pop(self):
        back = self.l.Back()
        return self.l.Remove(back)

    def index(self, x):
        for i, v in enumerate(self.l):
            if v == x:
                return i
        return -1

    def __len__(self):
        return self.l.Len()

    def __eq__(self, other):
        return self.l == other.l

    def __str__(self):
        return self.l.__str__()


def test_mylist():
    a = MyStack(1, 2, 3)
    assert len(a) == 3

    x = a.pop()
    assert x == 3

    a.append(4)
    print('a =', a)
    # [1, 2, 4]

    a.remove(2)
    print('a =', a)
    # [1, 4]

    i = a.index(4)
    assert i == 1

    b = MyStack(1, 4)
    c = MyStack(4, 1)

    print('a =', a)
    print('b =', b)
    print('c =', c)

    assert a == b
    assert b != c


def main():
    test_mylist()


if __name__ == "__main__":
    main()
