# Functions

# for i in range(5):
#     print(i)
#     for power in range(1, 4):
#         print(i**power, end = " ")
#     print()

# Functions

# def f(x):
#     y = x**2 + x + 2
#     return y
#
# print(f(4))
# print(f(5))
# print(f(10))
#
#
# def area(l, b): # parameters
#     a = l * b
#     return a
#
# var = area(5, 2) # arguments
# var2 = area(3, 4)
# print(var, var2)
#
# def hello(name): # parameter
#     print("Hello " + name)
#
# print(hello("Anant"))
# hello("Rishi")
# hello("Priya")


def is_prime(num):
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return False
    return True
    
# Python function can have multiple return statements
# print(is_prime(2))

# def dummy(x):
#     print(x)
#     return None
#     print(x**2)
#
# dummy(3)

# def print_primes(lower, upper):
#     for i in range(lower, upper+1):
#         if is_prime(i):
#             print(i)
#
# print_primes(2, 50)



def minimum(a, b):
    if a > b:
        return b
    else:
        return a

def hcf(a, b):
    smaller = minimum(a, b)
    result = 1
    for i in range(1, smaller+1):
        if a % i == 0 and b % i == 0:
            result = i
    return result

print(hcf(12, 11))


# Euclid's Algorithm
def hcf(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a + b
    
# Optimised Eulcid's algorithm
def hcf(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

# 39924 - count the number of digits
def count(num, digit):
    count = 0
    while num > 0:
        d = num % 10
        num = num // 10
        if d == digit:
            count = count + 1
    return count

# log























































