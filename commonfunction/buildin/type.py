#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def main():
    print(type(0))
    print(type(1.2))
    print(type('a'))
    print(type("a"))

    a = {}
    b = set()
    c = []
    d = ()
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))


if __name__ == "__main__":
    main()
