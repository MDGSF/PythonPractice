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
    # 类型转换
    print(int('3'))
    print(float('3'))
    print(str(3.1415926))


def test4():
    # 这三个是等价的
    print('He said, it\'s fine.')
    print("He said, it\'s fine.")
    print("He said, it's fine.")


def test5():
    # 这两个是等价的
    print('Hey!' + ' ' + 'You!')
    print('Hey!'  ' '  'You!')

    # output: lalala
    print("la" * 3)

    # output: True
    print('o' in 'Hey! You!')


def test6():
    s = 'Python'
    for i in range(len(s)):
        print(i, s[i])


def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()


if __name__ == "__main__":
    main()
