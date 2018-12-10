# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


import math

def pythagoreantriplet(sum):
    for c in range(math.ceil(sum/3),sum-3):
        for b in range(math.ceil((sum-c)/2),2,-1):
            a = sum - b - c
            if a*a +b*b == c*c:
                return a*b*c

print(pythagoreantriplet(1000))
