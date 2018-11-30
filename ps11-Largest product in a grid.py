# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
# the grid is shown in file "ps11-numbers.txt"

f = open("ps11-numbers.txt","r")
filelists = f.readlines()
numList = []
for line in filelists:
    temp = line.strip("\n")
    temp = temp.split(" ")
    numList.append(temp)
print(numList)
max1 = 0
for l in range(17): # vertical
    for n in range(20):
        try:
            tempProd = int(numList[l][n])*int(numList[l+1][n])*int(numList[l+2][n])*int(numList[l+3][n])
            if tempProd > max1:
                max1 = tempProd

        except:
            pass
max2 = 0
for l in range(20): # horizontal
    for n in range(20):
        try:
            tempProd = int(numList[l][n])*int(numList[l][n+1])*int(numList[l][n+2])*int(numList[l][n+3])
            if tempProd > max2:
                max2 = tempProd
        except:
            pass
max3 = 0
for l in range(20): # diagonally(left to right)
    for n in range(20):
        try:
            tempProd = int(numList[l][n])*int(numList[l+1][n+1])*int(numList[l+2][n+2])*int(numList[l+3][n+3])
            if tempProd > max3:
                max3 = tempProd

        except:
            pass

max4 = 0
for l in range(20): # diagonally(right to left)
    for n in range(20):
        try:
            tempProd = int(numList[l][n])*int(numList[l+1][n-1])*int(numList[l+2][n-2])*int(numList[l+3][n-3])
            if tempProd > max4:
                max4 = tempProd
        except:
            pass

print(max(max1,max2,max3,max4))
