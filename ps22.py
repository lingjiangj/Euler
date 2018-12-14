# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

import string

def AlphaValue(word):
    """
    word is a string, the function return the  the alphabetical value for the word
    """
    alphaStr = string.ascii_uppercase
    value = 0
    for i in word:
        value += alphaStr.index(i)+1
        
    return value
    

f = open("ps22_names.txt")
file = f.read().split(",")
names = []
for i in file:
    names.append(i.strip('"'))

names.sort()

sum = 0
for n in names:
    a = AlphaValue(n)
    b = names.index(n)+1   
    sum += a*b
    
print(sum)
    
        


    
  