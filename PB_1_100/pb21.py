# https://projecteuler.net/problem=21

import numpy as np

def divisor(n):
    div = [1]
    for i in range(2,n):
        if n % i == 0:
            div.append(i)
    return np.array(div).sum()

sum = 0

for i in range(10000):
    first = divisor(i)
    second = divisor(first)
    if first != i:
        if second == i:
            sum += i
            print(i)

print(sum)
