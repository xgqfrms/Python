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


#your code goes here


x = 4
sum = 100
while x > 0:
  action = input();
  if(action == "hit"):
    sum += 10;
  if(action == "miss"):
    sum -= 20;
  x -= 1

print(sum)


"""
#your code goes here

# a,b,c,d = (input()).split();
# ValueError: not enough values to unpack (expected 4, got 1)
# ValueError：没有足够的值来解包（预期 4，得到 1）
a = input();
b = input();
c = input();
d = input();

sum = 100

if(a == "hit"):
  sum += 10;
if(a == "miss"):
  sum -= 20;

if(b == "hit"):
  sum += 10;
else:
  sum -= 20;

if(c == "hit"):
  sum += 10;
else:
  sum -= 20;

if(d == "hit"):
  sum += 10;
else:
  sum -= 20;


print(sum)

"""
