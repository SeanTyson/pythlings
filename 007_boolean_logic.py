# Lesson 7: Boolean doggies!

# In this lesson we'll learn about the boolean type and boolean logic.
# All programming languages including Python have a type called "boolean" which essentially
# just means True or False. infact we write the value like that!

# is_python_awesome = True
# does_programming_suck = False

# There are lots of "comparison operators" we can use in python that evaluate to boolean too!
# Here are some comparison operators 

# == tests for "is equal to"
# != tests for "not equal to"
# >  tests for " is greater than"
# < tests for "is less than"
# >= tests for "greater than or equal to"
# <= tests for "less than or equal to"

# 1 > 2 == True
# 1 < 2 == False
# 1 == 2 == True
# 1 <= 1 == True
# 2 >= 3 == False

# There are special operators we can use to test multiple scenarios! there are "and" and "or"

# and will always return True if BOTH of the conditions are true
# 1 > 2 and 2==2 will return a True
# Whereas 
# 1 < 2 and 2==2 will return a False

# opposingly, or will return True if 1 or both are true
# 1 > 2 or 2==1 returns True
# whereas
# 2 == 1 or 1 == 4 returns False

# The boolean type may not seem useful on its own. Let's learn the power of boolean logic!
# Python has a special syntax to work with booleans. Here is an example

#temperature = 25

#if temperature >= 30:
#    print("It's a hot day!")
#else:
#    print("It's a pleasant day.")

# Output: It's a pleasant day.

# note the structure of this. the if keywork, then a boolean expression, then a colon
# after the initial if line - we need to indent our code. this is now a "block" of code
# the block after the if will run if the if statement is True. (Temperature is greater than or equal to 30)
# otherwise the block after the else: will run!
# Pretty simple :) 

# Lets inspect a part of our previous program
# We'll use hardcoded values for now to make it easy.

# The print statements are a bit of a mess? We could work out who's been good and who's been bad beforehand.
# Let's work out if the dogs have been good! We'll initially say yes but then we'll add more information
# Lets make sure they haven't bitten anyone! I've been keeping track  and written down the values.
# I've also been checking on if they pissed on the floor, I keep track of these things through the window.

is_biscuit_good = True
is_stella_good = True

biscuit_people_bitten = 0
stella_people_bitten = 1

biscuit_floor_pisses = 4
stella_floor_pisses = 3

#Now we will set some acceptable thresholds - every dog makes mistakes.
acceptable_piss_threshold = 3
acceptable_bite_threshold = 2

biscuit_generous_treats = 8
stella_generous_treats = 5

biscuit_conservative_treats = 7
stella_conservative_treats = 4

# Set the acceptable thresholds
acceptable_piss_threshold = 3
acceptable_bite_threshold = 2

# Check if Biscuit has been good based on biting and pissing thresholds

#replace the ??? in the rest of this program with the variables you think fit!

#note: you can use boolean logic to set variables like this in one line! without the if statements!
is_biscuit_good = (??? <= acceptable_bite_threshold) and (??? <= acceptable_piss_threshold)

# Check if Stella has been good based on biting and pissing thresholds
is_stella_good = (??? <= acceptable_bite_threshold) and (??? <= acceptable_piss_threshold)

if is_biscuit_good:
    print(f"Biscuit gets {???} treats - which is the generous value because she's been good!")
else:
    print(f"Biscuit gets {???} treats - which is the conservative value because she's been bad!")

if ???:
    print(f"Stella gets {stella_generous_treats} treats - which is the generous value because she's been good!")
else:
    print(f"Stella gets {stella_conservative_treats} treats - which is the conservative value because she's been bad!")

# if doesn't have to have an else! The program will just keep running and
#  not do anything based on the ifs if it isnt true

if is_stella_good and ???:
    print("Both dogs were good!")

print("End of program... beep beep")