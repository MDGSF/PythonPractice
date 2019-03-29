#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Move only one disc at a time.
# Never place a larger disc on a smaller one.

# disc 的编号从 1 到 n
# left = true,  move n to left
# left = false, move n to right
def moves(n, left):
    if n == 0: return
    moves(n - 1, not left)
    print(n, " left" if left else " right")
    moves(n - 1, not left)


def main():
    moves(3, True)


if __name__ == "__main__":
    main()
