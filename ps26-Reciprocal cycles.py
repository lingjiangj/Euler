# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


import math
import time

start = time.time()
# calculate the prime factor of denominators

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

# calculate the length of recurring cycle of 1/n, when n is a prime number
    
def lengthOfRecurCycle(n):
    """
    n is a prime number. Return the length of recuring cycle of number 1/n
    the length of recurring cycle of a prime number is the minimal k that 10^k-1 is divisable by n
    质数（即素数）循环节的长度是使分母P整除10^k-1的最小k值
    """
    k = 1
    while True:
        if (10**k - 1) % n ==0:
            break
        elif n==2 or n ==5:
            k = 0
            break
        else:
            k += 1
    return k

# create a dictionary which includes all the length of recuring cycle of number 1/n, where n<limit and n is a prime

def dict_RecurCycle(limit):
    """
    return a dictionary, keys are prime numbers less than limit,
    values are the length of recuring cycle of number 1/key
    """
    dict = {}
    for i in range(2,limit+1):
        if isPrime(i) == True:
            dict[i] = lengthOfRecurCycle(i)
    return dict
            

# return the longest length of recurring cycle of 1/d, d < upperlimit  

def Reciprocalcycles(upperlimit):
   """
   Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
   1. find the prime factors of d
   2. calculate lengthOfRecurCycle() for the prime factors of d
   3. length of recurring cycle in d's decimal is the product of all the length of recurring cycle of d's prime factors
   """
   dictionary= dict_RecurCycle(upperlimit)
   d = 2
   maxLength = 0
   while d <= upperlimit:
       primeFact = PrimeFact(d)
       tempLength = 1
       for n in primeFact:
           tempLength *= dictionary[n]
       if maxLength<tempLength:
           maxLength = tempLength
           result = d
       d += 1
       
   return result,maxLength

print(Reciprocalcycles(1000))
print(time.time()-start)
