#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
https://leetcode-cn.com/explore/interview/card/tencent/221/array-and-strings/898/
"""


def longestCommonPrefix(strs) -> str:
    result = ""
    curIdx = 0
    strNumber = len(strs)
    if strNumber == 0:
        return ""
    if strNumber == 1:
        return strs[0]
    while True:
        i = 0
        while i < strNumber - 1:
            if len(strs[i]) <= curIdx or len(strs[i + 1]) <= curIdx:
                return result
            if strs[i][curIdx] != strs[i + 1][curIdx]:
                return result
            i += 1
        else:
            result += strs[0][curIdx]
            curIdx += 1
    return result


def test1():
    print(longestCommonPrefix(["flower", "flow", "flight"]))
    print(longestCommonPrefix(["dog","racecar","car"]))
    print(longestCommonPrefix([]))
    print(longestCommonPrefix([""]))


def main():
    test1()


if __name__ == "__main__":
    main()
