#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 22:12:43 2019

@author: xgqfrms-mbp
"""

# coding: utf-8
from __future__ import division

def jia(x,y):
    print(x+y);

def jian(x,y):
    print(x-y);

def cheng(x,y):
    print(x*y);

def chu(x,y):
    print(x/y);

operator = { '+': jia, '-': jian, '*': cheng, '/': chu, };

# operator = {
#   '+ : jia,
#   '-' : jian,
#   '*' : cheng,
#   '/' : chu
# };
# SyntaxError: EOL while scanning string literal

def f(x,o,y):
    operator.get(o)(x,y);

f(3,'+',2);
# 5
