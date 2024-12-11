'''
By listing the first six prime numbers: 2,3,5,7,11, and 13, we can see that the 6th prime number is 13.
What is the 10001st prime number?
'''

'''
but there is a problem with this brute force approach, we are not leveraging previous computations for subsequent checks. 
Also, the complexity grows and it can become slow for large values of n.
If we can solve it using Sieve of Erathosthenes, then maybe we can avoid recalculating divisors for each number. Will do it. 
'''
#brute force
def is_prime(n):  
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
                   

def find_nth_prime(n):
    """Find the nth prime number."""
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num


nth_prime = find_nth_prime(10001)
print(f"The 10001st prime number is {nth_prime}")
