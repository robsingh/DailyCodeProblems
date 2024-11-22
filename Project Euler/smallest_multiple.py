'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

'''
break number into prime factors.
2 = 2
3 = 3
4 = 2^2
5 = 5
6 = 2*3
7 = 7
8 = 2^3
...
20 = 2^2*5
take the highest power that appears in the prime factor.
2^4 (16)
3^2 (9)
5^1 (5)
7^1 (7)
11,13,17,19 - prime nums

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

