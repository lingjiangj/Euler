# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

import math
import itertools
import numpy
import time

start = time.time()
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def PrimeFact(n):
    """
    the function returns all the prime factors of nunber n(with repeats)
    """
    primeFact = []
    k = 2
    while True:
        if isPrime(k) == True:
            while n % k == 0:
                primeFact.append(k)
                n = n/k
        if n == 1:
            break
        k = k+1
    
    return primeFact
  
def sum_all_fact(n):
    """
    the function returns the sum of all factors of number n
    """
    primeFact = PrimeFact(n)
    allFact = []
    for i in range(1,len(primeFact)+1):
        factor_composition = list(itertools.combinations(primeFact,i))
        for j in factor_composition:
            prod = numpy.prod(j)
            if prod not in allFact:
                allFact.append(prod)
                
    if n > 1:
        allFact.remove(n)
        allFact.append(1)
        total = sum(allFact)
    else:
        total = 1
    return total


def AmicNumSum(limit):
    AmicPair = set()
    for num in range(2,limit):
        a = sum_all_fact(num)
        b = sum_all_fact(a)
        if num==b and num != a:
            AmicPair.update([a,b])
                
    print(AmicPair)
    total = sum(AmicPair)
    return total
 
print(AmicNumSum(10000))
print(time.time()-start)   
