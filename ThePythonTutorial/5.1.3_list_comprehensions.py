#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from math import pi


def test1():
    squares = []
    for x in range(10):
        squares.append(x ** 2)
    print(squares)

    squares2 = list(map(lambda x: x ** 2, range(10)))
    print(squares2)

    squares3 = [x ** 2 for x in range(10)]
    print(squares3)


def test2():
    print('\ntest2')
    result = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    print(result)


def test3():
    print('\ntest3')
    vec = [-4, -2, 0, 2, 4]
    print(vec)
    print([x * 2 for x in vec])
    print([x for x in vec if x >= 0])
    print([abs(x) for x in vec])


def test4():
    print('\ntest4')
    freshfruit = ['  banana', '  loganberry', 'passion fruit   ']
    print([weapon.strip() for weapon in freshfruit])


def test5():
    print('\ntest5')
    print([(x, x ** 2) for x in range(6)])

    vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print([num for elem in vec for num in elem])


def test6():
    print('\ntest6')
    print([str(round(pi, i)) for i in range(1, 6)])


def test7():
    print('\ntest7')

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    result1 = [[row[i] for row in matrix] for i in range(4)]
    print(result1)

    print(*matrix)
    print(list(zip(*matrix)))


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
