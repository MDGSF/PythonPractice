#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
https://leetcode-cn.com/explore/interview/card/tencent/221/array-and-strings/899/
https://leetcode-cn.com/problems/3sum/
"""

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
        return []
    nums.sort()
    res = set()
    for i, v in enumerate(nums[:-2]):
        if i >= 1 and v == nums[i - 1]:
            continue
        d = {}
        for x in nums[i + 1:]:
            if x not in d:
                d[-v - x] = 1
            else:
                res.add((v, -v - x, x))
    return list(map(list, res))


def test1():
    print(threeSum([-1, 0, 1, 2, -1, -4]))


def main():
    test1()


if __name__ == "__main__":
    main()
