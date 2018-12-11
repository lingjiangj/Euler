# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 21000?

def PowerDigSum(n):
    num = 2**n
    strNum = str(num)
    sum = 0
    for i in strNum:
        sum += int(i)
        
    return sum

print(PowerDigSum(1000))
        
