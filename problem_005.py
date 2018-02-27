# -*- coding: utf-8 -*-
"""
Project Euler Problems
----------------------
Smallest multiple :

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Solution is : 232792560

"""
cnt_start = 1
cnt_end = 20
factorial = cnt_start

for i in range(cnt_start,cnt_end+1):
	factorial = factorial * i

print("The factorial of ",cnt_end,"is",factorial)

#factorial = factorial - 1 
j = cnt_end
flag = False
while j <= factorial and flag != True:    
    for i in range(cnt_start,cnt_end+1):
        if (j % i) != 0 :
            flag = False
            break        
        elif i == cnt_end:
            flag = True
            print("True")
            print(j)
        elif (j % 500000000) == 0 :
            print(j)
    j = j + 1