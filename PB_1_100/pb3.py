# https://projecteuler.net/problem=3
import math

n = 600851475143

prime_list = []
max = int(math.sqrt(n) + 1)

def primeCheck(num):
    
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    i = 5
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

for i in range(max):
    if primeCheck(i) == True:
        prime_list.append(i)

divisor = 0
for i in prime_list:
    if n % i == 0:
        divisor = i

print(divisor)