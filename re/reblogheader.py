#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re


def test():
    print('\ntest2')

    pattern = re.compile(
        r'(?P<quote>---)(?P<line>([^:\n]*):([^:\n]*)\n)*(?P=quote)',
        re.DEBUG | re.DOTALL)
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
    test()


if __name__ == "__main__":
    main()
