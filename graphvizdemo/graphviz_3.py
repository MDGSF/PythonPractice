#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# use graphviz to print bubble sort.

from graphviz import Digraph


def drawlist(g, l, name, ranklevel, swapidx):
    if len(l) == 0:
        return

    with g.subgraph(name=name) as sub:
        sub.attr(rank='same')
        sub.attr(rankdir='LR')

        rankNodeName = 'rank' + str(ranklevel)

        sub.edge(rankNodeName, name + str(l[0]), style='invisible', color='white')
        i = 0
        while i < len(l) - 1:
            sub.edge(name + str(l[i]), name + str(l[i + 1]))
            i += 1

        sub.node(name=rankNodeName, style='invisible')
        i = 0
        while i < len(l):
            if i == swapidx or i == swapidx + 1:
                sub.node(name=name + str(l[i]), label=str(l[i]), color='green')
            else:
                sub.node(name=name + str(l[i]), label=str(l[i]))
            i += 1


def bublesort(l):
    g = Digraph('测试图片')

    level = 0
    drawlist(g, l, "l", level, -100)
    level += 1

    i = len(l) - 1
    while i >= 0:

        j = 0
        while j < i:
            if l[j] > l[j + 1]:
                t = l[j]
                l[j] = l[j + 1]
                l[j + 1] = t
                drawlist(g, l, "l" + str(i) + str(j), level, j)
                level += 1
            j += 1

        i -= 1

    rankStart = 0
    rankEnd = level
    i = rankStart
    while i < rankEnd - 1:
        rankNodeName1 = 'rank' + str(i)
        rankNodeName2 = 'rank' + str(i + 1)
        g.edge(rankNodeName1, rankNodeName2, style='invisible', color='white')
        i += 1

    g.view()


def main():
    l = [5, 4, 3, 2, 1]
    bublesort(l)


if __name__ == "__main__":
    main()
