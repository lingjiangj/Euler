# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


def fifthPowers():
    fifthPowerList = [i**5 for i in range(0,10)]
    result = []
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                for l in range(0,10):
                    for m in range(0,10):
                        for n in range(0,10):
                            digit = i + (10*j) + 100*k + 1000*l + 10000*m + 100000*n
                            sumfifthPower = fifthPowerList[i]+fifthPowerList[j]+fifthPowerList[k]+fifthPowerList[l]+fifthPowerList[m]++fifthPowerList[n]
                            if digit == sumfifthPower:
                                result.append(digit)
    return sum(result)-1

print(fifthPowers())
