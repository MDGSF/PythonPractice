#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# https://docs.python.org/3/library/stdtypes.html#typesseq-range
# range(stop)
# range(start, stop[, step])

def main():
    print(range(10))

    print(list(range(10)))

    print(tuple(range(10)))

    print(list(range(20, 25)))

    # 0 到 20 之间的偶数
    print(list(range(0, 20, 2)))

    # 0 到 20 之间的奇数
    print(list(range(1, 20, 2)))

    print(list(range(0, 50, 5)))

    print(list(range(0, -10, -1)))


if __name__ == "__main__":
    main()
