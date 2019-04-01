#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from collections import deque


def test1():
    queue = deque(["Eric", "John", "Michael"])
    queue.append("Terry")
    queue.append("Graham")

    t = queue.popleft()
    print(t)
    print(queue)

    t = queue.popleft()
    print(t)
    print(queue)


def main():
    test1()


if __name__ == "__main__":
    main()
