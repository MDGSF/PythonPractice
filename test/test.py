#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def main():
    l = [0,1,2,3,4,5]
    print(l)

    l[1:6:2] = [100, 200, 300]
    print(l)

if __name__ == "__main__":
    main()
