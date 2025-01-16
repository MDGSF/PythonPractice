#!/usr/bin/env bash

export PYTHONPATH=$PYTHONPATH:$PWD

pytype demo01.py

# 递归地检查项目目录下的所有 Python 文件
# pytype .

# 生成类型注解文件 .pyi
# pytype -o output_dir your_script.py
