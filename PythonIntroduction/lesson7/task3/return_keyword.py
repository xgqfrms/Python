def sum_two_numbers(a, b):
    return a + b            # return result to the function caller

c = sum_two_numbers(3, 12)  # assign result of function execution to variable 'c'


def fib(n):
    """This is documentation string for function. It'll be available by fib.__doc__()
    Return a list containing the Fibonacci series up to n."""
    result = []
    a = 0
    b = 1
    while a < n:
        result.append(a)  # 0 1
        tmp_var = b  # 1 1
        b = a + b  # 1
        a = tmp_var  # 0
        # print(a)
    return result

print(fib(10))