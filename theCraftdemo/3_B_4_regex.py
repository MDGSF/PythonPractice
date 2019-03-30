#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
https://docs.python.org/3/library/re.html
https://regex101.com/
https://regexper.com/
"""

import re


def test1():
    strs = 'The quick brown fox jumps over the lazy dog'
    pattn = re.compile(r'\wo\w')
    result = re.findall(pattn, strs)
    print(result)


def test2():
    """
    本义字符: a-z, A-Z, 0-9, _
    特殊字符: \ + * . ? - ^ $ | ( ) [ ] { } < >
    如果要搜索特殊字符的话，都要加上转义字符 \
    """
    pass


def test3():
    """
    集合原子: []
    [abc] 表示 a or b or c，即 abc 中任意一个字符
    beg[iau]n 能够代表 begin, began, begun

    [a-z] 表示从小写字母 a 到小写字母 z 中的任意一个字符。
    [^abc] 表示 abc 以外的其他任意字符。
    """
    print('\ntest3')
    strs = 'begin began begun bigins begining'
    pttn = r'beg[iau]n'
    result = re.findall(pttn, strs)
    print(result)


def test4():
    """
    类别原子
    \d 表示任意数字，等价于 [0-9]
    \D 表示任意非数字，等价于 [^0-9]
    \w 表示任意本义字符，等价于 [a-zA-Z0-9_]
    \W 表示任意非本义字符，等价于 [^a-zA-Z0-9_]
    \s 表示任意空白字符，等价于 [ \f\n\r\t\v]
    \S 表示任意非空白字符，等价于 [^ \f\n\r\t\v]
    . 除 \r \n 之外的任意字符，等价于 [^\r\n]

    d 是 digits
    w 是 word characters
    s 是 spaces
    f 是 flip
    n 是 new line
    r 是 return
    t 是 tab
    v 是 vertical tab
    """
    print('\ntest4')
    strs = '<dl>(843) 542-4256</dl> <dl>(431) 270-9664</dl>'
    pttn = r'\d\d\d\-'
    result = re.findall(pttn, strs)
    print(result)


def test5():
    """
    边界原子
    ^ 匹配被搜索字符串的开始位置
    $ 匹配被搜索字符串的结束位置
    \b 匹配单词的边界。 er\b 能匹配 coder 中的 er，却不能匹配 error 中的 er
    \B 匹配非单词的边界。 er\B 能匹配 error 中的 er，却不能匹配 coder 中的 er
    """
    print('\ntest5')
    strs = 'never ever verb however everest'
    pttn = r'er\b'
    result = re.findall(pttn, strs)
    print(result)

    pttn = r'er\B'
    result = re.findall(pttn, strs)
    print(result)


def test6():
    """
    组合原子： () 能够将多个单字符原子组合成一个原子
    er 是两个原子： e 和紧随其后的 r
    [er] 是一个原子： 或者 e 或者 r
    (er) 是一个原子： er
    """
    pass


def test7():
    """
    数量操作符
    + 表示前面的原子必须至少出现一次，即 出现次数 >= 1
        例如： go+gle 可以匹配 google gooogle goooogle 等。
    ? 表示前面的原子最多只可以出现一次，即 0 <= 出现次数 <=
        例如： colou?red 可以匹配 colored coloured
    * 表示前面的原子可以不出现，也可以出现一次或者多次，即 出现次数 >= 0
        例如： 520* 可以匹配 52 520 5200 52000 5200000
    {n}    之前的原子出现确定的 n 次。
    {n,}   之前的原子出现至少 n 次。
    {n, m} 之前的原子出现至少 n 次，至多 m 次。
        例如： go{2, 5}gle 只能匹配 google gooogle goooogle gooooogle
    """
    print('\ntest7')
    strs = 'google gogle'
    pttn = r'go+gle'
    result = re.findall(pttn, strs)
    print(result)

    strs = 'error wonderer severeness'
    print(re.findall(r'er+', strs))
    print(re.findall(r'[er]+', strs))
    print(re.findall(r'(er)+', strs))


def test8():
    """
    或操作符 | 是所有操作符中优先级最低的
    """
    print('\ntest8')
    strs = 'begin began begun begins beginn'
    pttn = r'begin|began|begun'
    print(re.findall(pttn, strs))


def test9():
    """
    中括号中的 | 不被当做特殊字符处理
    中括号中的 () 不被当做特殊字符处理
    """
    print('\ntest9')

    strs = 'achroiocythaemia achroiocythemia a|e'
    pttn = r'[a|ae]'
    print(re.findall(pttn, strs))

    pttn = r'[a|e]'
    print(re.findall(pttn, strs))

    pttn = r'[ae]'
    print(re.findall(pttn, strs))

    pttn = r'[(ae)]'
    print(re.findall(pttn, strs))

    pttn = r'[a|ae|(ae)]'
    print(re.findall(pttn, strs))


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


if __name__ == "__main__":
    main()
