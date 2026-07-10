# Type Conversion Practice Program

# Get input from the user
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Convert input to integer and float
int_num1 = int(num1)
float_num2 = float(num2)

# Perform arithmetic operations
print("\n----- Arithmetic Operations -----")
print("Addition:", int_num1 + float_num2)
print("Subtraction:", int_num1 - float_num2)
print("Multiplication:", int_num1 * float_num2)
print("Division:", int_num1 / float_num2)

# Convert numeric value to string
string_value = str(int_num1)

print("\nNumeric value converted to string:")
print("The string value is:", string_value)

# Display data types
print("\n----- Data Types -----")
print("Type of int_num1:", type(int_num1))
print("Type of float_num2:", type(float_num2))
print("Type of string_value:", type(string_value))
