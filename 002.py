# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 21:24:43 2017

@author: g

Project Euler 
Problem 2

Finds the sum of even Fibonacci numbers less than 4mil.
Solved recursively.
"""

ans = 0

def fibo(minOneTerm, minTwoTerm, ans):    
    nthTerm = minOneTerm + minTwoTerm
    if nthTerm%2 == 0:
        ans += nthTerm
    
    if nthTerm > 4000000: 
        nthTerm = minOneTerm
        return ans
    
    else: 
        return fibo(nthTerm,minOneTerm, ans)
        
print(fibo(1,1,0))