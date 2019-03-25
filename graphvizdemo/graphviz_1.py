#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from graphviz import Digraph


def main():
    g = Digraph('测试图片')
    g.node(name='a', color='red')
    g.node(name='b', color='blue')
    g.edge('a', 'b', color='green')
    g.view()


if __name__ == "__main__":
    main()
