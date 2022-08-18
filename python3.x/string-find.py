#!/usr/bin/env python3
#!/usr/bin/python3

# coding: utf-8
# coding: utf8
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


def search(word, text):
  print(word.find(text))
  if(word.find(text) > -1):
    return "Word found"
  else:
    return "Word not found"

text = input()
word = input()

print(search(text, word))


"""
The search() function should return "Word found" if the word is present in the text, or "Word not found", if it’s not.
"""
