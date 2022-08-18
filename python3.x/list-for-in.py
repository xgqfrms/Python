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


cart = [15, 42, 120, 9, 5, 380]

discount = int(input())
total = 0

for item in cart:
  total += item - (item * discount)/100

print(total)

# (100 * 10) / 100 => 10
# Input 10

"""


cart = [15, 42, 120, 9, 5, 380]

discount = int(input())
total = 0

for item in cart:
  total += item
#   total += item * (1 - discount)

price = total - (total * discount) / 100
print(price)


"""
