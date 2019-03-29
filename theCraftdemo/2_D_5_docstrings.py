#!/usr/bin/env python
# -*- coding: UTF-8 -*-

r"""
函数的文档注释，可以放在模块、类、函数的最开始
https://www.python.org/dev/peps/pep-0257/
http://www.sphinx-doc.org/en/master/

For consistency, always use \"\"\"triple double quotes\"\"\" around
docstrings.

Use r\"\"\"raw triple double quotes\"\"\" if you use any backslashes in your
docstrings.

For Unicode docstrings, use u\"\"\"Unicode triple-quoted strings\"\"\".
"""


def is_prime(n):
    """
    judege n is prime or not.

    :param n: a number
    :return: a boolean
    """
    if n < 2:
        return False
    if n == 2:
        return True
    for m in range(2, int(n ** 0.5) + 1):
        if (n % m) == 0:
            return False
    else:
        return True


def test1():
    help(is_prime)
    print(is_prime.__doc__)


def main():
    test1()


if __name__ == "__main__":
    main()
