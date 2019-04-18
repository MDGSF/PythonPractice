#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import turtle as t

lv = 14 # 树的最大层级
s = 45 # 角度

# 颜色 (r, g, b)
r = 0
g = 0
b = 0


def draw_tree(l, level):
    """
    画出当前 level 的树枝
    :param l: 当前层级树枝的长度
    :param level: 当前层级
    """
    global r, g, b

    w = t.width()  # 保存当前画笔宽度

    t.width(w * 3.0 / 4.0)  # 把画笔的宽度变小一点

    r, g, b = r + 1, g + 2, b + 3  # 修改颜色
    t.pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l  # 修改当前树枝长度

    t.lt(s)  # 左转 s 度
    t.fd(l)  # 画出当前的第一个树枝，向左的那个树枝

    if level < lv:  # 如果当前的层级还没有达到最大的层级
        draw_tree(l, level + 1)  # 那就继续画下一个层级

    t.bk(l)  # 后退回到原来的位置
    t.rt(2 * s)  # 右转 2 倍的 s 度
    t.fd(l)  # 画出当前的第二个树枝，向右的那个树枝

    if level < lv:  # 如果当前的层级还没有达到最大的层级
        draw_tree(l, level + 1)  # 那就继续画下一个层级

    # 画完了子树枝，恢复现场
    t.bk(l)
    t.lt(s)
    t.width(w)


def main():
    t.colormode(255)  # 设置颜色模式
    t.lt(90)  # 左转 90 度
    t.width(lv)  # 设置画笔宽度
    t.pencolor(r, g, b)  # 设置画笔颜色

    l = 120

    t.penup()  # 提笔
    t.bk(l)  # 后退，方向不改变
    t.pendown()  # 落笔
    t.fd(l)  # 前进

    t.speed(0)  # 设置画笔速度

    draw_tree(l, 4)

    t.done()


if __name__ == "__main__":
    main()
