# syntax_structure.py

# Program title
print("=== Basic Python Structure Demonstration ===")

# Top-level print statements
print("Welcome to the Python program.")
print("This program demonstrates Python syntax and indentation.")
print("Let's begin!")

number = 10

# Code block starts here
# Indentation is required in Python to define which statements belong to the if block.
if number > 5:
    print("The number is greater than 5.")

    # Nested code block starts here
    if number == 10:
        print("The number is exactly 10.")
    # Nested code block ends here

    print("End of the outer if block.")
# Code block ends here

print("Program executed successfully.")
