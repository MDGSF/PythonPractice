#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# ascii 和 repr 都是用来返回一个方便阅读的字符串，处理非 ascii 字符的时候有点不同。


# ascii(object)
# As repr(), return a string containing a printable representation of an object,
# but escape the non-ASCII characters in the string returned by repr() using \x, \u or \U escapes.


def main():
    a_list = [1, 2, 3, 4]
    print(ascii(a_list))
    print(repr(a_list))

    d = {'huangjian': 1, 'pingpong': 2}
    print(ascii(d))
    print(repr(d))


if __name__ == "__main__":
    main()
