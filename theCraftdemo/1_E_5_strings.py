#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def test1():
    # 字符转化为对应的码值
    print(ord('a'))
    print(chr(97))

def test2():
    # 字符串的4种表示方法
    s1 = 'Simple is better than complex.'
    print(s1)

    s2 = "Simple is better than complex."
    print(s2)

    s3 = '''Simple is better than complex.
Complex is better than complicated.'''
    print(s3)

    s4 = """
Simple is better than complex.
Complex is better than complicated.
"""
    print(s4)

def test3():
    print(int('3'))
    print(float('3'))
    print(str(3.1415926))


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
