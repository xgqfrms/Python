import math

__author__ = 'xray'
x_rate = 0.65
total_dollars = 200
fee = 2
total_pounds = (total_dollars - fee) * x_rate
print total_pounds

total_pounds -= 100
print total_pounds


total_dollars = (total_pounds/x_rate)-fee
print total_dollars

total_dollars = math.ceil(total_pounds/x_rate)-fee
print total_dollars


""" This is an example of a multiline
128.7
28.7
42.1538461538
43.0
"""