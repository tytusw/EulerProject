# -*- coding: utf-8 -*-
"""
Project Euler Problems
----------------------
Lattice paths :

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

Solution :
2x2 => 6
3x3 => 20
4x4 => 70
5x5 => 252
6x6 => 924
7x7 => 3432
8x8 => 12870
9x9 => 48620
10x10 => 184756
11x11 => 705432

"""


move_right = 2 #right = logic 0
move_down = move_right #down = logic 1, move_down = move_right if  if the grid is symetric
bit_nbr = move_down
#val_min = 0b0000000011111111
val_min = 0
#val_max = 0b1111111100000000
val_max = 0
bit_cnt = 0
way_cnt = 0

for i in range(bit_nbr):
	val_min = (val_min << 1) + 1

val_max = val_min << move_right

print("for a",move_right,"x",move_down)
print("val min =",bin(val_min))
print("val max =",bin(val_max))

for i in range(val_min,val_max + 1):
    temp = i
    bit_cnt = 0
    while temp != 0 :
        if temp % 2 == 1 :
            bit_cnt = bit_cnt + 1
        temp = temp >> 1
    if bit_cnt == bit_nbr :
        way_cnt= way_cnt + 1
        print(i,"=>",bin(i))
        
print("nbr of way =",way_cnt)









