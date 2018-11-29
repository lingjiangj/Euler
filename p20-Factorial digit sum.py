# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

def factsum(n):
    
    num = fact(n)
    strnum = str(num)
    result = sum(int(strnum[i]) for i in range(len(strnum)))
    
    return result

print(factsum(100))
