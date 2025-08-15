# https://projecteuler.net/problem=4

import time

start = time.time()

big = 0

def checkPalindrome(num):
    num = str(num)
    inv = int(num[::-1])
    if inv == int(num):
        return True
    return False


for i in range(100,1000,1):
    for j in range(100,1000,1):
        mult = i * j 
        if checkPalindrome(mult) == True:
            if mult > big:
                big = mult

print(big)


end = time.time()
print(end-start)
        