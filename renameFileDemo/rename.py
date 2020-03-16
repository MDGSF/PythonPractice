#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys


def main():
  imageDirectory = '/home/huangjian/test/annoTest/huangjian_test_autoanno/images'
  files = os.listdir(imageDirectory)
  files.sort()
  count = 1
  for oneFile in files:
    fileParts = oneFile.split(".")
    filePreParts = fileParts[0].split("_")
    filePreParts[-1] = str(count)
    count += 1
    newFileName = '_'.join(filePreParts) + "." + fileParts[1]
    print(newFileName)

    oldFilePathName = os.path.join(imageDirectory, oneFile)
    newFilePathName = os.path.join(imageDirectory, newFileName)
    os.rename(oldFilePathName, newFilePathName)


if __name__ == "__main__":
    main()

