# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# numbers are in file "numbers.txt"



def LargeSum(filename):
    f = open(filename,"r")
    filelist = f.readlines()
    numlist = []
    for line in filelist:
        temp = line.strip("\n")
        numlist.append(temp)
    sum = 0
    for line in numlist:
        sum += int(line)
    strsum = str(sum)
    result = ""
    for i in range(10):
        result += strsum[i]
    return result

print(LargeSum("numbers.txt"))
