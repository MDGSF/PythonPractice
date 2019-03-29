#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import keyword


def main():
    # 所有的关键字
    print(keyword.kwlist)

    # 判断 if 是不是关键字
    print(keyword.iskeyword('if'))


if __name__ == "__main__":
    main()
