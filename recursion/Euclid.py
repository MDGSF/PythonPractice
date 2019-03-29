#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 最大公约数
# greatest common divisor

# example: p = 1440, q = 408
# 1440 % 408 = 216
# 408  % 216 = 192
# 216  % 192 = 24
# 192  % 24  = 0
#         1440  408  216  192  24  0
# 第一轮   p     q
# 第二轮         p    q
# 第三轮              p    q
# 第四轮                   p    q
# 第五轮                        p  q

def gcd(p, q):
    if q == 0:
        return p
    else:
        return gcd(q, p % q)


def gcd2(p, q):
    while q != 0:
        p, q = q, p % q
    return p


def main():
    print(gcd(1440, 408))
    print(gcd2(1440, 408))


if __name__ == "__main__":
    main()
