# https://projecteuler.net/problem=7

prime_list = [2]

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

i = 3
while len(prime_list) < 10001:
    if primeCheck(i) == True:
        prime_list.append(i)

    i += 2

print(prime_list[-1])