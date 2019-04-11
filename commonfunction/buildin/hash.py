#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
hash(object)
Return the hash value of the object (if it has one). Hash values are integers.
They are used to quickly compare dictionary keys during a dictionary lookup.
Numeric values that compare equal have the same hash value (even if they are
of different types, as is the case for 1 and 1.0).
"""


def test1():
    print(hash(1))
    print(hash(1.0))
    print(hash("1"))


def main():
    test1()


if __name__ == "__main__":
    main()
