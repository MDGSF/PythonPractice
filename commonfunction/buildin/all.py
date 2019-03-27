#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# all(iterable)
# Return True if all elements of the iterable are true (or if the iterable is empty).

def main():
    a_list = []
    print(all(a_list)) # True

    b_list = [True, True]
    print(all(b_list)) # True

    c_list = [True, True, False]
    print(all(c_list)) # False

    d_list = ['a', 'b', 'c', '']
    print(all(d_list)) # False

    e_list = ['a', 'b', 'c']
    print(all(e_list)) # True


if __name__ == "__main__":
    main()