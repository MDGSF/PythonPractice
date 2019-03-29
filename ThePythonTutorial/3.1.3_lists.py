#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def test1():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(letters)

    letters[2:5] = ['C', 'D', 'E']
    print(letters)

    letters[2:5] = []
    print(letters)

    letters[:] = []
    print(letters)


def test2():
    print('\ntest2')

    a = ['a', 'b', 'c']
    n = [1, 2, 3]
    x = [a, n]
    print(x)
    print(x[0])
    print(x[0][1])


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
