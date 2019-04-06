#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from typing import List


class Solution:
    @staticmethod
    def fourSum(nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        res = set()
        for i, iv in enumerate(nums[:-3]):
            if i >= 1 and iv == nums[i - 1]:
                continue
            j = i + 1
            while j < len(nums) - 2:
                jv = nums[j]
                if j > i + 1 and jv == nums[j - 1]:
                    j += 1
                    continue
                start = j + 1
                end = len(nums) - 1
                while start < end:
                    if iv + jv + nums[start] + nums[end] == target:
                        res.add((iv, jv, nums[start], nums[end]))
                        start += 1
                        end -= 1
                    elif iv + jv + nums[start] + nums[end] > target:
                        end -= 1
                    else:
                        start += 1
                j += 1
        return list(map(list, res))


def main():
    #print(Solution.fourSum([0, 0, 0, 0], 0))
    #print(Solution.fourSum([1, 0, -1, 0, -2, 2], 0))
    print(Solution.fourSum([-1, 0, 1, 2, -1, -4], -1))


if __name__ == "__main__":
    main()
