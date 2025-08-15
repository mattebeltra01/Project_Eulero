# https://projecteuler.net/problem=15

# We can see the path as word composed only of letter D and R respectively for down and right path
# The word is costrain in lenght and also the number of D and R is fixed
# Considering a grid of dimension (n x n) the lenght of the word is 2n we only choose how to position for example the n letters D
# since the letter R will be already choosen so this is given by the binomial coefficient (2n n)

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

grid = 20

n_path = (factorial(2*grid)/(factorial(grid)*factorial(grid)))
print(n_path)