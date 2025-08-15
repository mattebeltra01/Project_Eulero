# https://projecteuler.net/problem=5

def divisibility(num):
    if num % 19 == 0:
        if num % 18 == 0:
            if num % 17 == 0:
                if num % 16 == 0:
                    if num % 15 == 0:
                        if num % 14 == 0:
                            if num % 13 == 0:
                                if num % 12 == 0:
                                    if num % 11 == 0:
                                        return True
    return False

i = 0
check = False
while check == False:
    i += 20
    check = divisibility(i)
    

print(i)