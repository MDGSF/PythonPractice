#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import turtle as t


def main():
    t.color('red', 'yellow')
    t.begin_fill()
    while True:
        t.forward(200)
        t.left(170)
        if abs(t.pos()) < 1:
            break
    t.end_fill()
    t.done()


if __name__ == "__main__":
    main()
