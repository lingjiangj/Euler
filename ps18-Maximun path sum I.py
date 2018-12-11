#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:13:11 2018

@author: jianglindsey
"""
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

#   3
#  7 4
# 2 4 6
#8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom of the triangle in file "ps18-numbers.txt"

def MaxPathSum():  
    #open the number file and generate lists of numberlists for each line of the file 
    filename = "ps18-numbers.txt"
    f = open(filename,"r")
    filelist = f.readlines()
    numlist = []
    for line in filelist:
        temp = line.strip("\n")
        temp = temp.split(" ")
        numlist.append(temp)
    #generate a dictionary which contains the largest sum of each number in the line added numbers under it
    totalTri = {} 
    # put last line of numbers in dictionary
    # (m,n) refers to the nth number in mth line.
    totalline = len(numlist)
    i = 1
    for num in numlist[totalline-1]:
        totalTri[(totalline,i)] = int(num)
        i += 1
    
    line = totalline - 1 # start from the second line from bottom
    while line > 0 :
        curLine = numlist[line-1] #number list of current line
        for n in range(len(curLine)):
            totalTri[(line,n+1)]=int(curLine[n])+max(totalTri[(line+1,n+1)],totalTri[(line+1,n+2)])
        line -= 1
    return totalTri[(1,1)]    

           
print(MaxPathSum())

