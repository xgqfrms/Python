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
   * @link https://www.youtube.com/watch?v=lyura1g0QgY
   *
  */
"""

from gpiozero import LED
from time import sleep

red = LED(12)
# Change 12 to your GPIO pin

red.on()
sleep(3)
red.off()
