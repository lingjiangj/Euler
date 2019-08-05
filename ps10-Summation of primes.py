# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.


import math
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def sumPrime(n):
    """
    n is the upper limit
    """
    total = 0
    for i in range(2,n+1):
        if isPrime(i) == True:
            total += i
            
    return total


print(sumPrime(2000000))
  
