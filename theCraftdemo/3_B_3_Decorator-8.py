#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper


def strong(func):
    def wrapper():
        original_result = func()
        modified_result = '<strong>' + original_result + '</strong>'
        return modified_result

    return wrapper


@strong
@uppercase
def ann_output():
    return 'The quick brown fox jumps over the lazy dog.'


def main():
    print(ann_output())

    # 输出：
    # <strong>THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.</strong>

    # 如果修改为：
    # @uppercase
    # @strong
    # def ann_output():
    # 那么输出：
    # <STRONG>THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.</STRONG>

    # 也就是说，多个 decorator 的执行顺序是从下往上的。


if __name__ == "__main__":
    main()
