# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import itertools 
import numpy

def prime_divisors(n):
    '''
    this function returns all prime factors of number n (with repeats)
    it does so by striping n of its prime factors from smallest to biggest 
    this method relies on the number in question not having a single huge prime factor
    '''
    factors=[]
    while n % 2 == 0:
        factors.append(2)
        n = n/2
    k = 3
    while n != 1:
        while n % k == 0:
            factors.append(k)
            n /= k
        k = k+1
    return factors 

def sum_all_factors(n):
    '''
    function returns SUM of all divisors (excluding n) of the number n
    '''
    primeFact = prime_divisors(n)
    allFact = set()
    for i in range(1,len(primeFact)+1):
        factor_composition = list(itertools.combinations(primeFact,i))        
        for j in range(0,len(factor_composition)):
            allFact.add(numpy.prod(factor_composition[j]))
    allFact=list(allFact)
    if n!=1:
        allFact.remove(n)
    allFact.append(1)
    total=sum(allFact)
    return total

def non_abundant_sum():
    abundant = []
    numbers = set(range(1,28124))
    for i in range(1,28124):
        if i < sum_all_factors(i): # if abundant
            abundant.append(i)
    combo = list(itertools.combinations_with_replacement(abundant,2))
    combosum = set()
    for j in range (0, len(combo)):
        combosum.add(sum(combo[j]))
    remaining = numbers - combosum
    return sum(remaining)

print(non_abundant_sum())
