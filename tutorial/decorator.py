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
   * @created 2020-08-12
   *
   * @description decorate
   * @augments
   * @example
   * @link https://www.sololearn.com/Play/Python/
   *
  */
"""

# 装饰器/修饰器 高阶函数
# 高阶函数，返回新的函数
# Decorators provide a way to modify functions using other functions.
# def decor(func):
#   def wrap():
#     print("======before calling function======")
#     func()
#     print("======after called function======")
#   return wrap

# 支持参数 🚀
def decor(func, args):
  def wrap(args):
    print("======before calling function======")
    func(args)
    print("======after called function======")
  return wrap

# 方法 一, 使用高级函数包裹
# 1.1 使用 def 声明函数
def greeting(name):
  print("Hello world!", name)

# 1.2 使用 修饰器高阶函数，返回新的函数
decorated = decor(greeting, '')
# 两个参数，实参, 形参

# 1.3 执行修饰后的函数
decorated('webgeeker')
# 一个参数, 实参

# 方法 二, 使用 @decorator symbol
# 2.1 使用 @修饰符号

# TypeError: decor() missing 1 required positional argument: 'args'
@decor('')
def greeting(name):
  print('@修饰符号')
  print('Hello world!', name)

# 2.2 执行修饰后的函数
greeting('xgqfrms')





"""
# test

$ python3 decorator.py
$ python3 decorate.py

"""
