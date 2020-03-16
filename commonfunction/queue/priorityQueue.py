#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
https://docs.python.org/3/library/queue.html#queue.PriorityQueue
"""

from queue import PriorityQueue


def test1():
  q = PriorityQueue()
  q.put((1, "huangjian"))
  q.put((-2, "huangping"))
  q.put((3, "all"))
  while q.qsize() > 0:
    print(q.get())


def main():
  test1()


if __name__ == "__main__":
  main()
