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

print("Starting")

# init
file = open("newfile.py", "w")
file.write("initial contents")
file.close()

# read
print("\nread")
file = open("newfile.py", "r")
print(file.read())
file.close()

# write
print("\nwrite")
file = open("newfile.py", "w")
file.write("Some new text")
file.close()

# read again
print("\nReading new contents")
file = open("newfile.py", "r")
print(file.read())
file.close()

print("\nFinished")
