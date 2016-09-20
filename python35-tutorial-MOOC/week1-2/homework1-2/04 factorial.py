# coding: utf8

__author__ = 'xray'

'''
 （4 ）阶乘计算。计算 1+2!+3!+...+10! 的结果。
'''
Sum, tmp = 0, 1
# for i in range(0, 11):
#     tmp *= i
for i in range(0, 9):
    tmp *= (i + 1)
    Sum += tmp
print(" 运算结果是: {}".format(Sum))

# 409113  (9)
# 4037913 (10)





