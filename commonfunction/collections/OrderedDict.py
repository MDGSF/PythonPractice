#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
如果要保持Key的顺序，可以用OrderedDict。
OrderedDict的Key会按照插入的顺序排列，不是Key本身排序。
"""

from collections import OrderedDict


def test1():
    d = dict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
    print(d)
    od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
    print(od)


def test2():
    od = OrderedDict()
    od['z'] = 1
    od['y'] = 1
    od['x'] = 1
    print(od.keys())  # odict_keys(['z', 'y', 'x'])
    od.popitem()


class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


def test3():
    print('\ntest3')
    od = LastUpdatedOrderedDict(3)
    od['a'] = 1
    od['b'] = 2
    od['c'] = 3
    print(od)

    od['d'] = 4
    print(od)

    od['c'] = 20
    print(od)


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
