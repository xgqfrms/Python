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

import test

class Main():
  # 构造函数 初始化
  def __init__(self):
    # test.pyc
    self.test = test.Test()
  def log(name):
    self.test.sum(1, 2)
    print 'python2 print function' + name


# main 程序的入口
if __name__ == '__main__':
  # 实例化
  app = Main()
  app.log('app')
