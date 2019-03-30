#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 在函数内部定义函数

def a_func():

    # 在这里定义了函数 b_func，但是并没有没调用到
    def b_func():
        print("Hi, I'm b_func!")

    print("Hi, I'm a_func!")


def main():
    a_func()
    # 输出:
    # Hi, I'm a_func!


if __name__ == "__main__":
    main()
