#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
re.sub(pattern, repl, string, count=0, flags=0)
"""

import re


def test1():
    result = re.sub(
        r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
        r'static PyObject*\npy_\1(void)\n',
        'def myfunc():'
    )
    print(result)


def test2():
    print('\ntest2')

    def dashrepl(matchobj):
        if matchobj.group(0) == '-':
            return ' '
        else:
            return '-'

    result = re.sub(
        '-{1,2}',
        dashrepl,
        'pro----gram-files'
    )
    print(result)


def test3():
    print('\ntest3')
    result = re.sub(
        r'\sAND\s',
        ' & ',
        'Baked Beans And Spam',
        flags=re.IGNORECASE
    )
    print(result)


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
