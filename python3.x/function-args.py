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
   * @created 2022-08-18
   *
   * @description
   * @augments
   * @example
   * @link
   *
  */
"""


def test(a, b, c):
  print(a, b, c)
  # print(args)
  # print(arguments)
  
# NameError: name 'args' is not defined
# NameError: name 'arguments' is not defined

test(1,2,3)
# 1 2 3

# test(1,2,3,4)
# TypeError: test() takes 3 positional arguments but 4 were given


# 不定长参数
def printArgs(arg1, *args ):
   # "打印任何传入的参数"
   print("arg1 =", arg1)
   for arg in args:
      print("arg =", arg)
   return
 
printArgs(1)
# arg1 = 1
print('\n')
printArgs(1,2,3)
# arg1 = 1
# arg = 2
# arg = 3



# https://www.runoob.com/python/python-functions.html
