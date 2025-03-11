# advanced_operations.py

import math

def sin(x):
    return math.sin(math.radians(x))  # Convert to radians if needed

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def log(x, base=10):
    if x > 0:
        return math.log(x, base)
    return "Error: Log of non-positive number"

def factorial(x):
    if x >= 0 and x == int(x):
        return math.factorial(int(x))
    return "Error: Factorial of negative or non-integer number"
