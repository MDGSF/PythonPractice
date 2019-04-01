#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def test1():
    """
    If you need to modify the sequence you are iterating over while inside the
    loop (for example to duplicate selected items),
    it is recommended that you first make a copy.
    Iterating over a sequence does not implicitly make a copy.
    The slice notation makes this especially convenient:
    """

    words = ['cat', 'window', 'defenestrate']
    for w in words[:]: # Loop over a slice copy of the entire list.
        if len(w) > 6:
            words.insert(0, w)
    print(words)

    # 如果写成 for w in words: 则循环无法退出


def main():
    test1()


if __name__ == "__main__":
    main()
