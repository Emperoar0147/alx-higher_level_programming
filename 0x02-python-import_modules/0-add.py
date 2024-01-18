#!/usr/bin/python3
# Import the add function from add_0.py
from add_0 import add

# Assign the values to variables a and b
a = 1
b = 2

# Check if the script is the main program and not an imported module
if __name__ == "__main__":
    # Call the add function with a and b and print the result
    result = add(a, b)
    print(f"{a} + {b} = {result}\n")
