# Lesson 9: Looping with For Loops

# In this lesson, we'll explore for loops, a fundamental concept in programming.
# For loops allow us to repeat a block of code a specific number of times or iterate
# through collections like lists.

# ----LESSON----

# A for loop has a specific structure in Python. It typically consists of three main parts:
# 1. The loop variable: This variable changes with each iteration and controls the loop.
# 2. The iterable: The collection or sequence of items you want to loop through, like a list.
# 3. The loop body: The code block to be executed during each iteration.

# Let's start with a basic for loop to print numbers from 1 to 5.

for number in [1, 2, 3, 4, 5]:
    print(number)

# This loop will iterate through the list [1, 2, 3, 4, 5].
# The loop variable 'number' takes on the values from the list one by one.
# The loop body, which is indented, prints the current value of 'number' during each iteration.

# We can also use a loop to perform a task a specific number of times. For example, let's print "Hello" five times.

for _ in range(5):
    print("Hello")

# My head needs a break from the technical stuff. This is computer science:
# The combination of math, code, logic and philosophy!
# Lets get philosophical

# What if we wanted to embody daytime TV presenter Oprah?
#      .-""""""-.
#    .'          '.
#   /   O      O   \
#  |                |
#  |   \        /   |
#   \   '.____.'   /
#    '.          .'
#      '-......-'
# YOU GET A CAR, AND YOU GET A CAR, AND YOU GET A CAR

#ALL OF THE DOGGIES WANT A TREAT!
dogs = ["biscuit", "stella", "fox"]

# Oops! We forgot gizmo! How do we add him to our dogs?

output = "" #lets use this empty string to YELL FOR EVERY DOG THAT WANTS A TREAT

# the cool thing about strings is that you can add them together like numbers!
# "hello " + "world" = "hello world"

# what should this for loop look like if we want to print out "DOG_NAME WANTS A TREAT" for every dog?

for dog in dogs:
    
print(output) #Make sure output lets us know which of those doggies want a treat!