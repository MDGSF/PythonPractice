#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import random


def test1():
    # 生成一个列表

    a_list = []
    r = a_list.append(1)
    a_list.append(2)
    print('r =', r)
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
    # len, max, min

    n = 3

    a_list = [random.randrange(65, 91) for i in range(n)]
    b_list = [chr(random.randrange(65, 91)) for i in range(n)]
    print(a_list)
    print(b_list)

    c_list = a_list + b_list + a_list * 2
    print(c_list)

    a_list *= 3
    print(a_list)

    print(len(c_list))
    print(max(b_list))
    print(min(b_list))

    print('X' not in b_list)


def test6():
    # sort

    n = 10

    a_list = [random.randrange(1, 100) for i in range(n)]
    print(f'a_list comprehends {len(a_list)} random numbers:\n', a_list)

    a_list.sort()
    print('the list sorted:\n', a_list)

    a_list.sort(reverse=True)
    print('the list sorted reversely:\n', a_list)


def test7():
    # sort

    n = 10

    a_list = [chr(random.randrange(65, 91)) for i in range(n)]
    print(f'a_list comprehends {len(a_list)} random string elements:\n',
          a_list)

    a_list.sort()
    print('the list sorted:\n', a_list)

    a_list.sort(reverse=True)
    print('the list sorted reversely:\n', a_list)

    print()

    b_list = [chr(random.randrange(65, 91)) + chr(random.randrange(97, 123))
              for i in range(n)]
    print(f'b_list comprehends {len(b_list)} random string elements:\n',
          b_list)

    b_list.sort()
    print('the sorted:\n', b_list)

    # key 参数，默认是 None
    # key=str.lower 的意思是，在比较的时候，先全都转换成小写再比较……
    # —— 但并不改变原有值
    b_list.sort(key=str.lower, reverse=True)
    print('the sorted reversely:\n', b_list)


def test8():
    # list 中存在不同类型的数据时，不能使用 sort
    # TypeError: '<' not supported between instances of 'str' and 'int'

    a_list = [1, 'a', 'c']
    a_list.sort()


def test9():
    n = 3
    a_list = [random.randrange(65, 91) for i in range(n)]
    b_list = [chr(random.randrange(65, 91)) for i in range(n)]
    print(a_list)
    print(b_list)

    c_list = a_list + b_list + a_list * 2
    print(c_list)

    # 在末尾添加一个元素
    c_list.append('100')
    print(c_list)

    # 清空 list
    print()
    print(a_list)
    a_list.clear()
    print(a_list)

    # 拷贝列表，深拷贝，会重新分配内存
    print()
    d_list = c_list.copy()
    print(d_list)
    del d_list[6:8]
    print(d_list)
    print(c_list)

    # = 赋值，共用内存
    print()
    e_list = d_list
    del e_list[6:8]
    print(e_list)
    print(d_list)

    # extend 把 c_list 添加到 a_list 末尾
    print()
    print(a_list)
    a_list.extend(c_list)
    print(a_list)

    # insert 在指定位置插入
    print()
    print(a_list)
    a_list.insert(1, 'example')
    a_list.insert(3, 'example')
    print(a_list)

    # reverse 把 list 反过来
    print()
    print(a_list)
    a_list.reverse()
    print(a_list)


def test10():
    # del, a.pop[i], a.remove(x)

    n = 3

    a_list = [random.randrange(65, 91) for i in range(n)]
    print(a_list)

    print()
    a_list.insert(1, 'example')
    a_list.append('example')

    # remove 删除第一个出现的元素
    print()
    print(a_list)
    a_list.remove('example')
    print(a_list)

    # pop
    print()
    print(a_list)
    p = a_list.pop(2)
    print(a_list)
    print(p)

    # del
    print()
    a_list.insert(2, 'example1')
    a_list.insert(2, 'example2')
    print(a_list)
    del a_list[2]
    print(a_list)


def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    # test8()
    test9()
    test10()


if __name__ == "__main__":
    main()
