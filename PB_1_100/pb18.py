# https://projecteuler.net/problem=18

import numpy as np
import itertools

def create_pyramid(val):
    pyramid = []
    i = 0
    row = 1 #lenght row 

    while i < len(val):
        pyramid.append(val[i:i+row])
        i += row
        row += 1 # the lenght row increase by one each time to create the pyramid
    return pyramid

num = [75, 95, 64, 17, 47, 82, 18, 35, 87, 10, 20, 4,
        82, 47, 65, 19, 1, 23, 75, 3, 34, 88, 2, 77, 73,
        7, 63, 67, 99, 65, 4, 28, 6, 16, 70, 92, 41, 41, 
        26, 56, 83, 40, 80, 70, 33, 41, 48, 72, 33, 47, 
        32, 37, 16, 94, 29, 53, 71, 44, 65, 25, 43, 91, 
        52, 97, 51, 14, 70, 11, 33, 28, 77, 73, 17, 78, 
        39, 68, 17, 57, 91, 71, 52, 38, 17, 14, 91, 43, 
        58, 50, 27, 29, 48, 63, 66, 4, 68, 89, 53, 67, 
        30, 73, 16, 69, 87, 40, 31, 4, 62, 98, 27, 23, 
        9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

pir = create_pyramid(num)

# I have to create all the possibile path considering 0 going left and 1 going right with the first number is 0 fixed
def binary_comb(n):
    tail = list(itertools.product((0,1), repeat=n-1))
    return [(0, *t) for t in tail]

paths = binary_comb(len(pir))

j = 0
sums = []

for path in paths:
    sum = 0
    j = 0
    for i in range(len(pir)):
        if path[i] == 1:
            j += 1
        sum += pir[i][j]
    sums.append(sum)

print(max(sums))






