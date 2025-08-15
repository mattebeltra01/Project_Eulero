# https://projecteuler.net/problem=9

import time

start = time.time()

a = 1
b = 2
c = 3

for c in range(980):
    for b in range(c):
        for a in range(b):
            if a + b + c == 1000:
                if a*a + b*b == c*c:
                    print(a,b,c)
                    print(a*b*c)

end = time.time()
print(end - start)