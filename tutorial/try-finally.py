#!/usr/bin/env python3

# coding: utf8

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
   * @created 2020-08-0
   *
   * @description
   * @augments
   * @example
   * @link
   *
  */
"""

"""
file = open("filename.txt")
try:
  # FileNotFoundError: [Errno 2] No such file or directory: 'filename.txt'
  print(file.read())
# except:
#   print("finally close", FileReadError)
finally:
  print("finally close")
  file.close()
  # NameError: name 'file' is not defined

 """
try:
  f = open("filename.txt")
  print(f.read())
  print(1 / 0)
finally:
  f.close()


# https://www.runoob.com/python/python-tutorial.html
