# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 09:12:13 2017

@author: wilczews
"""

N = 999
n1 = 3
n2 = 5
n1_div = int(N / n1)
n2_div = int(N / n2)
n1_n2_div = int(N / (n1 * n2))
sum_n1 = 0
sum_n2 = 0
sum_n1_n2 = 0

for i in range(1,n1_div + 1):
    sum_n1 = sum_n1 + i*n1

for i in range(1,n2_div + 1):
    sum_n2 = sum_n2 + i*n2

for i in range(1,n1_n2_div + 1):
    sum_n1_n2 = sum_n1_n2 + i*n1*n2

print(sum_n1 + sum_n2 - sum_n1_n2)