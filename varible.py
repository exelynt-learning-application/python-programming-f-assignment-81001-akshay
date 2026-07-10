# Student Profile Program

# Store student details
student_name = "Akshay"
age = 22
course_fee = 15000.50
is_enrolled = True

# Display student details
print("----- Student Details -----")
print("Student Name:", student_name)
print("Age:", age)
print("Course Fee:", course_fee)
print("Enrolled:", is_enrolled)

# Display data types
print("\n----- Data Types -----")
print("Student Name:", type(student_name))
print("Age:", type(age))
print("Course Fee:", type(course_fee))
print("Enrolled:", type(is_enrolled))

# Perform operations
age = age + 1                 # Increment age
course_fee = course_fee + 1000.00   # Add tax
is_enrolled = False           # Change enrollment status

# Display updated details
print("\n----- Updated Student Details -----")
print("Student Name:", student_name)
print("Age:", age)
print("Course Fee:", course_fee)
print("Enrolled:", is_enrolled)

# Display updated data types
print("\n----- Updated Data Types -----")
print("Student Name:", type(student_name))
print("Age:", type(age))
print("Course Fee:", type(course_fee))
print("Enrolled:", type(is_enrolled))
