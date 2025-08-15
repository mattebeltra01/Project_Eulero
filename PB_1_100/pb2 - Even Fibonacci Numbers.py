# https://projecteuler.net/problem=2

sum = 0

last = 0
fibonacci = 1

temp = 0

while fibonacci < 4000000:
    if fibonacci % 2 == 0:
        sum += fibonacci
    
    temp = fibonacci
    fibonacci = fibonacci + last
    last = temp

print(sum)