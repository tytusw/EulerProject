# -*- coding: utf-8 -*-
"""
Project Euler Problems
----------------------
Special Pythagorean triplet :

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Solution is : 200 + 375 + 425 = 1000 --> 200 * 375 * 425 = 31875000
"""
result = 0
a_sq = 0
b_sq = 0
c_sq = 0

for a in range(1,1000):
    for b in range(a + 1,1000):
        for c in range(b + 1,1000):
            result = a + b + c
            if result == 1000:
                a_sq = a**2
                b_sq = b**2
                c_sq = c**2
                if (a_sq + b_sq) == c_sq:
                    print(a,"+",b,"+",c,"=",result)
                    print(a,"x",b,"x",c,"=",a*b*c)







