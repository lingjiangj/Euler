# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

import time

t1 = time.time()

def NumOfTerms(num):
    count = 1 # the list of Terms includes number itself
    while num != 1:
        if num % 2 == 0:
            num /= 2
            count +=1            
        else:
            num = num*3 + 1
            count +=1 
    return count
    
def LongestCollatz(upperlimit):
    longestTerms = 0
    for i in range(1,upperlimit):
        tempTerms = NumOfTerms(i)
        if tempTerms > longestTerms:
            longestTerms = tempTerms
            result = i
            
    return longestTerms,result


print(LongestCollatz(1000000))   
t2 = time.time()  
time = t2-t1
print(time)

