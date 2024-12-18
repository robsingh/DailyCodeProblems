'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
Find the sum of all primes below 2 million.
'''

def prime_sum(limit):
    # initialize a list to mark prime numbers
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    # start marking multiples of primes as non-prime
    p = 2
    while p * p <= limit:
        if is_prime[p]: # if p is still marked as prime
            for multiple in range(p*p, limit + 1, p): # mark multiples of p
                is_prime[multiple] = False
        p += 1
    
    return sum(num for num, prime in enumerate(is_prime) if prime)


limit = 2000000
print(prime_sum(limit))
