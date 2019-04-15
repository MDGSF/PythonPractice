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


class TestList(unittest.TestCase):

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


def main():
    unittest.main()


if __name__ == "__main__":
    main()
