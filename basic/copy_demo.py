#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import copy


def test1():
    """
    copy.copy 只拷贝了一层
    copy.deepcopy 递归拷贝
    """

    a = [1, 2, 3, 4, ['a', 'b', 'c']]
    b = a
    c = copy.copy(a)
    d = copy.deepcopy(a)

    a.append(5)
    print(f'id(a) = {id(a)}, a = {a}')
    print(f'id(b) = {id(b)}, b = {b}')
    print(f'id(c) = {id(c)}, c = {c}')
    print(f'id(d) = {id(d)}, d = {d}')
    # id(a) = 140522664018056, a = [1, 2, 3, 4, ['a', 'b', 'c'], 5]
    # id(b) = 140522664018056, b = [1, 2, 3, 4, ['a', 'b', 'c'], 5]
    # id(c) = 140522636761864, c = [1, 2, 3, 4, ['a', 'b', 'c']]
    # id(d) = 140522636861896, d = [1, 2, 3, 4, ['a', 'b', 'c']]

    a[4].append('d')
    print(f'id(a) = {id(a)}, a = {a}')
    print(f'id(b) = {id(b)}, b = {b}')
    print(f'id(c) = {id(c)}, c = {c}')
    print(f'id(d) = {id(d)}, d = {d}')
    # id(a) = 140522664018056, a = [1, 2, 3, 4, ['a', 'b', 'c', 'd'], 5]
    # id(b) = 140522664018056, b = [1, 2, 3, 4, ['a', 'b', 'c', 'd'], 5]
    # id(c) = 140522636761864, c = [1, 2, 3, 4, ['a', 'b', 'c', 'd']]
    # id(d) = 140522636861896, d = [1, 2, 3, 4, ['a', 'b', 'c']]


def main():
    test1()


if __name__ == "__main__":
    main()
