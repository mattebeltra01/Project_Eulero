# https://projecteuler.net/problem=12

# The number of divisor of a number n appear only as couple of d and n/d so we need to count twice up to sqrt(n) 
# and then remove to perfect square

import math

div = 0
count = 1
tri = 0

while div < 500:
    div = 0
    tri = 0

    for i in range(count + 1):
        tri += i
    
    for i in range(1,int(math.sqrt(tri)) + 1):
        if tri % i == 0:
            div += 2
        if i*i == tri:
            div -= 1

    count += 1

print(tri)
print(count-1)

