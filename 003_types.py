# Problem 3: Dog Ages and Treats

# Biscuit and Stella have had a wonderful playdate, and now they are celebrating Stellas birthday together
# It's time to calculate stellas age in "dog years" and figure out how many treats she should receive.

# ----LESSON----

# Python (and most other languages) have a concept called "Types" which is basically what is says on the tin.
# Types are ...well, types a value can have. So far we've used numbers and letters
# numbers are split into different types, we've used "integers" so far
# collections of letters are called "strings" - they're just a string of different characters.
# it's important to note strings can include numbers or be wholly numbers. if we use "" quotes - it's a string.

# - Integers (e.g., 42)
# - Floats (e.g., 3.1416)
# - Strings (e.g., "Hello, World!")

# One other type numbers can have is "float" (floating point numbers)- e.g. pi to 4 places! (3.1416)
# some types can work with each other in specific ways. for example you can add an integer to a float
# you can't add a string to a number that wouldn't make sense!

# Oh no!! We're trying to work out how many treats our doggies get but the program is broken.
# Try running the program and looking at the error - pay special attention to the "line number"
# Fix it so our doggies can get their delicious treats!

# Let's set up the variables:
biscuit_age = 1  # Biscuit's age in human years
stella_age = 0.5   # Stella's age in human years
dog_years_factor = "3" #lets keep the factor simple for now

# Calculate Biscuit and Stella's ages in dog years.
biscuit_dog_years = biscuit_age * dog_years_factor
stella_dog_years = stella_age * dog_years_factor

# Calculate regular treats: two treat for each dog year they've lived.
biscuit_treats = biscuit_dog_years * 2
stella_treats = stella_dog_years * 2

# Stella gets a special birthday treat on her birthday.

# Try changing this and running the program again. What do you think will happen?
# If what you expect doesn't happen - try figuring out why and fixing it!
stella_birthday_treats = "Bone" 

# Let's celebrate!
# quick note: you can use the special character \n in strings to mean newline! so our terminal isn't messy
# For long statements you can also make your editor less messy by terminating the string on the first line
# using " and starting the string again on the second with "

print(f"It's Stella's birthday! \n Biscuit is {biscuit_age} years old in human years,"
      f" which is {biscuit_dog_years} in dog years. She'll get {biscuit_treats} regular treats.")

print(f"Stella is {stella_age} years old in human years,which is {stella_dog_years}"
       f"in dog years. She'll get {stella_treats} regular treats and a special Bone treat")