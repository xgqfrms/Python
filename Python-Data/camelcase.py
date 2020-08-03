# coding: utf8

# import camelcase
# import CamelcasedModule as camelcased_module
import CamelCase as camelcase

# ModuleNotFoundError: No module named 'Camelcase'

c = camelcase.CamelCase()
# AttributeError: module 'camelcase' has no attribute 'CamelCase'

txt = "hello world"

print(c.hump(txt))


