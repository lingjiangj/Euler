# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

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

def SmallestMult(n):
    """
    find the smallest positive number that is evenly divisible by all of 
    the numbers from 1 to n
    """
    totalDict = {}
    for num in range(n,0,-1):
        tempDict = {}
        # construct a dict, all the keys are the prime factors of num,
        # all the values are the number of times each prime factors appears in num
        k = 2
        while True:
        # find all the prime factors of num and update tempDict
            if isPrime(k) == True:
                tempDict[k] = 0
                while num % k == 0:
                    tempDict[k] +=1
                    num = num/k # divide the number by the least prime number each time
            if num == 1:
                break
            k +=1
            
        for key in tempDict:
            if key not in totalDict:
                totalDict[key] = tempDict[key]
            elif totalDict[key] < tempDict[key]:
                totalDict[key] = tempDict[key]
            else:
                continue
    
    result = 1
    for prime in totalDict:
        result *= prime**(totalDict[prime])
    
    return result

print(SmallestMult(20))

