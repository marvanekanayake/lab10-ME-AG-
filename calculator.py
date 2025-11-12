# https://github.com/marvanekanayake/lab10-ME-AG-/

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a):
    if a < 0:
        raise ValueError
    else:
        return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a,b)

# First example

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
        return a/b


def log(a, b):
    if a > 0 and b > 0 and a!=1:
        return math.log(b, a) # use math library + raise ValueError
    else:
        raise ValueError

def exp(a, b):
    return a^b







