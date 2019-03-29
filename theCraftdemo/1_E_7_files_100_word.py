#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 所有英语单词列表 https://github.com/dwyl/english-words

# a = 1, b = 2, c = 3, ....
# 计算一个单词中每个字母的和为 100 的单词。


def sum_of_word(word):
    sum = 0
    for char in word:
        sum += ord(char) - 96
    return sum


def main():
    with open('results.txt', 'w') as result:
        with open('/home/huangjian/git/others/english-words/words_alpha.txt',
                  'r') as file:
            for word in file.readlines():
                if sum_of_word(word.strip()) == 100:
                    result.write(word)


if __name__ == "__main__":
    main()
