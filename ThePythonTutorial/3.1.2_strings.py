#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def test1():
    print('C:\some\name')
    print(r'C:\some\name')  # 不转义


def test2():
    print('\ntest2')

    print("""\
    Usage: thingy [OPTIONS]
         -h                        Display this usage message
         -H hostname               Hostname to connect to
    """)


def test3():
    print('\ntest3')

    text = ('Put several strings within parentheses '
            'to have them joined together.')
    print(text)


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
