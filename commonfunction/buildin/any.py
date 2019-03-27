#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# any(iterable)
#   Return True if any element of the iterable is true. If the iterable is empty, return False.


def main():
    a_list = []
    print(any(a_list)) # False

    b_list = [True, True]
    print(any(b_list)) # True

    c_list = [True, True, False]
    print(any(c_list)) # True

    d_list = ['a', 'b', 'c', '']
    print(any(d_list)) # True

    e_list = ['a', 'b', 'c']
    print(any(e_list)) # True

    f_list = ['']
    print(any(f_list)) # False


if __name__ == "__main__":
    main()