
# Decorators with Arguments

"""

https://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html#decorators-with-arguments
https://www.geeksforgeeks.org/decorators-with-parameters-in-python/
https://stackoverflow.com/questions/5929107/decorators-with-parameters

"""

# PythonDecorators/decorator_with_arguments.py
class decorator_with_arguments(object):
  def __init__(self, arg1, arg2, arg3):
    # TypeError: __init__() takes 4 positional arguments but 5 were given
    """
      If there are decorator arguments, the function
      to be decorated is not passed to the constructor!
    """
    print("1. Inside __init__()")
    self.arg1 = arg1
    self.arg2 = arg2
    self.arg3 = arg3

  def __call__(self, f):
    """
      If there are decorator arguments, __call__() is only called
      once, as part of the decoration process! You can only give
      it a single argument, which is the function object.
    """
    print("2. Inside __call__()")
    def wrapped_f(*args):
      print("\n5. Inside wrapped_f()")
      print("6. Decorator arguments:", self.arg1, self.arg2, self.arg3)
      f(*args)
      print("8. After f(*args)")
    # return OK ✅ ??? __call__ 闭包函数 ???
    return wrapped_f
      # return bug ❌
      # return wrapped_f

# @decorator_with_arguments("a1", "a2", "a3")
# def sayHello(a1, a2, a3,):
#   print('sayHello arguments:', a1, a2, a3)

@decorator_with_arguments("a1", "a2", "a3")
# 3 个参数
def sayHello(a1, a2, a3, a4):
  # 4 个参数
  print('7. sayHello arguments:\n', a1, a2, a3, a4)


# print("3. After decoration")
# print("4. Preparing to call sayHello()")

sayHello("say", "hello", "argument", "list")
# TypeError: 'NoneType' object is not callable

print("9. after first sayHello() call\n")

sayHello("a", "different", "set of", "arguments")

print("9. after second sayHello() call")


"""

# test
$ python3 decorators-at-with-arguments.py

"""
