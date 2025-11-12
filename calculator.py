# https://github.com/MrJoethBobeth/lab10-LM-NL
# Partner 1: Luis Malave Matias
# Partner 2: Nathan Lohnes

import math

def square_root(a):
    if a < 0:
        raise ValueError
    else:
        return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero (a cannot be 0).")
    return b / a

def logarithm(a, b):
    if b <= 0 or a <= 0 or a == 1:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b

