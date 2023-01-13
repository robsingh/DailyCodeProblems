"""
Currying is a specific kind of argument binding, in which we create a sequence of functions that each take
exactly one argument. We can implement this using a decorator.
signature will check how many arguemts a function takes.
We can bind arguments to a function, so that we end up with a function that takes one argument less than the original function.
This is done using functools.partial()

"""

from inspect import signature
from functools import partial

def curry(func):
    def inner(arg):
        if len(signature(func).parameters) == 1:
            return func(arg)
        return curry(partial(func, arg))
    
    return inner

@curry
def add(a,b,c):
    return a + b + c

# print(add(10)(100)(1000))
add_10 = add(10)
add_10_100 = add_10(100)
print(add_10_100(1000))