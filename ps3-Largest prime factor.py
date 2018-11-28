# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


import math
def isPrime(x):
    """
    if x is a prime number return True,else return False
    """
    if x == 1:
        return False
    else:
        k = int(math.sqrt(x))
        for i in range(2,k+1):
            if x % i == 0:
                return False
        return True

def largestPrimeFactor(num):
    i = 2
    result = 2
    
    while True:
        if num % i == 0 and isPrime(i) == True:
            num = num/i # divide the number by the least prime number each time
            result = i
        if num == 1:
            break
        i +=1
    
    return result

# define number n
num =  600851475143
print(largestPrimeFactor(num))
