#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys

sys.path.append(os.path.abspath("../moduleA_dir"))
import moduleA

sys.path.append(os.path.abspath("../moduleB_dir"))
import moduleB


def main():
    moduleA.showmodulename()
    moduleB.showmodulename()


if __name__ == "__main__":
    main()
