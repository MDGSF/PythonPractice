#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Node:
    def __init__(self, x):
        self.val = x


def test1():
    n = Node(10)
    print(n.val) # 10

    n.val = 20
    print(n.val) # 20

    def f(n):
        n.val = 30

    f(n)
    print(n.val) # 30，说明在函数内部的修改起作用了


def main():
    test1()


if __name__ == "__main__":
    main()
