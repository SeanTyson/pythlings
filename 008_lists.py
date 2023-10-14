# In this lesson, we will explore lists, a versatile and widely-used data structure in Python.
# Lists allow you to store collections of items, such as numbers, strings, or even other lists.
# They are flexible and powerful, making them essential in many programming scenarios.

# ----LESSON----

# A list is defined by placing a comma-separated sequence of items inside square brackets [].
# For example, here's a list of numbers:
numbers = [1, 2, 3, 4, 5]

# And here's a list of our dogs! We've got 2 more!:
dogs = ["biscuit", "stella", "fox", "gizmo"]

# You can even have a list of mixed data types:
mixed_list = [42, "apple", 3.14, True]

# To access an item in a list, use its index with the syntax list[index]. Python uses 0-based indexing.
# This means the first item is at index 0, the second at index 1, and so on.
print(f"The first item in 'dogs' list is {dogs[0]}")

# Remember that every type (yes, List is a type!) has functions that can be performed on it in python
# like len() which can actually be used on lots of types but in this case will get the len(gth) of the list!
# why not try printing out the length of the mixed list?
# do you remember how to give functions their arguments?

# write it here.

# other functions that can be performed on lists can ONLY be performed on lists.
# they BELONG to the list type.
# they are called with a dot at the end of the list and THEN the function.

numbers.append(6)

# lists can even be printed! the interpreter will work out you're trying to use it as a string
print(numbers)

# There are LOADS of other functions to be used on lists. list.sort() list.reverse()
# Learning a programming language isn't about learning all of its functions
# It's about learning its basic structure, rules and types then thinking about how to solve a problem!
print(len(numbers))