#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# https://docs.python.org/3/library/functions.html#open


import os


def test1():
    f = open('test-file.txt', 'w')
    print(f.name)

    if os.path.exists(f.name):
        os.remove(f.name)
        print(f'{f.name} deleted.')
    else:
        print(f'{f.name} does not exist.')


def test2():
    print('\ntest2')

    f = open('test-file.txt', 'w')
    f.write('first line\nsecond line\nthird line\n')
    f.close()

    f = open('test-file.txt', 'r')
    s = f.read()
    print(s)

    if os.path.exists(f.name):
        os.remove(f.name)
        print(f'{f.name} deleted.')
    else:
        print(f'{f.name} does not exist.')


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
