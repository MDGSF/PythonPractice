#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os
import unittest

try:
    from iniparser import *
except:
    _src_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print('src_path', _src_path)
    sys.path.append(_src_path)

"""
指定运行单个测试用例
python iniparser_test.py -v TestIniParser.test3
"""


class TestIniParser(unittest.TestCase):

    def test1(self):
        p = IniParser()
        p.LoadFromFile("app.conf")
        self.assertEqual(p.getd("appname"), "annotations_tool")
        self.assertEqual(p.getd("httpaddr"), "127.0.0.1")
        self.assertEqual(p.getd("HostURL"), "http://127.0.0.1:8666")

    def test2(self):
        p = IniParser()
        p.LoadFromFile("app.conf")
        p.SaveToFile("newapp.ini")

    def test3(self):
        p = IniParser()
        p.LoadFromFile("test.ini")
        self.assertListEqual(p.sections(),
                             ['Section_a', 'Section_c', 'Section_b'])
        self.assertListEqual(p.items("Section_a"),
                             [('option_a1', 'apple_a1'),
                              ('option_a2', 'banana_a2')])

    def testReadAndWrite(self):
        p = IniParser()
        p.read("test.ini")
        p.write("test2.ini")
        p2 = IniParser()
        p2.read("test2.ini")
        self.assertListEqual(p.sections(), p2.sections())

        for sectionname in p.sections():
            self.assertListEqual(p.items(sectionname), p2.items(sectionname))

    def testRemove(self):
        p = IniParser()
        p.read("test.ini")

        self.assertTrue(p.hassection("Section_a"))
        p.remove("Section_a")
        self.assertFalse(p.hassection("Section_a"))

        self.assertTrue(p.hasKey("Section_b", "option_b2"))
        p.remove("Section_b", "option_b2")
        self.assertFalse(p.hasKey("Section_b", "option_b2"))

    def testAddSection(self):
        p = IniParser()
        p.addsection("section1")
        self.assertTrue(p.hassection("section1"))

    def testKeys(self):
        p = IniParser()
        p.read("test.ini")
        self.assertListEqual(p.keys("Section_a"), ["option_a1", "option_a2"])

    def testGetSet(self):
        p = IniParser()
        p.read("test.ini")
        p.set("Section_a", "name", "huangjian")
        self.assertTrue(p.hasKey("Section_a", "name"))
        self.assertEqual(p.get("Section_a", "name"), "huangjian")

        p.setd("globalname", "ghuangjian")
        self.assertTrue(p.hasKey("default", "globalname"))
        self.assertEqual(p.get("default", "globalname"), "ghuangjian")

    def testGetNotExistKey(self):
        p = IniParser()
        p.read("test.ini")

        self.assertEqual(p.get("not_exist_section", "aa"), "")

        self.assertEqual(p.get("Section_a", "not_exist_key"), "")


def main():
    pass


if __name__ == "__main__":
    main()
    unittest.main()
