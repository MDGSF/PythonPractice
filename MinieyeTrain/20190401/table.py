#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
from collections import Iterable


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def __str__(self):
        return "(" + str(self.key) + ", " + str(self.value) + ")"


class InnerTableIter:
    """
    InnerTableIter is iterater for InnerTable.
    """

    def __init__(self, t):
        self.table = t
        self.currentIdx1 = None
        self.currentIdx2 = None
        self.currentNode = None
        if len(t) > 0:
            self.first()

    def __iter__(self):
        return self

    def __next__(self):
        if self.table is None \
                or self.currentIdx1 is None \
                or self.currentIdx2 is None \
                or self.currentNode is None:
            raise StopIteration
        else:
            k = self.currentNode.key
            v = self.currentNode.value

            while True:
                if self.currentIdx1 >= len(self.table.table):
                    self.currentIdx1 = None
                    self.currentIdx2 = None
                    self.currentNode = None
                    break
                if self.table.table[self.currentIdx1] is None:
                    self.currentIdx1 += 1
                    self.currentIdx2 = -1
                    continue

                l = self.table.table[self.currentIdx1]
                if self.currentIdx2 < len(l) - 1:
                    self.currentIdx2 += 1
                    self.currentNode = \
                        self.table.table[self.currentIdx1][self.currentIdx2]
                    break
                else:
                    self.currentIdx1 += 1
                    self.currentIdx2 = -1
            return k, v

    def first(self):
        if len(self.table.table) == 0:
            self.currentIdx1 = None
            self.currentIdx2 = None
            self.currentNode = None
            return

        self.currentIdx1 = 0
        self.currentIdx2 = 0
        while True:
            if self.currentIdx1 >= len(self.table.table):
                break
            if self.table.table[self.currentIdx1] is None:
                self.currentIdx1 += 1
                self.currentIdx2 = 0
                continue

            l = self.table.table[self.currentIdx1]
            if self.currentIdx2 < len(l):
                break
            else:
                self.currentIdx1 += 1
                self.currentIdx2 = 0

        self.currentNode = self.table.table[self.currentIdx1][self.currentIdx2]


class InnerTable:
    def __init__(self, capacity=1):
        if capacity < 0:
            capacity = 0
        self.len = 0
        self.capacity = capacity
        self.table = [None for i in range(capacity)]

    def init(self, capacity=1):
        self.len = 0
        self.capacity = capacity
        self.table = [None for i in range(capacity)]

    def insert(self, key, value=None):
        if self.capacity == 0:
            return
        p = mainposition(self.capacity, key)
        if self.table[p] is None:
            self.table[p] = [Node(key, value)]
            self.len += 1
        else:
            for node in self.table[p]:
                if node.key == key:
                    node.value = value
                    break
            else:
                self.table[p].append(Node(key, value))
                self.len += 1

    def remove(self, key):
        if self.len == 0 or self.capacity == 0:
            return
        p = mainposition(self.capacity, key)
        if self.table[p] is None:
            return
        for i, node in enumerate(self.table[p]):
            if node.key == key:
                del self.table[p][i]
                self.len -= 1
                return

    def exists(self, key):
        if self.len == 0 or self.capacity == 0:
            return False
        p = mainposition(self.capacity, key)
        if self.table[p]:
            for node in self.table[p]:
                if node.key == key:
                    return True
        return False

    def get(self, key):
        if self.len == 0 or self.capacity == 0:
            return None, False
        p = mainposition(self.capacity, key)
        if self.table[p]:
            for node in self.table[p]:
                if node.key == key:
                    return node.value, True
        return None, False

    def __len__(self):
        """support len(obj)"""
        return self.len

    def __iter__(self):
        """support iterable, ex. for i in table:"""
        return InnerTableIter(self)

    def __str__(self):
        result = ""

        result += "["
        for slot in self.table:
            if slot is None:
                result += "None, "
            else:
                result += "["
                for node in slot:
                    result += str(node) + ", "
                result += "], "
        result += "]"
        return result


class TableIter:
    """
    TableIter is iterater for Table.
    """

    def __init__(self, t):
        self.table = t
        if len(self.table.oldt) == 0:
            self.isold = False
            self.current = self.table.t.__iter__()
        else:
            self.isold = True
            self.current = self.table.oldt.__iter__()

    def __iter__(self):
        return self

    def __next__(self):
        if self.isold:
            try:
                d = self.current.__next__()
                return d
            except StopIteration:
                self.isold = False
                self.current = self.table.t.__iter__()
                return self.current.__next__()
        else:
            return self.current.__next__()


class Table:
    """
    Table represents a hashtable.
    """

    def __init__(self, *args, capacity=1, **kwargs):
        self.oldt = InnerTable(capacity=0)
        self.t = InnerTable(capacity=capacity)

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
        """
        往 self 中插入 key=value
        """
        if self.__needGrow():
            self.__grow()
        self.t.insert(key, value)
        self.oldt.remove(key)
        self.__moveSomeOldToNew()

    def get(self, key):
        """
        get node(key:value) from table, return value.
        """

        # find in new table
        result = self.t.get(key)
        if result[1]:
            return result[0]

        # find in old table
        result = self.oldt.get(key)
        if result[1]:
            return result[0]

        # no found
        return None

    def exists(self, key):
        """
        判断 key 在 self 中是否存在。
        """
        return self.t.exists(key) or self.oldt.exists(key)

    def remove(self, key):
        """
        从 self 中删除 key。
        """
        self.t.remove(key)
        self.oldt.remove(key)
        if self.__needShrink():
            self.__shrink()
        self.__moveSomeOldToNew()

    def setdefault(self, key, default):
        """
        Insert key with a value of default if key is not in the dictionary.

        Return the value for key if key is in the dictionary, else default.
        """
        if self.exists(key):
            return self.get(key)
        else:
            self.insert(key, default)
            return default

    def issubset(self, other):
        """
        判断 self 是否是 other 的子集。
        """
        for node in self:
            if not other.exists(node[0]):
                return False
        return True

    def union(self, other):
        """
        返回一个新的 table，这个新的 table 是 self 和 other 的合并。
        """
        newt = Table(capacity=len(self) + len(other))
        merge1(self.oldt, newt.t)
        merge1(self.t, newt.t)
        merge1(other.oldt, newt.t)
        merge1(other.t, newt.t)
        return newt

    def update(self, other):
        """
        use other Table to update self.
        """
        for node in other.t:
            self.t.insert(node[0], node[1])

    def __moveSomeOldToNew(self):
        """
        move some node from self.oldt to self.t
        """
        if len(self.oldt) > 0:
            MilliTime = lambda: int(round(time.time() * 1000))
            startTime = MilliTime()
            i = 0
            for node in self.oldt:
                self.t.insert(node[0], node[1])
                self.oldt.remove(node[0])
                i += 1
                if i > 10:
                    curTime = MilliTime()
                    if curTime - startTime > 100:
                        break
            if len(self.oldt) == 0:
                self.oldt.init()

    def __needGrow(self):
        """
        判断是否需要动态扩容。
        """
        if self.t.len > int(self.t.capacity * 1.5):
            return True
        return False

    def __grow(self):
        if len(self.oldt) > 0:
            merge2(self.oldt, self.t)
        self.oldt = self.t
        self.t = InnerTable(capacity=self.oldt.capacity * 2)
        # print('grow, t.capacity=', self.t.capacity)

    def __needShrink(self):
        """
        判断是否需要减少空间占用。
        """
        if (len(self.oldt) + len(self.t)) * 5 < self.t.capacity:
            return True
        return False

    def __shrink(self):
        if len(self.oldt) > 0:
            merge1(self.t, self.oldt)
        else:
            self.oldt = self.t
        self.t = InnerTable(capacity=self.oldt.capacity // 2)

    def __len__(self):
        """support len(obj)"""
        return len(self.t) + len(self.oldt)

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for node in self:
            if not other.exists(node[0]):
                return False
        return True

    def __iter__(self):
        """support iterable, ex. for i in table:"""
        return TableIter(self)

    def __getitem__(self, key):
        """support dict[key]"""
        value = self.get(key)
        if value is None:
            raise KeyError(key)
        return value

    def __setitem__(self, key, value):
        """support dict[key] = value"""
        self.insert(key, value)

    def __delitem__(self, key):
        """support del dict[key]"""
        self.remove(key)

    def __str__(self):
        return self.oldt.__str__() + "\n" + self.t.__str__()


def mainposition(maxsize, key):
    return hash(key) % maxsize


def merge1(table1, table2):
    """
    merge table1's data to table2.
    If table1 and table2 has the same key, remain table1, remove table2.
    """
    for node in table1:
        table2.insert(node[0], node[1])


def merge2(table1, table2):
    """
    merge table1's data to table2.
    If table1 and table2 has the same key, remain table2, remove table1.
    """
    for node in table1:
        if not table2.exists(node[0]):
            table2.insert(node[0], node[1])
