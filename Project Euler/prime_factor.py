'''
The prime factors of 13195 are 5,7,13, and 29.
What is the largest prime factor of the number 600851475143?
'''
'''
prime factor : prime number divisible by 1 and itself.
start with smallest prime number to check if it divides the number.
if it does, keep dividing until it no longer divides.
any factor greater than square root must also be a prime.
'''

def largest_prime(number:int):
    # start with smallest prime factor
    factor = 2

    # keep dividing number by current factor until it is divisible
    while number % factor == 0:
        number //= factor

    # move on to next odd number
    factor = 3
    # check all possible factors upto square root of n
    while factor * factor <= number:
        while number % factor == 0:
            number //= factor
        factor += 2 # increment to next odd number
    
    # if number is still greater than 1, it is a prime factor
    return number if number > 1 else factor

    
number = 600851475143
print(largest_prime(number))