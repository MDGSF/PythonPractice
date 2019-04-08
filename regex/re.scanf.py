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
    inputString = '/usr/sbin/sendmail - 0 errors, 4 warnings'
    pattern = re.compile(r'(\S+) - (\d+) errors, (\d+) warnings')
    match = pattern.match(inputString)
    if match is not None:
        print(match.groups())


def main():
    test1()


if __name__ == "__main__":
    main()
