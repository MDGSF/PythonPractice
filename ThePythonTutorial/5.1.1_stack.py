#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def test1():
    stack = [3, 4, 5]
    stack.append(6)
    stack.append(7)
    print(stack)

    t = stack.pop()
    print(t)
    print(stack)

    t = stack.pop()
    print(t)
    print(stack)


def main():
    test1()


if __name__ == "__main__":
    main()
