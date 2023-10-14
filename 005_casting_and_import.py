# Problem 5: Dog Treat Dilemma cleanup

import math #I'll explain this a bit lower down!



# You'll notice that this file is ALMOST exactly the same as the last file
# If you're eagle-eyed you'll have spotted a few problems with our last attempt:
# 1) the round function wont give us generous treats if the result of dog year * treats for years is a number
# with a decimal place lower than the midpoint because round will round down in that case.
# 2) the output is weird. the good girls get an integer of treats and the bad get a float! weird.

# let's have a couple of lessons then we can tidy some stuff up with a few changes.

# ----LESSON - IMPORTS ----

# In Python, we have a large range of features in what is called the "standard library"
# This includes the functions and syntax we've been using so far (like print() and round() )
# However it also includes 'modules' that are installed but not included in
# our programs unless we need them
# There is a LARGE amount of extra modules in the standard library of python.
# as you write more programs you'll get used to more and maybe even intall some third party ones!

# You can import standard library modules by using "import module_name"
# Just like we've done import math above!
# Now we can use functions in imported modules by doing module.function()

# Two useful functions in the math module are ceil() and floor() which perform operations on floats.
# ceil(3.1) will give us 4.0 and floor(2.1) will give us 3.0! (ceiling and floor!)
# However you may notice that it takes floats but also returns floats.

# ----LESSON - CASTING ----

# Another handy function in the standard library is int() - these take anything that could be an int
# e.g. int(3.0) is 3 (float to int) and int("3") is 3 (string to int)
# I've used ceil to tidy the generous treats and int to cast them from floats so they look prettier


# ---- TASK ----
#Can you use my math and casting code plus the lessons to work out how to get prettier conservative treats?

biscuit_dog_years = 5.3
stella_dog_years = 2.8

treats_for_years_lived = 2


# Pay particular attention to how i've used two functions in one line.
# Functions will always operate inside out which means they can take calculations or results from functions
# The bit inside the brackets are called the functions "arguments"
# Here math.ceil() takes the calculation as an argument
# int() takes the result of the math.ceil as its argument! Pretty cool.

biscuit_generous_treats = int(math.ceil(biscuit_dog_years * treats_for_years_lived))
stella_generous_treats = int(math.ceil((stella_dog_years * treats_for_years_lived)))

# Calculate the treats for the conservative scenario:
# Hint - you may have to alter these two lines!
biscuit_conservative_treats = biscuit_dog_years * 2 // 1
stella_conservative_treats = stella_dog_years * 2  // 1


# Display the treat amounts based on behavior.
# You see how you don't need the preceding f for a string that doesn't use a variable? f means format!

print("Let's reward Biscuit and Stella:") 

print(f"If Biscuit has been a good girl she will get {biscuit_generous_treats} treats!")
print(f"If Biscuit has been a bad girl she will get {biscuit_conservative_treats} treats >:(")

print(f"If Stella has been a good girl she will get {stella_generous_treats} treats!")
print(f"If Stella has been a bad girl she will get {stella_conservative_treats} treats >:(")