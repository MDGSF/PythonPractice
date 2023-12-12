#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from moduleA_dir import moduleA
from moduleA_dir.sub01 import sub01


def main():
  moduleA.showmodulename()
  sub01.showmodulename()


if __name__ == "__main__":
  main()
