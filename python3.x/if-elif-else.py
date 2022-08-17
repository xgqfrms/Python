#!/usr/bin/env python3

# coding=utf-8

__author__ = 'xgqfrms'
__editor__ = 'vscode'
__version__ = '1.0.1'
__copyright__ = """
  Copyright (c) 2012-2050, xgqfrms; mailto:xgqfrms@xgqfrms.xyz
"""


score = 70

if score < 60:
   print("C")
elif score < 85:
   print("B")
else:
   print("A")




purity = float(input())
#your code goes here


if(purity >= 99.9):
    print("24K")
elif(purity >= 91.7 and purity < 99.9):
    print("22K")
elif(purity >= 83.3 and purity < 91.7):
    print("20K")
elif(purity >= 75.0 and purity < 83.3):
    print("18K")


'''
if(purity >= 99.9):
    print("24K")
elif(purity >= 91.7 and purity < 99.9):
    print("24K")
elif(purity >= 83.3 and purity < 91.7):
    print("20K")
elif(purity >= 75 and purity < 83.3):
    print("18K")


'''


"""


24K – 99.9%
22K – 91.7%
20K – 83.3%
18K – 75.0%

"""
