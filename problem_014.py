# -*- coding: utf-8 -*-
"""
Project Euler Problems
----------------------
Longest Collatz sequence :



The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.


Solution is : for i = 837799 the length is 525

"""

def get_collatz_length(val) :
    cnt = 1
    while val != 1 :
        print(val)
        if val % 2 == 0 :
            val = val / 2
        else:
            val = val * 3 + 1
        cnt = cnt + 1
    return cnt
 
get_collatz_length(14)
"""	
length = 0
prev_i = 0
prev_length = 0

for i in range(1,1000001):
    length = get_collatz_length(i)
    if prev_length < length:
        prev_length = length
        prev_i = i

print("for i =",prev_i,"the length is",prev_length)
"""










