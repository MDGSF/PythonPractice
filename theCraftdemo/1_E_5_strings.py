#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def test1():
    # 字符转化为对应的码值
    print(ord('a'))
    print(chr(97))


def test2():
    # 字符串的4种表示方法
    s1 = 'Simple is better than complex.'
    print(s1)

    s2 = "Simple is better than complex."
    print(s2)

    s3 = '''Simple is better than complex.
Complex is better than complicated.'''
    print(s3)

    s4 = """
Simple is better than complex.
Complex is better than complicated.
"""
    print(s4)


def test3():
    # 类型转换
    print(int('3'))
    print(float('3'))
    print(str(3.1415926))


def test4():
    # 这三个是等价的
    print('He said, it\'s fine.')
    print("He said, it\'s fine.")
    print("He said, it's fine.")


def test5():
    # 这两个是等价的
    print('Hey!' + ' ' + 'You!')
    print('Hey!'  ' '  'You!')

    # output: lalala
    print("la" * 3)

    # output: True
    print('o' in 'Hey! You!')


def test6():
    # 字符串遍历
    s = 'Python'
    for i in range(len(s)):
        print(i, s[i])

    for c in s:
        print(c)

    i = 0
    while i < len(s):
        print(i, s[i])
        i += 1


def test7():
    # 切片
    s = 'Python'
    print(s)
    print(s[1])
    print(s[2:])
    print(s[2:5])
    print(s[:5])
    print(s[1:5:2])  # [start:stop:step]


def test8():
    print('Python'.upper())
    print('Python'.lower())
    print('Python'.swapcase())
    print('Python'.casefold())
    print('this is a great day.'.capitalize())
    print('this is a great day.'.title())
    print('this is a great day.'.title().swapcase())


def test9():
    # 字符串查找

    s = """Simple is better than complex.
    Complex is better than complicated."""

    # output: True
    print("mpl" in s)

    # 计算出现的次数
    print(s.lower().count('mp'))
    print(s.lower().count('mp', 10))
    print(s.lower().count('mp', 10, 30))

    # 找到最早出现的下标，找不到返回 -1
    print(s.lower().find('mp'))
    print(s.lower().find('mp', 10))
    print(s.lower().find('mp', 10, 30))

    # 和 find 一样，不过是从后往前找
    print(s.lower().rfind('mp'))
    print(s.lower().rfind('mp', 10))
    print(s.lower().rfind('mp', 10, 30))

    # 作用与 find() 相同，但，如果没找到的话，会触发 ValueError 异常
    s.lower().index('mp')

    # 作用与 rfind() 相同，但，如果没找到的话，会触发 ValueError 异常
    s.lower().rindex('mp')


def test10():
    # 判断前缀，后缀

    s = """Simple is better than complex.
        Complex is better than complicated."""

    print("s.lower().startswith('S'):", s.lower().startswith('S'))
    print("s.lower().startswith('b'):", s.lower().startswith('b', 10))
    print("s.lower().startswith('e'):", s.lower().startswith('e', 11, 20))

    print("s.lower().endswith('.'):", s.lower().endswith('.'))
    print("s.lower().endswith('.'):", s.lower().endswith('.', 10))
    print("s.lower().endswith('.'):", s.lower().endswith('.', 10, 20))


def test11():
    # 字符串替换

    s = """Simple is better than complex.
Complex is better than complicated."""

    # str.replace(old, new[, count])
    # count 是可选参数，替换的次数
    # 返回替换之后的字符串
    print(s.lower().replace('mp', '[ ]', 2))

    # 把 \t 替换为空格
    s = "Special\tcases\taren't\tspecial\tenough\tto\tbreak\tthe\trules."
    print(s.expandtabs())
    print(s.expandtabs(2))


def test12():
    s = "\r \t Simple is better than complex.    \t \n"
    print(s)
    print(s.strip())
    print(s.lstrip())
    print(s.rstrip())


def test13():
    # 切割字符串

    s = """Name,Age,Location
John,18,New York
Mike,22,San Francisco
Janny,25,Miami
Sunny,21,Shanghai"""

    print(s)
    print(s.splitlines())  # 按行切割，返回一个 list
    print(s.split())  # 默认按各种空白字符切割

    # 这两个是等价的，都是按逗号切割
    print(s.split(","))
    print(s.split(sep=','))

    print(s.split(sep=',', maxsplit=1))  # 切割一次
    print(s.split(sep=',', maxsplit=0))  # 不切割
    print(s.split(sep=',', maxsplit=-1))  # 全部切割


def test14():
    # 拼接字符串

    s = ''
    t = ['P', 'y', 't', 'h', 'o', 'n']
    print(s.join(t))


def test15():
    # 字符串排版

    s = 'Sparse is better than dense!'

    # 居中对齐
    print(s.title().center(60))
    print(s.center(60, '='))
    print(s.center(10))  # 如果宽度参数小于字符串长度，则返回原字符串

    # 靠右对齐
    print(s.rjust(60))
    print(s.rjust(60, '.'))

    # 靠左对齐
    print(s.ljust(60, '.'))

    # zfill 用来在左侧填充 0
    for i in range(1, 11):
        filename = str(i).zfill(3) + '.mp3'
        print(filename)


def test16():
    # 格式化字符串

    name = 'John'
    age = 25

    # format
    print('{} is {} years old.'.format(name, age))
    print('{0} is {1} years old.'.format(name, age))
    print('{1} is {0} years old.'.format(name, age))
    print('{} is grown up? {}'.format(name, age > 18))

    # f-string
    print(f'{name} is {age} years old.')
    print(f'{name} is grown up? {age > 18}')


def test17():
    # 字符串属性

    # str.isalnum()
    print("'1234567890'.isalnum():",
          '1234567890'.isalnum())  # '3.14'.isalnum() 返回的是 False

    # str.isalpha()
    print("'abcdefghij'.isalpha():", \
          'abcdefghij'.isalpha())

    # str.isascii()
    print("'山巅一寺一壶酒'.isascii():", \
          '山巅一寺一壶酒'.isascii())

    # str.isdecimal()
    print("'0.123456789'.isdecimal():", \
          '0.1234567890'.isdecimal())

    # str.isdigit()
    print("'0.123456789'.isdigit():", \
          '0.1234567890'.isdigit())  # 注意，如果字符串是 identifier，返回值也是 False

    # str.isnumeric()
    print("'0.123456789'.isnumeric():", \
          '0.1234567890'.isnumeric())

    # str.islower()
    print("'Continue'.islower():", \
          'Continue'.islower())

    # str.isupper()
    print("'Simple Is Better Than Complex'.isupper():", \
          'Simple Is Better Than Complex'.isupper())

    # str.istitle()
    print("'Simple Is Better Than Complex'.istitle():", \
          'Simple Is Better Than Complex'.istitle())

    # str.isprintable()
    print("'\t'.isprintable():", \
          '\t'.isprintable())

    # str.isspace()
    print("'\t'.isspace():", \
          '\t'.isspace())

    # str.isidentifier()
    print("'for'.isidentifier():", \
          'for'.isidentifier())


def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    test10()
    test11()
    test12()
    test13()
    test14()
    test15()
    test16()
    test17()


if __name__ == "__main__":
    main()
