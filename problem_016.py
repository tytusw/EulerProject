# -*- coding: utf-8 -*-
"""
Project Euler Problems
----------------------
Power digit sum :

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

Solution :

"""
val = str(2**1000)
somme = 0

for i in range(len(val)):
    somme = somme + int(val[i])

print (somme)










