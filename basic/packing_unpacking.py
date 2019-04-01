#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def test1():
    def fun(a, b, c, d):
        print(a, b, c, d)

    my_list = [1, 2, 3, 4]

    # unpacking list into four argument
    fun(*my_list)

    # fun(my_list) # 这个无法工作

    # unpacking a tuple
    fun(*(10, 11, 12, 13))


def test2():
    print('\ntest2')

    args = [3, 6]
    print(range(*args))


# 把传进来的多个参数打包成一个 args 变量，这个变量是 tuple 类型。
def mySum(*args):
    print('mysum, type(args) =', type(args))  # 这个类型是 tuple
    sum = 0
    for i in range(0, len(args)):
        sum = sum + args[i]
    return sum


def test3():
    print('\ntest3')

    print(mySum(1, 2, 3, 4, 5))


def test4():
    print('\ntest4')

    def fun1(a, b, c):
        print(a, b, c)

    def fun2(*args):
        # 把 tuple 类型转换为 list 类型，才能进行修改
        # 如果不修改的话，则无需进行转换
        args = list(args)
        args[0] = 'Geekforgeeks'
        args[1] = 'awesome'
        fun1(*args)

    fun2('Hello', 'beautiful', 'world')


def test5():
    print('\ntest5')

    def fun(a, b, c):
        print(a, b, c)

    d = {'a': 2, 'b': 4, 'c': 10}
    print('d =', d)
    print('*d =', *d)
    # print(**d) # 这个会出错
    fun(**d)


def test6():
    print('\ntest6')

    def test(*args):
        print('test args =', args)

    def test2(**kwargs):
        print('test2 kwargs=', kwargs)

    def fun(**kwargs):
        print('type(kwargs) =', type(kwargs))  # 这个是 dict 类型
        print('kwargs =', kwargs)
        print('*kwargs =', *kwargs) # 一个 * 解包出来就是 key 的字符串
        test(*kwargs)
        test2(**kwargs) # 两个 ** 解包出来，就是一个个 key=value 的键值对
        for key in kwargs:
            print(key, kwargs[key])

    fun(name='geeks', ID='110', language='Python')


def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()


if __name__ == "__main__":
    main()
