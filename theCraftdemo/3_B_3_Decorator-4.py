#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 在函数内部定义函数

def a_func():

    # 在这里定义了函数 b_func
    def b_func():
        print("Hi, I'm b_func!")

    print("Hi, I'm a_func!")
    return b_func # 返回了 b_func 这个函数，并未调用


def main():
    result = a_func()
    print('result =', result)
    
    # 输出:
    # Hi, I'm a_func!
    # result = <function a_func.<locals>.b_func at 0x7f61f8ad6c80>


if __name__ == "__main__":
    main()
