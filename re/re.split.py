#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
re.split(pattern, string, maxsplit=0, flags=0)
"""

import re


def test1():
    # 按空白字符切割
    result = re.split(r'\W+', 'Words, words, words')
    print(result)  # ['Words', 'words', 'words']

    # 原字符串的末尾匹配到了，会在返回的列表的最后一个加个空字符串。
    result = re.split(r'\W+', 'Words, words, words.')
    print(result)  # ['Words', 'words', 'words', '']

    # 加了括号之后，会把匹配到的一起返回
    result = re.split(r'(\W+)', 'Words, words, words.')
    print(result)  # ['Words', ', ', 'words', ', ', 'words', '.', '']


def test2():
    print('\ntest2')

    result = re.split(r'[a-f]+', '0a3B9')
    print(result)  # ['0', '3B9']

    # 忽略大小写
    result = re.split(r'[a-f]+', '0a3B9', flags=re.IGNORECASE)
    print(result)  # ['0', '3', '9']

    # 忽略大小写
    # 加了括号之后，会把匹配到的一起返回
    result = re.split(r'([a-f]+)', '0a3B9', flags=re.IGNORECASE)
    print(result)  # ['0', 'a', '3', 'B', '9']


def test3():
    print('\ntest3')

    # 原字符串的头部匹配了，返回的列表最开始会多一个空字符串。
    # 原字符串的末尾匹配到了，会在返回的列表的最后一个加个空字符串。

    result = re.split(r'\W+', '...words, words...')
    print(result)  # ['', 'words', 'words', '']

    result = re.split(r'\W+', 'words, words...')
    print(result)  # ['words', 'words', '']

    result = re.split(r'\W+', '...words, words')
    print(result)  # ['', 'words', 'words']

    result = re.split(r'\W+', 'words, words')
    print(result)  # ['words', 'words']

    result = re.split(r'(\W+)', '...words, words...')
    print(result)  # ['', '...', 'words', ', ', 'words', '...', '']

    result = re.split(r'(\W+)', 'words, words...')
    print(result)  # ['words', ', ', 'words', '...', '']

    result = re.split(r'(\W+)', '...words, words')
    print(result)  # ['', '...', 'words', ', ', 'words']

    result = re.split(r'(\W+)', 'words, words')
    print(result)  # ['words', ', ', 'words']


def test4():
    print('\ntest4')

    # maxsplit<0 返回的整个列表中就一个元素，就是原字符串
    # maxsplit=0 默认全部切割
    # maxsplit>0 表示切割次数

    # 切割一次
    result = re.split(r'\W+', 'Words, words, words.', 1)
    print(result)  # ['Words', 'words, words.']

    # 切割 2 次
    result = re.split(r'\W+', 'Words, words, words, hello.', maxsplit=2)
    print(result)  # ['Words', 'words', 'words, hello.']

    # 直接返回整个字符串
    result = re.split(r'\W+', 'Words, words, words.', -1)
    print(result)  # ['Words, words, words.']


def main():
    test1()
    test2()
    test3()
    test4()


if __name__ == "__main__":
    main()
