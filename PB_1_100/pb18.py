# https://projecteuler.net/problem=18

def create_pyramid(val):
    pyramid = []
    i = 0
    row = 1 #lenght row

    while i < len(val):
        pyramid.append(val[i:i+row])
        i += row
        row += 1
    return pyramid

num = [3,7,4,2,4,6,8,5,9,3]

pir = create_pyramid(num)

sums = []
somma = 0

for i in range(len(pir)):
    somma += pir[i,0]


