
# Decorators with Arguments

"""

https://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html#decorators-with-arguments
https://www.geeksforgeeks.org/decorators-with-parameters-in-python/
https://stackoverflow.com/questions/5929107/decorators-with-parameters

"""


# decorator factory

def decorator_factory(argument):
  def decorator(function):
    def wrapper(*args, **kwargs):
      funny_stuff()
      something_with_argument(argument)
      result = function(*args, **kwargs)
      more_funny_stuff()
      return result
    return wrapper
  return decorator
