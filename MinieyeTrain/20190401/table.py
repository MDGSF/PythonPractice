#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import copy
from collections import Iterable


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def __str__(self):
        return "(" + str(self.key) + ", " + str(self.value) + ")"


class Table:
    """
    hashtable
    """

    def __init__(self, *args, **kwargs):
        capacity = 1 << 3
        self.t = [None for i in range(capacity)]
        self.len = 0

        if len(args) > 0:
            for arg in args:
                if isinstance(arg, Iterable):
                    for x in arg:
                        self.insert(x)
                else:
                    self.insert(arg)

        for key, value in kwargs.items():
            self.insert(key, value)

    def insert(self, key, value=None):
        p = self.mainposition(key)
        if self.t[p] is None:
            self.t[p] = [Node(key, value)]
            self.len += 1
        else:
            for node in self.t[p]:
                if node.key == key:
                    node.value = value
                    break
            else:
                self.t[p].append(Node(key, value))
                self.len += 1

    def remove(self, key):
        p = self.mainposition(key)
        if self.t[p]:
            for i, node in enumerate(self.t[p]):
                if node.key == key:
                    del self.t[p][i]
                    self.len -= 1
                    break

    def exists(self, key):
        p = self.mainposition(key)
        if self.t[p]:
            for node in self.t[p]:
                if node.key == key:
                    return True
        return False

    def issubset(self, other):
        for slot in self.t:
            if slot is None:
                continue
            for node in slot:
                if not other.exists(node.key):
                    return False
        return True

    def union(self, other):
        """
        返回一个新的 table，这个新的 table 是 self 和 other 的合并。
        """
        pass

    def copy(self):
        """
        返回一个 table 的拷贝
        """
        newt = Table()
        newt.t = copy.deepcopy(self.t)
        newt.len = self.len
        return newt

    def mainposition(self, key):
        return hash(key) % len(self.t)

    def __len__(self):
        """support len(obj)"""
        return self.len

    def __str__(self):
        result = ""

        result += "["
        for slot in self.t:
            if slot is None:
                result += "None, "
            else:
                result += "["
                for node in slot:
                    result += str(node) + ", "
                result += "], "
        result += "]"
        return result
