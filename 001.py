# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 21:06:46 2017

@author: g

Project Euler 
Problem 1

Finds the sum of multiples of 3 and 5 below 1000.
"""

sumOfThrees = 0
sumOfFives = 0
sumOfFifteens = 0

upper = int(input("Give a positive integer: "))
upper -= 1

multiplesOfThree = upper//3

multiplesOfFive = upper//5

multiplesOfFifteen = upper//15

for i in range(multiplesOfThree):
    sumOfThrees = sumOfThrees + (i+1)*3
    
for j in range(multiplesOfFive):
    sumOfFives = sumOfFives + (j+1)*5
    
for k in range(multiplesOfFifteen):
    sumOfFifteens = sumOfFifteens + (k+1)*15
    
ans = sumOfThrees + sumOfFives - sumOfFifteens

print("Sum of multiples of 3 and 5: " + str(ans))