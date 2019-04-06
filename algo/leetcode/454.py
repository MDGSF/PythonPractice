#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from typing import List


class Solution:
    @staticmethod
    def fourSumCount(A: List[int], B: List[int], C: List[int],
                     D: List[int]) -> int:
        res = 0
        m = {}
        for a in A:
            for b in B:
                if a + b in m:
                    m[a + b] += 1
                else:
                    m[a + b] = 1
        for c in C:
            for d in D:
                if -(c+d) in m:
                    res += m[-(c + d)]
        return res


def main():
    print(Solution.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))


if __name__ == "__main__":
    main()
