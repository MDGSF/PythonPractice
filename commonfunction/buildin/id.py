#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# id(object)
# Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.
#
# CPython implementation detail: This is the address of the object in memory.


def main():
    i = 0
    print(id(i))


if __name__ == "__main__":
    main()
