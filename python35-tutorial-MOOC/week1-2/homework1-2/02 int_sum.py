#!/usr/bin/python
# -*- coding: utf8 -*-

__author__ = 'xray'

'''
(2) 整数序列求和。
用户输入一个正整数 N，计算从 1 到 N（包含1和N）相加之后的结果。
'''
n = input(" 请输入整数 N: ")
Sum = 0
for i in range(int(n)):
    Sum += i + 1
print("1 到 到 N  求和结果: ", Sum)