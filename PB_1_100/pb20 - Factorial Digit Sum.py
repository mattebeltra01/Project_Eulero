# https://projecteuler.net/problem=20

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

num = fact(100)
num = str(num)
sum = 0

for i in range(len(num)):
    sum += int(num[i])

print(sum)