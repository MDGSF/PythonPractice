#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import turtle as t


def drawStar(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()

    t.seth(0)
    for i in range(5):
        t.fd(40)
        t.rt(144)


def main():
    for x in range(0, 250, 50):
        drawStar(x, 0)
    t.done()


if __name__ == "__main__":
    main()
