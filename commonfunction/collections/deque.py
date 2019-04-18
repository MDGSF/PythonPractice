#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，
因为list是线性存储，数据量大的时候，插入和删除效率很低。
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：

append()
pop()

appendleft()
popleft()
"""

from collections import deque


def test1():
    q = deque(['a', 'b', 'c'])
    q.append('x')
    q.appendleft('y')
    print(q)


def main():
    test1()


if __name__ == "__main__":
    main()
