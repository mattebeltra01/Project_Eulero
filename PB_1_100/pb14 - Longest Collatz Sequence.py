# https://projecteuler.net/problem=14

big = 0
big_num = 0
seq = []

for i in range(2,1000000):
    seq = []
    n = i
    while n != 1:
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        seq.append(n)
        if len(seq) > big:
            big = len(seq)
            big_num = i

print(big, big_num)
