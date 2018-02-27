# -*- coding: utf-8 -*-
"""
Project Euler Problems
----------------------
Sum square difference :

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Solution is : 25164150

"""
cnt_start = 1
cnt_end = 100

sum_of_sq = 0
sq_of_sum = 0

for i in range(cnt_start, cnt_end + 1) :
	sum_of_sq = sum_of_sq + (i**2)
	sq_of_sum = sq_of_sum + i	
	
print("The result is", (sq_of_sum**2) - sum_of_sq)