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
   * @created 2020-08-01
   *
   * @description
   * @augments
   * @example
   * @link
   *
  */
"""

print("write mode & close")

# append
# file = open("newfile.py", "w+a")
# file = open("newfile.py", "wa")
# ValueError: must have exactly one of create/read/write/append mode
# file = open("newfile.py", "ab+")
# TypeError: a bytes-like object is required, not 'str'
file = open("newfile.py", "a")
appended_length = file.write("appended text")
print("appended_length =", appended_length)
# appended_length = 13
file.close()

with open("newfile.py", "a") as file:
  appended_length = file.write("\nappended text, again")
  print("appended_length =", appended_length)
  # appended_length = 21
  file.close()
