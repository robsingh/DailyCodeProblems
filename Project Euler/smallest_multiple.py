'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

'''
break number into prime factors.
take the highest power that appears in the prime factor.
product of these highest powers = LCM
'''
from math import gcd

def lcm(a,b):
    return a * b // gcd(a,b)

def lcm_range(n):
    result = 1
    for i in range(1, n+1):
        result = lcm(result, i)
    return result

print(lcm_range(20))