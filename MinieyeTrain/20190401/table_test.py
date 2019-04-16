#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os
import unittest

try:
    from table import *
except:
    _src_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print('src_path', _src_path)
    sys.path.append(_src_path)


class TestTable(unittest.TestCase):

    def test_insert_remove(self):
        t = Table()
        for i in range(10):
            t.insert(i, i)
        self.assertEqual(len(t), 10)

        for i in range(10):
            self.assertTrue(t.exists(i))

        t.remove(100)
        self.assertEqual(len(t), 10)

        t.remove(1)
        self.assertEqual(len(t), 9)
        self.assertFalse(t.exists(1))

        t.remove(2)
        self.assertEqual(len(t), 8)
        self.assertFalse(t.exists(2))

        t.remove(3)
        self.assertEqual(len(t), 7)
        self.assertFalse(t.exists(3))

    def test_issubset(self):
        a = Table(1, 2, 3)
        b = Table(1, 4)
        c = Table(1)
        d = Table(1, 2)
        e = Table(1, 2, 3)

        self.assertFalse(b.issubset(a))
        self.assertTrue(c.issubset(a))
        self.assertTrue(d.issubset(a))
        self.assertTrue(e.issubset(a))
        self.assertTrue(a.issubset(e))

    def test_insert(self):
        a = Table()
        for i in range(100):
            a.insert(i)
        self.check_table_keys(a, [i for i in range(100)])

        for i in range(99, 2, -1):
            a.remove(i)
            self.check_table_keys(a, [i for i in range(i)])

        self.check_table_keys(a, [0, 1, 2])

        a.remove(0)
        a.remove(1)
        a.remove(2)
        self.assertEqual(len(a), 0)

        for i in range(20):
            a.insert(i)
        self.check_table_keys(a, [i for i in range(20)])

    def check_table_keys(self, table, expectlist):
        outputlist = []
        for node in table:
            outputlist.append(node[0])
        outputlist.sort()

        len1 = len(outputlist)
        len2 = len(expectlist)
        self.assertEqual(len1, len2)

        i = 0
        while i < len1:
            self.assertEqual(outputlist[i], expectlist[i])
            i += 1

    def test_iter(self):
        a = Table(range(5))
        self.check_table_keys(a, [x for x in range(5)])

    def test_union(self):
        a = Table(1, 2, 3)
        b = Table(2, 3, 4, 5)
        c = a.union(b)
        self.check_table_keys(c, [1, 2, 3, 4, 5])

    # def test_str(self):
    #     a = Table(1, 2, 3)
    #     print('\ntable a =', a)

    def test_eq(self):
        a = Table(1, 2, 3)
        b = Table(1, 2, 3)
        c = Table(1)
        d = Table(1, 2)
        self.assertTrue(a == b)
        self.assertFalse(a == c)
        self.assertFalse(a == d)

    # 运行单个测试用例
    # python table_test.py -v TestTable.test_grow_shrink
    def test_grow_shrink(self):
        a = Table()
        self.assertEqual(a.t.capacity, 1)

        a.insert(1)
        self.assertEqual(a.t.capacity, 1)

        a.insert(2)
        self.assertEqual(a.t.capacity, 1)

        a.insert(3)
        self.assertEqual(a.t.capacity, 2)

        a.insert(4)
        self.assertEqual(a.t.capacity, 2)

        a.insert(5)
        self.assertEqual(a.t.capacity, 4)

        a.insert(6)
        self.assertEqual(a.t.capacity, 4)

        a.insert(7)
        self.assertEqual(a.t.capacity, 4)

        a.insert(8)
        self.assertEqual(a.t.capacity, 4)

        a.insert(9)
        self.assertEqual(a.t.capacity, 8)

    def test_get(self):
        a = Table()
        for i in range(10):
            a.insert(i, i)
        for i in range(10):
            self.assertEqual(a.get(i), i)

        a.insert("name", "huangjian")
        self.assertEqual(a.get("name"), "huangjian")

        a.remove("name")
        self.assertEqual(a.get("name"), None)

    def test_getitem(self):
        a = Table()
        for i in range(10):
            a.insert(i, i)
        for i in range(10):
            self.assertEqual(a[i], i)

        with self.assertRaises(KeyError):
            a[100]

        with self.assertRaises(TypeError):
            a[1:2]

    def test_setitem(self):
        a = Table()
        a["name"] = "huangjian"
        a["ID"] = 110
        self.assertEqual(a["name"], "huangjian")
        self.assertEqual(a["ID"], 110)

        a["ID"] = 120
        self.assertEqual(a["ID"], 120)

    def test_delitem(self):
        a = Table()
        a["name"] = "huangjian"
        self.assertEqual(a["name"], "huangjian")
        self.assertEqual(len(a), 1)

        del a["name"]
        with self.assertRaises(KeyError):
            a["name"]

        self.assertEqual(len(a), 0)

    def check_table_dict(self, table, expectdict):
        self.assertEqual(len(table), len(expectdict))

        for node in table:
            self.assertTrue(node[0] in expectdict)
            self.assertEqual(node[1], expectdict[node[0]])

    def test_update(self):
        a = Table(name="huangjian", ID=1)
        b = Table(ann=6575, name="huangping")
        a.update(b)
        self.check_table_dict(a, {
            "name": "huangping",
            "ID": 1,
            "ann": 6575})

    def test_max_min(self):
        """
        max(dict) return the max key.
        """
        phonebook1 = {'ann': 6575, 'bob': 8982, 'joe': 2598, 'zoe': 1225,
                      'ann': 6585}
        phonebook2 = {'john': 9876, 'mike': 5603, 'stan': 6898, 'eric': 7898}
        phonebook1.update(phonebook2)

        self.assertEqual(max(phonebook1), "zoe")
        self.assertEqual(min(phonebook1), "ann")


def main():
    unittest.main()


if __name__ == "__main__":
    main()
