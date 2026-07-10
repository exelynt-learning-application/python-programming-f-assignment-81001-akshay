# my_first_program.py

# My First Python Program

# Ask the user to enter their details
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
favorite_number = float(input("Enter your favorite number: "))

# Display the user's details
print("\n----- User Details -----")
print("Name:", name)
print("Age:", age)
print("Height:", height, "meters")
print("Favorite Number:", favorite_number)

# Display the data type of each variable
print("\n----- Data Types -----")
print("Name:", type(name))
print("Age:", type(age))
print("Height:", type(height))
print("Favorite Number:", type(favorite_number))

# Perform an arithmetic operation
total = age + favorite_number

# Display the result
print("\n----- Arithmetic Operation -----")
print("Age + Favorite Number =", total)
print("The total of your age and favorite number is:", total)

# End of the program
print("\nProgram executed successfully!")
