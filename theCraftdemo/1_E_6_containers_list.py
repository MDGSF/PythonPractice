#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import random


def test1():
    # 生成一个列表

    a_list = []
    a_list.append(1)
    a_list.append(2)
    print(a_list, f'has a length of {len(a_list)}.')

    b_list = [1, 2, 3]
    print(b_list, f'has a length of {len(b_list)}.')

    c_list = list(range(1, 9))
    c_list.append(11)
    print(c_list, f'has a length of {len(c_list)}.')

    d_list = [2 ** x for x in range(8)]
    print(d_list, f'has a length of {len(d_list)}.')


def test2():
    # list Comprehension

    n = 10

    # 生成一个 n 个元素的序列，每个元素是 1~100 之间的随机数
    a_list = [random.randrange(1, 100) for i in range(n)]
    print(f'a_list comprehends {len(a_list)} random numbers: {a_list}')

    # 从 a_list 里把偶数都挑出来
    b_list = [x for x in a_list if x % 2 == 0]
    print(f'... and it has {len(b_list)} even numbers: {b_list}')


def test3():
    a_list = [1, 2, 3]
    b_list = [4, 5, 6]
    c_list = a_list + b_list * 3
    print(c_list)
    print(7 not in c_list)
    print(a_list > b_list)


def test4():
    n = 3

    a_list = [random.randrange(65, 91) for i in range(n)]
    b_list = [chr(random.randrange(65, 91)) for i in range(n)]
    print(a_list)
    print(b_list)

    c_list = a_list + b_list + a_list * 2
    print(c_list)

    # 切片
    print()
    print(c_list[3])
    print(c_list[:])
    print(c_list[5:])
    print(c_list[:3])
    print(c_list[2:6])

    # 删除列表中的元素
    print()
    del c_list[3]
    print(c_list)
    del c_list[5:8]
    print(c_list)

    # 根据索引替换
    # s[start:stop:step] = t，跟 range 的三个参数类似；
    # len(t) = len([start:stop:step]) 必须为真
    print()
    c_list[1:5:2] = ['a', 2]
    print(c_list)


def test5():
    n = 3

    a_list = [random.randrange(65, 91) for i in range(n)]
    b_list = [chr(random.randrange(65, 91)) for i in range(n)]


def main():
    test1()
    test2()
    test3()
    test4()
    test5()


if __name__ == "__main__":
    main()
