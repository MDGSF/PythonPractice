#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys

# 添加模块的搜索路径
sys.path.append("/home/huangjian/git/huangjian/PythonPractice/theCraftdemo"
                "/2_D_6_modules")

import mycode


def test():
    print(sys.path)
    print(sys.builtin_module_names)


def test1():
    #help(mycode.is_prime)
    #help(mycode.say_hi)
    print(mycode.__name__)
    print(mycode.is_prime(3))
    mycode.say_hi('mike', 'zoe')
    print(dir(mycode))


def main():
    test()
    test1()


if __name__ == "__main__":
    main()
