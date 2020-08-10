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

# init
print("\nwrite")
with open("newfile.py", "w") as file:
  file.write("initial contents")
  file.close()

# read
print("\nread")
with open("newfile.py", "r") as file:
  print(file.read())
  file.close()
