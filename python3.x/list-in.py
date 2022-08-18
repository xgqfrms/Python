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



commands = ["Lights Off", "Lock the door", "Open the door", "Make Coffee", "Shut down"]
#your code goes here

voice = input()

if(voice in commands):
  print("OK")
else:
  print("Not supported")
