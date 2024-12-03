'''
The sum of squares of first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385.
The square of sum of first ten natural numbers is, (1+2+3+...+10)^2 = 55^2 = 3025

Hence the difference between the sum of square of first ten natural numbers and square of the sum is = 3025 - 385 = 2640
Find the difference between the sum of square of first one hundred natural numbers and the square of the sum.
'''

n = 100

#calculate sum of squares
sum_of_squares = n * (n + 1) * (2 * n + 1) // 6

#calculate square of the sum
sum_of_natural_nums = n * (n + 1) // 2
square_of_sum = sum_of_natural_nums ** 2

diff = square_of_sum - sum_of_squares
print(diff)