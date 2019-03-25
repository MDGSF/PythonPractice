#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from graphviz import Digraph


def drawlist(g, l, name, ranklevel):
    if len(l) == 0:
        return

    with g.subgraph(name=name) as sub:
        sub.attr(rank='same')
        sub.attr(rankdir='LR')

        rankNodeName = 'rank' + str(ranklevel)

        sub.edge(rankNodeName, name+str(l[0]), style='invisible', color='white')
        i = 0
        while i < len(l) - 1:
            sub.edge(name+str(l[i]), name+str(l[i + 1]))
            i += 1

        sub.node(name=rankNodeName, style='invisible')
        for item in l:
            sub.node(name=name+str(item), label=str(item))


def main():
    g = Digraph('测试图片')

    l1 = [1, 2, 3, 4, 5]
    drawlist(g, l1, "l1", 0)

    l2 = [9, 8, 7]
    drawlist(g, l2, "l2", 1)

    rankStart = 0
    rankEnd = 1
    i = rankStart
    while i < rankEnd:
        rankNodeName1 = 'rank' + str(i)
        rankNodeName2 = 'rank' + str(i + 1)
        g.edge(rankNodeName1, rankNodeName2, style='invisible', color='white')
        i += 1

    g.view()


if __name__ == "__main__":
    main()
