# https://projecteuler.net/problem=16

n = 2**1000
n = str(n)
print(n)

sum = 0
for i in range(len(n)):
    sum += int(n[i])

print(sum)