# https://projecteuler.net/problem=6

n = 100

sum_sq = 0
for i in range(n+1):
    sum_sq += i

sum_sq = sum_sq**2

sum_of_sq = 0
for i in range(n+1):
    sum_of_sq += (i*i)

print(sum_sq - sum_of_sq)