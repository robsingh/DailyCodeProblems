'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, 
for which a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2

There exists exactly one Pythagorean triplet for which a + b + c = 1000
Find the product abc.
'''
'''
constraints:
1. a < b < c
2. a**2 + b ** 2 + c **2
3. a + b + c = 1000
'''

def find_triplet(sum_value):
    for a in range(1, sum_value // 3):
        b = (sum_value * (sum_value - 2 * a)) // ( 2 * (sum_value - a))
        c = sum_value - a - b
        if a * a + b * b == c * c:
            return a,b,c, a * b * c
            
a,b,c, product = find_triplet(1000)
print(f"Triplet is a = {a}, b = {b}, c = {c}")
print(f"Product is = {product}")
