# Problem 4: Dog Treat Dilemma

# Note: we're "hardcoding" our previous values here rather than using results from the last problem
# Maybe later we'll learn how to make this a bit more dynamic.

biscuit_dog_years = 5.3
stella_dog_years = 2.8

treats_for_years_lived = 2

# After Biscuit and Stella's wonderful birthday celebration, we've tried to reward them with treats
# but oh no! in the last problem we ended up with fractions of treats
# We have to make sure they get whole treats.

# ----LESSON----

# In Python, you can perform various mathematical operations on numbers, including integers and floats.
# Some common operations include addition (+), subtraction (-), multiplication (*), and division (/).
# You've used some of these already!

# When performing division, you can get a float result even if you divide two integers.
# For example, 5 / 2 would result in 2.5.

# You can use the "//" operator to perform floor division, which always rounds down to the nearest integer.
# For example, 5 // 2 would result in 2, not 2.5.

# When you need to round to the nearest integer, you can use the "round()" function
# Note that if a float is half way between e.g. 1.5 - round is generous and will result in 2!

# ----TASK----
# We're trying to calculate two values for the doggies.
# We'll give them the rounded up number if they're good and the rounded down number if they're bad
# Run the program, oh no! it seems our rounding up is implemented but not the rounding down
# what mathematical operation should you use to round the conservative number of treats to the lowest integer
# This one might be trickier - ask if you need to!


# Calculate regular treats: one treat for each dog year they've lived.

# Calculate the treats for the generous scenario:
biscuit_generous_treats = round(biscuit_dog_years * treats_for_years_lived)
stella_generous_treats = round(stella_dog_years * treats_for_years_lived)

# Calculate the treats for the conservative scenario:
# Hint - you may have to alter these two lines!
biscuit_conservative_treats = biscuit_dog_years * 2
stella_conservative_treats = stella_dog_years * 2 


# Display the treat amounts based on behavior.
# You see how you don't need the preceding f for a string that doesn't use a variable? f means format!

print("Let's reward Biscuit and Stella:") 

print(f"If Biscuit has been a good girl she will get {biscuit_generous_treats} treats!")
print(f"If Biscuit has been a bad girl she will get {biscuit_conservative_treats} treats >:(")

print(f"If Stella has been a good girl she will get {stella_generous_treats} treats!")
print(f"If Stella has been a bad girl she will get {stella_conservative_treats} treats >:(")