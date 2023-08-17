"""Write a function, add_subtract, which alternately adds and subtracts curried arguments
add_subtract(-5)(10)(3)(9) -> -5 + 10 - 3 + 9 -> 11
"""
"""
Currying is a specific kind of argument binding, in which we create a sequence of functions that each take
exactly one argument. We can implement this using a decorator.
signature will check how many arguemts a function takes.
We can bind arguments to a function, so that we end up with a function that takes one argument less than the original function.
This is done using functools.partial()
"""

import functools

class CurriedFunction:
    def __init__(self, func, *args):
        self.func = func
        self.args = args

    def __call__(self, *curried_args):
        args = self.args + curried_args
        return CurriedFunction(self.func, *args)

    def evaluate(self):
        result = self.args[0]
        operator = 1

        for arg in self.args[1:]:
            result += operator * arg
            operator *= -1

        return result

def add_subtract(*args):
    return CurriedFunction(None, *args)

result = add_subtract(-5)(10)(3)(9).evaluate()
print(result)  # Output: 11
