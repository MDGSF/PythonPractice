#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 在函数内部定义函数

def a_func():

    # 在这里定义了函数 b_func
    def b_func():
        print("Hi, I'm b_func!")

    print("Hi, I'm a_func!")
    return b_func() # 在这里才调用了 b_func()，并且把 b_func() 的执行结果返回


def main():
    result = a_func()
    print('result =', result)

    # 输出:
    # Hi, I'm a_func!
    # Hi, I'm b_func!
    # result = None


if __name__ == "__main__":
    main()
