#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re


def test1():
    """
    匹配一个被单引号或者是双引号括起来的字符串。
    """
    pattern = re.compile(r'(?P<quote>[\'\"]).*?(?P=quote)')
    match = pattern.match('"huangjian"')
    if match is not None:
        print(match.group())


def test2():
    print('\ntest2')

    pattern = re.compile(r'(?P<quote>---)(.*)(?P=quote)',
                         flags=re.DOTALL)
    strs = r"""
    
---
layout: post
title: "[字符串] 全排列"
date: 2016-04-07
author: mdgsf
comments: true
categories: Art
tags: [C,String,Permutation]
description:
published: true #default true
---
    
    """

    result = pattern.findall(strs)
    print(result)


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
