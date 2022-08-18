
#!/usr/bin/env python3
# coding=utf-8

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
   * @created 2022-08-17
   *
   * @description
   * @augments
   * @example
   * @link
   *
  */
"""



#your code goes here

strs = input();
# this is awesome
# abc xyz


arr = list(strs[::])

# print(arr)
# ['a', 'b', 'c', ' ', 'x', 'y', 'z']

# reverse 没有返回值 ❌
# ss = arr.reverse()
# print(ss)
# None

# 反转 list ✅
arr.reverse()

# print(arr)
# ['z', 'y', 'x', ' ', 'c', 'b', 'a']

print(''.join(arr))


"""

l = len(arr)
# print(l)

result = ''

while(l) :
  result += arr[l - 1];
  l -= 1

print(result)

"""

"""

l = len(arr)
# print(l)

result = ''

# TypeError: 'int' object is not iterable ❌
for i in l:
  result += arr[len - i - 1]

print(result)



"""





"""

list.pop([index=-1])


https://www.runoob.com/python3/python3-list.html

list.reverse()

https://www.runoob.com/python3/python3-att-list-reverse.html


"""

