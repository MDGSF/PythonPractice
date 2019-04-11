#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Node:
    def __init__(self, key, value):
        self.key = None
        self.value = None

class Table:
    """
    hashtable
    """

    def __init__(self, capacity=1 << 3):
        self.t = [None for i in range(capacity)]

    def insert(self, key, value):
        p = self.mainposition(key)
        if self.t[p] is None:
            self.t[p] = [Node(key, value)]
        else:
            # search key first
            self.t[p].append(Node(key, value))

    def mainposition(self, key):
        return hash(key) % len(self.t)



def test1():
    t = Table()
    print(t)


def main():
    test1()


if __name__ == "__main__":
    main()
