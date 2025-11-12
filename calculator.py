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
        raise ZeroDivisionError
    else:
        return b / a

def log(a, b):
    if b <= 0:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b

