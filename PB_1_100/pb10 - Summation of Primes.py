# https://projecteuler.net/problem=10

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

sum = 2
i = 3

while i < 2000000:
    if primeCheck(i) == True:
        sum += i
    i += 2

print(sum)