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
12x12 => 2704156
13x13 => 10400600
14x14 => 134209536

20x20 => 137846528820 -> Pascal s triangle => 40! / (20!)²

All what follow is over-kill
"""
def fill_pascal_triangle(val):
    i = len(val)
    j = len(val[0])
    x =  1
    y =  1

    while x < i and y < j :
        val[x][y] = val[x-1][y] + val[x][y-1]
        x = x + 1
        y = y + 1
    print(val)

move_right = 5 #right = logic 1
move_down = move_right #down = logic 0, move_down = move_right if  if the grid is symetric
tab = [ [ 1 for y in range( move_down ) ] for x in range( move_right ) ]
fill_pascal_triangle(tab)


"""
bit_nbr = move_down

val_min = 0

bit_cnt = 0
way_cnt = 0

val_min = 2**move_right - 1 #e.g. => val_min = 0b0011
val_max = val_min << move_down #e.g. => val_max = 0b1100


print("for a",move_right,"x",move_down)
print("val min =",bin(val_min)[2:].zfill(move_right + move_down))
#print("val min =",val_min)
print("val max =",bin(val_max)[2:].zfill(move_right + move_down))
print("val max =",val_max)

for i in range(val_min,val_max + 1):
    temp = i
    bit_cnt = 0
    while temp != 0 :
        if temp % 2 == 1 :
            bit_cnt = bit_cnt + 1
        temp = temp >> 1
    if bit_cnt == bit_nbr :
        way_cnt= way_cnt + 1
        #print(i,"=>",bin(i)[2:].zfill(move_right + move_down))

print("nbr of way =",way_cnt)
"""










