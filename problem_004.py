# -*- coding: utf-8 -*-
"""
Project Euler Problems
----------------------

Largest palindrome product :

A palindromic number reads the same both ways. The largest palindrome made from
 the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

def is_str_palindrome(string):
    if type(string) != str :
        #print("The input value is not string type" )
        return False
    str_len = len(string)
    
    if str_len % 2 != 0 or str_len <= 0:
        #print("The input value has not a even number of characters")
        return False
    
    i = 0 #counter which starts from the start
    j = str_len - 1 #counter which starts from the end
    
    while i < str_len / 2 :
        if string[i] != string[j]:
            #print("The input value is not a palindrome")
            return False
        i = i + 1
        j = j - 1
    
    return True
    


x = 999
y = 999

while x > 499 :
    while y > 499 :
        if is_str_palindrome(str(x*y)) == True:
            print("x =",x,"y =",y,"result =",x*y)
        y = y - 1
    y = 999
    x = x - 1
    
