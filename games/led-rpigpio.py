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
   * @link https://www.youtube.com/watch?v=KNsqlqBrkuY
   *
  */
"""

import RPI.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)

while True:
  gpio.output(17, gpio.HIGH)
  time.sleep(1)
  gpio.output(17, gpio.LOW)
  time.sleep(1)

"""

from RPI.GPIO import setmode, setup, output, BCM, OUT, HIGH, LOW
from time import sleep

setmode(BCM)
setup(17, OUT)

while True:
  output(17, HIGH)
  sleep(1)
  output(17, LOW)
  sleep(1)

"""
