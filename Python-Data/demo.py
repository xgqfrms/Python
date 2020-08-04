# coding: utf8

# import Module
# 导入整个模块
# import camelcase

# 模块名.函数名
# c = camelcase.CamelCase()
# txt = "hello world"
# print(c.hump(txt))

# from Module import Function
# 导入部分模块
from camelcase import CamelCase

函数名
c = CamelCase()
txt = "hello world"
print(c.hump(txt))


# import Module as Alias_Module
# 导入整个模块, 并且使用 Alias 模块别名
# import camelcase as cc

# c = cc.CamelCase()
# txt = "hello world"
# print(c.hump(txt))


"""bug

  # ModuleNotFoundError: No module named 'Camelcase'
  # AttributeError: module 'camelcase' has no attribute 'CamelCase'

  # This method capitalizes the first letter of each word.
"""

