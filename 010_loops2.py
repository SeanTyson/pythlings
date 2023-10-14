
# This lesson will introduce you to a different kind of loop!
# The new guy in town is the "while" loop - The for loop takes a nice and lovely set range or iterable
# but the WHILE loop executes it's codeblock POTENTIALLY FOR INFINITY
# The way the while loop works is it takes an expression and it will just execute as long as it's True!

# while True:
#   print("INFINITY IS A LONG TIME")

# THIS IS PERFECTLY VALID SYNTAX. uncomment it if you don't believe me
# but if you do - ctrl+c is how you can get the terminal to stop executing your program

# run_once = False
# while run_once == False:
#   run_once = True

# ^ that's much more sensible! If a bit useles... 

# OH NO! We forgot about our dogs screaming for treats!
dogs = ["biscuit", "stella", "fox", "gizmo"]

# Fortunately the council of digital dog handlers (CDDH) has been keeping track of who's been the goodest
# and therefore how many treats each dog gets!

treats = "3524"

# Damn... the CDDH needs to stat watching who they hire. We can't get each dog 3524 treats!!
# I think they were supposed to create a list of 3, 5, 2 and 4.
# we COULD just change the above to a list or make a new list but what if they mess up again?
# Incase they just give that variable name a string in future we should create a new list based upon it
# Luckily I know a trick! 

# List of treats for each dog (in the same order):
treats = list(treats) #casting to list with the list constructor will gives us ["3", "5", "2", "4"]!

# Now all we need to do is print out which dog gets how many treats! replace the ??? to make it work
# note: we can access the value at a particular position in a list with its position index remember?
# it also works with a variable - always keep in mind variables are just names for values :)
 
i = 0
while ??? < len(dogs):
    print(f"{dogs[i]} gets {???} treats!")
    i += 1

# Once the program is fixed, it should print out each dog's name and the number of treats they receive.
# Good luck, and have fun fixing the program!