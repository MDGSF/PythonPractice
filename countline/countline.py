#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
统计

指定目录下
指定文件后缀
排除目录
排除文件后缀

所有文件总行数
所有文件空白行数
所有文件非空白行数

单个文件总行数
单个文件空白行数
单个文件非空白行数
"""

import os
import click


def is_str_empty(str):
    return len(str) == 0 or len(str.strip()) == 0


def paramtersParse(directory, suffix, exdir, exsuffix):
    directoryList = [os.getcwd()] if is_str_empty(directory) \
        else directory.split(',')
    suffixList = ['py'] if is_str_empty(suffix) else suffix.split(',')
    exdirList = [] if is_str_empty(exdir) else exdir.split(',')
    exsuffixList = [] if is_str_empty(exsuffix) else exsuffix.split(sep=',')
    return set(directoryList), set(suffixList), set(exdirList), \
           set(exsuffixList)


def isValidDir(directory, exdirs):
    if directory in exdirs:
        return False
    return True


def isValidFile(filename, suffixs, exsuffixs):
    fileExt = os.path.splitext(filename)[1]
    if fileExt in suffixs:
        return True
    if fileExt in exsuffixs:
        return False
    return False


def countOneFile(filename):
    """
    count one file
    all lines.
    all blank lines.
    all non blank lines.
    """
    curFileAllLines = 0
    curFileAllBlankLines = 0
    curFileAllNonBlankLines = 0

    f = open(filename, 'r')

    for line in f.readlines():
        curFileAllLines += 1

        if is_str_empty(line):
            curFileAllBlankLines += 1
        else:
            curFileAllNonBlankLines += 1

    f.close()

    return curFileAllLines, curFileAllBlankLines, curFileAllNonBlankLines


def countOneDirectory(directory, suffixs, exdirs, exsuffixs, filesLine):
    """
    count one directory.
    """
    curLines = 0
    curBlankLines = 0
    curNonBlankLines = 0

    files = os.listdir(directory)
    for f in files:
        if f[0] == '.':  # 隐藏文件
            continue

        fWithPath = os.path.join(directory, f)
        if os.path.isdir(fWithPath):
            if isValidDir(fWithPath, exdirs):
                subLines, subBlankLines, subNonBlankLines = \
                    countOneDirectory(fWithPath, suffixs, exdirs, exsuffixs,
                                      filesLine)
                curLines += subLines
                curBlankLines += subBlankLines
                curNonBlankLines += subNonBlankLines
        else:  # 文件
            if isValidFile(f, suffixs, exsuffixs):
                curFileAllLines, curFileAllBlankLines, \
                curFileAllNonBlankLines = \
                    countOneFile(fWithPath)
                curLines += curFileAllLines
                curBlankLines += curFileAllBlankLines
                curNonBlankLines += curFileAllNonBlankLines
                filesLine[fWithPath] = {
                    "FileAllLines": curFileAllLines,
                    "FileAllBlankLines": curFileAllBlankLines,
                    "FileAllNonBlankLines": curFileAllNonBlankLines
                }

    return curLines, curBlankLines, curNonBlankLines


def Count(directorys, suffixs, exdirs, exsuffixs, verbose):
    """
    count all directorys.
    """
    allLine = 0
    allBlankLine = 0
    allNonBlankLine = 0
    filesLine = {}

    for directory in directorys:
        curLines, curBlankLines, curNonBlankLines = \
            countOneDirectory(directory, suffixs, exdirs, exsuffixs, filesLine)
        allLine += curLines
        allBlankLine += curBlankLines
        allNonBlankLine += curNonBlankLines

    print('allLine =', allLine)
    print('allBlankLine =', allBlankLine)
    print('allNonBlankLine =', allNonBlankLine)
    if verbose:
        for filename, value in filesLine.items():
            print(filename, value)


@click.command()
@click.option('--directory', default='',
              help='Directory you want to search (split with ,).')
@click.option('--suffix', default='.py',
              help='File with suffix you want to search '
                   '(Default py) (split with ,).')
@click.option('--exdir', default='',
              help='Exclude directory (split with ,).')
@click.option('--exsuffix', default='',
              help='Exclude suffix (split with ,).')
@click.option('--verbose', is_flag=True, default=False,
              help='Show verbose information.')
def main(directory, suffix, exdir, exsuffix, verbose):
    """
    Simple program that count python code lines.
    """

    directoryList, suffixList, exdirList, exsuffixList = paramtersParse(
        directory, suffix, exdir, exsuffix
    )

    Count(directoryList, suffixList, exdirList, exsuffixList, verbose)


if __name__ == "__main__":
    main()
