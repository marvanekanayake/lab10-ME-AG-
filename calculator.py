"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError()
    return b / a

def log(a, b):
    if a > 0 and b > 0 and a!=1:
        math.log(b, a)# use math library + raise ValueError
    else:
        raise ValueError

def exp(a, b):
    return a^b







