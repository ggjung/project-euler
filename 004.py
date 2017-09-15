# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 11:31:02 2017

@author: g

Project Euler 
Problem 4

Find the largest palindrome made from the product of two 3-digit numbers.

Might be faster to make large palindromes and check if they have correct factors?
"""

largestPal = 0
palindromeFlag = False

for i in range(1000,100,-1): 
    
    for j in range(999,i-1,-1):
        
        product = str(i*j) 
        
        palindromeFlag = True

        for k in range(len(product)//2): 
            if product[k] != product[len(product)-1-k]: 
                palindromeFlag = False
                break
        
        if palindromeFlag == True:
            if int(product) > int(largestPal): 
                largestPal = product

print("Largest palindrome solution: " + largestPal)

