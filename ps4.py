# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def isPal(num):
    numStr = str(num)
    numlist = [numStr[i] for i in range(len(numStr))]
    for i in range(0,len(numlist)//2):
        if numlist[i] != numlist[len(numlist)-1-i]:
            return False
    return True

def largestPal():
    list = []
    for num1 in range(999,500,-1):
        for num2 in range(999,500,-1):
            if isPal(num1*num2) == True:
                list.append(num1*num2)
    return max(list)

print(largestPal())
