#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys

try:
    import table
except:
    _src_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print('src_path', _src_path)
    sys.path.append(_src_path)


class MySet:
    def __init__(self, *args):
        self.t = table.Table(args)

    def add(self, x):
        self.t.insert(x)

    def remove(self, x):
        self.t.remove(x)

    def has(self, x):
        return self.t.exists(x)

    def issubset(self, other):
        return self.t.issubset(other.t)

    def union(self, other):
        newset = MySet()
        newset.t = self.t.union(other.t)
        return newset

    def __eq__(self, other):
        return self.t == other.t

    def __str__(self):
        output = []
        for node in self.t:
            output.append(node[0])
        return str(output)


def main():
    s = MySet()
    s.add(1)
    s.add(2)
    print(s) #[1, 2]

    s.remove(1)
    print(s) #[2]

    s.add(1)
    print(s) #[1, 2]

    print(s.has(1)) # True

    b = MySet(1)
    print(b.issubset(s)) # True

    c = MySet(2, 3, 4, 5)
    d = c.union(s)
    print(d) # [1, 2, 3, 4, 5]

    e = MySet(1, 2, 3, 4, 5)
    print(d == e) # True


if __name__ == "__main__":
    main()
