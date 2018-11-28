# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?


import math
def isPrime(num):
    
    if num <= 1:
        return False
    else:
        k = int(math.sqrt(num))
        for i in range(2,k+1):
            if num % i == 0:
                return False
        return True
    
def nth_prime(n):
    count = 0
    k = 1
    
    while count < n:
        k +=1
        if isPrime(k) == True:
            count +=1

    return k

print(nth_prime(10001))
