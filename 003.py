# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 22:01:10 2017

@author: g

Find largest prime factor of the number 600851475143.
Can probably refine using a generator, but this works quick enough.
"""

upper = int(input("Give a positive integer: "))
ans = 0

def checkFactor(number):
    if number == 2:
        return 2
        
    for i in range(2,number+1):
        if number%i == 0:
            if i == number: 
                return number
            else: 
                return checkFactor(int(number/i))
            
print(checkFactor(upper))