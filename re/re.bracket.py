#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re


def test1():
    pattern = re.compile(r'(\(\)|\[\]|\{\})+')
    match = pattern.match("[](){}")
    if match is not None:
        print(match.group())


def main():
    test1()


if __name__ == "__main__":
    main()
