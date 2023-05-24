"""
The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. 
The method is to take increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), then [6, 9, 12, ...]
 (multiples of three), and so on. Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.

Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).
"""

def sieve_of_eratosthenes(N):
    """
    create a boolean array and initialize all enteries as True.
    A value in the array will finally be false if i is not a prime, else True.
    """
    is_prime = [True] * (N+1)
    is_prime[0] = is_prime[1] = False # 0 and 1 are not prime
    p = 2
    while p * p <= N:
        #if is_prime[p] is not changed, then it is a prime
        if is_prime[p]:
            #update all multiples of p
            for i in range(p*p, N+1, p):
                is_prime[i] = False
        p += 1
    
    # generate the list of prime numbers
    primes = [i for i in range(2, N+1) if is_prime[i]]
    return primes


#generator to produce primes indefinitely
def prime_generator():
    is_prime = {} #dictionary to store primes and their multiples
    n = 2 # start with the first prime number

    while True:
        if n not in is_prime:
            yield n
            is_prime[n*n] = [n] #mark its multiples for future composites
        else:
            for p in is_prime[n]:
                is_prime.setdefault(n+p, []).append(p) #add next multiple
            del is_prime[n]
        
        n += 1


generator = prime_generator()
primes = [next(generator) for _ in range(20)]
print(primes)
