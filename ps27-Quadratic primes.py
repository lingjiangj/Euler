# Euler discovered the remarkable quadratic formula:
# n2+n+41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

# The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

# Considering quadratics of the form:

# n2+an+b, where |a|<1000 and |b|≤1000

# where |n| is the modulus/absolute value of n
# e.g. |11|=11 and |−4|=4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n,starting with n=0.


import math
import time
start = time.time()
def ifPrime(n):
    if n <= 1:
        return False
    else:
        k = int(math.sqrt(n))
        for i in range(2,k+1):
            if n % i == 0:
                return False
    return True

def numOfPrime(a,b):
    """
    return the number of primes for the consecutive integer for formula:
    n2+an+b , where |a|<1000 and |b|≤1000
    """
    n = 0
    while True:
        formula = n**2 + a*n + b
        if ifPrime(formula) == True:
            n += 1
        else:
            break
    return n

def coeffi(limit):
    """
    return coefficients a,b for the formula n2+an+b , where |a|<limit and |b|≤limit,limit >= 0
    that produces the maximum number of primes for consecutive values of n, starting with n=0.
    """
    a = -limit
    maximum = 0
    while a <= limit:
        b = -limit
        while b <= limit:
            temp = numOfPrime(a,b)
            if temp > maximum:
                maximum = temp
                max_a = a
                max_b = b
            b += 1
        a += 1
    prod = max_a * max_b
    return prod,max_a,max_b

print(coeffi(1000))
print(time.time()-start)
