"""
This problem was asked by Stripe.

reduce (also known as fold) is a function that takes in an array, a combining function, 
and an initial value and builds up a result by calling the combining function on each element of the array, left to right. 
For example, we can write sum() in terms of reduce:

def add(a, b):
    return a + b

def sum(lst):
    return reduce(lst, add, 0)

This should call add on the initial value with the first element of the array,
and then the result of that with the second element of the array, and so on until we reach the end, when we return the sum of the array.

Implement your own version of reduce.
"""

def reduce(lst, func, initial_value):
    """
    Args:
        lst: input to be reduced
        func: function used to reducing the list
        initial_value: 
            for addition function, initial_value should be 0
            for multiplication function, initial_value should be 1, (can't be zero because anything multiplied with zero is zero)

    Return:
        resut[list[int]]
    """
    result = initial_value
    for item in lst:
        result = func(result, item)
    return result

def add(a,b):
    return a + b

def sum(lst):
    return reduce(lst, add, 0)


numbers = [0,1,2,3,4,5]
print(sum(numbers))
