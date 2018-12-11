# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def totalmult(limits):
    n = 1
    sum = 0
    while n < limits:
        if n % 5 ==0 or n % 3 ==0:
            sum +=n
        n +=1
    return sum

# set upper limits
limits = 1000
print("The sum is",totalmult(limits))

        
