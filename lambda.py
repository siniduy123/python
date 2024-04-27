# basic structure
def adderFunc(x, y):
    return x + y
# func = lambda arg: expression
# func(arg)

# multiple args and single expression
adder = lambda x, y: x + y

print(adder(4, 5))

# example
isPalindrome = lambda s: str(s) == str(s)[::-1]

print(isPalindrome(1121))

# usage inside another function
def func(superscript):
    return lambda base: pow(base, superscript)

sqr = func(2) # lambda num: pow(num, 2)
cub = func(3)

print(sqr(3), cub(3))