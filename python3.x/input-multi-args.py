#!/usr/bin/env python3

# coding=utf-8

__author__ = 'xgqfrms'
__editor__ = 'vscode'
__version__ = '1.0.1'
__copyright__ = """
  Copyright (c) 2012-2050, xgqfrms; mailto:xgqfrms@xgqfrms.xyz
"""

"""
  /**
   *
   * @author xgqfrms
   * @license MIT
   * @copyright xgqfrms
   * @created 2022-08-17
   *
   * @description
   * @augments
   * @example
   * @link
   *
  */
"""


# Python3 如何处理 input 同时接收多个参数

# name = input("input your name: ")
# print(f"your name is {name}")

# input() & multi args
# 多个参数之间通过空格分隔：xgqfrms 23
# name,age = (input("name and age: ")).split()

# 多个参数之间通过逗号分隔：xgqfrms,23
name,age = (input("name and age: ")).split(",")

# name = input("name: ")
# age = input("age: ")

print(f"your name is {name}, age is {age}")
# your name is xgqfrms, age is 23
