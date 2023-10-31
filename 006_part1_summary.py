# Lesson 6: Python Basics Recap and Type Handling

# In the previous lessons, we've covered some fundamental programming concepts. 
# Now, let's revisit these topics and dive into the concept of type handling.

# 1. Variables and Printing
# Variables allow us to store and manipulate data.
# Printing is a way to display information to the user.

greeting = "Hello"  # Defining a variable called greeting
print(f"{greeting} World")  # Printing a greeting message

# 2. Arithmetic and Variables
# We can use variables in mathematical operations.
# Arithmetic operations include addition (+), subtraction (-), multiplication (*), and division (/).
# There are more we'll get more used to like ** or %
# - ** is for raising the first int to the power of the second e.g. 2**3 = 8
# - % (the modulo operator) is for getting the remainder of a divide 2 % 2 = 0 because 2 is divisible by 2 and has no remainder!

num1 = 10
num2 = 5
result = num1 + num2  # Adding two numbers
print(result)  # Printing the result

# 3. Types in Python
# Python has various data types, including integers, floats, and strings.
# Type inference means Python determines the data type based on the value assigned.

integer_number = 42  # An integer
floating_point_number = 3.1416  # A float
text = "Hello, World!"  # A string

# 4. Type Coercion and Type Errors
# Python allows some degree of type coercion, converting data to a compatible type.
# However, not all type conversions are valid, leading to type errors.

# --- NOTES ON PYTHON ---
# Interpreted Language
# Python is an interpreted language. It is not compiled into machine code 
# but executed directly by the Python interpreter.
# python interpreter is like the god of python - it decides what is valid syntax and runs our programs
# it also gives us errors when we get stuff wrong!

# Python is a dynamically-typed language, which means types are assigned automatically.
# Type coercion allows some flexibility, but it's essential to be mindful of type errors.
# We can explicitly cast types using functions like int(), float(), and str().

# There are alternatives to dynamic typing but this is what Python uses.
# Some languages require use to explicitly define what types our variables are and some go further
# meaning that they require us to never change types.
# You should have noticed by now that Python will interpret the type as it goes along and we change it at will
# this does NOT mean we can perform functions or operations on types that aren't valid though.
# print(int("Hello")) - is NOT valid.
print (int("50")) # is valid. The interpreter can work out 42 is allowed to be an int.


example1 = "42"  # A string
example2 = 7  # An integer

# Uncomment the following line to see a type error:
# result = example1 + example2

# Fix the above error by using type conversion, for instance:
# result = int(example1) + example2


# 6. Type Casting
# We can explicitly change the type of data through casting functions.
# Examples of casting functions include int(), float(), and str().


age = 28.5  # A float
age_as_integer = int(age)  # Casting to an integer

# 7. Broken Examples
# Below are some broken examples. Can you identify the type errors and fix them?

# Example A:
# result1 = 42 / "7"  # Uncomment this line to see a type error

# Example B:
# result2 = "Hello" + 42  # Uncomment this line to see a type error

# Example C:
# result3 = str(7) - "3"  # Uncomment this line to see a type error

# Your task is to fix these errors using type conversion and make the code valid.

# Experiment with these concepts and fix the broken examples to gain a deeper understanding of Python's type handling.
