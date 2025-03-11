# src/calculations_Processor.py

import math
from Basic_Operations import add, subtract, multiply, divide

# Define allowed functions for safe evaluation
allowed_functions = {
    "sin": math.sin, "cos": math.cos, "tan": math.tan, "log": math.log,
    "sqrt": math.sqrt, "pi": math.pi, "e": math.e,
    "add": add, "subtract": subtract, "multiply": multiply, "divide": divide
}

def calculate(expression):
    try:
        expression = expression.replace("pi", "math.pi").replace("e", "math.e")
        expression = expression.replace("x^2", "**2").replace("1/x", "1/")
        expression = expression.replace("x", "*")  # Ensure multiplication is handled

        # Evaluate using safe functions
        return eval(expression, {"__builtins__": None}, allowed_functions)
    except Exception:
        return "Error"

if __name__ == "__main__":
    while True:
        user_input = input("Enter calculation (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        print("Result:", calculate(user_input))