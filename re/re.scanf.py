#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
scanf() Token         Regular Expression
%c                    .
%5c                   .{5}
%d                    [-+]?\d+
%e, %E, %f, %g        [-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?
%i                    [-+]?(0[xX][\dA-Fa-f]+|0[0-7]*|\d+)
%o                    [-+]?[0-7]+
%s                    \S+
%u                    \d+
%x, %X                [-+]?(0[xX])?[\dA-Fa-f]+
"""

import re


def test1():
    """测试 %s, %u"""
    inputString = '/usr/sbin/sendmail - 0 errors, 4 warnings'
    pattern = re.compile(r'(\S+) - (\d+) errors, (\d+) warnings')
    match = pattern.match(inputString)
    if match is not None:
        print(f'match.groups() = {match.groups()}')
        print(f'match.group() = {match.group()}')
        print(f'match.group(0) = {match.group(0)}')
        print(f'match.group(1) = {match.group(1)}')
        print(f'match.group(2) = {match.group(2)}')
        print(f'match.group(3) = {match.group(3)}')


def test2():
    """测试 %c ，单个字符"""
    print('\ntest2')
    inputString = 'this is for test'
    pattern = re.compile(r'.')
    match = pattern.match(inputString)
    if match is not None:
        print(f'match.groups() = {match.groups()}')
        print(f'match.group() = {match.group()}')
        print(f'match.group(0) = {match.group(0)}')


def test3():
    """测试 %c ，单个字符"""
    print('\ntest3')
    inputString = 'this is for test'
    pattern = re.compile(r'(.)')  # 这个加了括号之后，才是在一个 group 中
    match = pattern.match(inputString)
    if match is not None:
        print(f'match.groups() = {match.groups()}')
        print(f'match.group() = {match.group()}')
        print(f'match.group(0) = {match.group(0)}')
        print(f'match.group(1) = {match.group(1)}')


def test4():
    """测试 %e, %E, %f, %g ，浮点数，科学计数法"""
    print('\ntest4')
    inputString = '+200.3721'
    pattern = re.compile(r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?')
    match = pattern.match(inputString)
    if match is not None:
        print(f'match.group() = {match.group()}')


def test5():
    """测试 %i ，十六进制、八进制、十进制"""
    print('\ntest5')

    pattern = re.compile(r'[-+]?(0[xX][\dA-Fa-f]+|0[0-7]*|\d+)')

    match = pattern.match('0xAA55')
    if match is not None:
        print(f'match.group() = {match.group()}')

    match = pattern.match('234.56')
    if match is not None:
        print(f'match.group() = {match.group()}')


def test6():
    """测试 %o ，八进制"""
    print('\ntest6')
    pattern = re.compile(r'[-+]?[0-7]+')
    match = pattern.match('0756')
    if match is not None:
        print(f'match.group() = {match.group()}')


def test7():
    """测试 %u ，正整数"""
    print('\ntest7')
    pattern = re.compile(r'\d+')
    match = pattern.match('756')
    if match is not None:
        print(f'match.group() = {match.group()}')

    # match 匹配是从字符串的起始位置开始匹配的，遇到不匹配的就结束了
    match = pattern.match('-756')
    if match is not None:
        print(f'match.group() = {match.group()}') # 不匹配，所以没有输出


def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()


if __name__ == "__main__":
    main()
