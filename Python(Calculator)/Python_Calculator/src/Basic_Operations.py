# basic_operations.py

import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    return "Error: Division by zero"

def inverse(x):
    if x != 0:
        return 1 / x
    return "Error: Cannot divide by zero"

def square(x):
    return x ** 2

def sqrt(x):
    if x >= 0:
        return math.sqrt(x)
    return "Error: Negative square root"
