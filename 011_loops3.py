# We're learning a lot about loops! They're a really important part of programming
# Think about any software you use, you'll be able to figure out where it probably uses loops
# for example a messaging service! If you have a list of current chats for a user
# that's an iterable! you may want to display that list to the user and let them do things with each chat
# for that you would loop!

# There's only a couple more elements to loops I want to cover right now.
# the continue keyword - this keyword is used in a loop when you want to ignore the rest of the code block
# from the point of the usage of "continue" - and just move onto the next iteration (item in the loop)

# the break keyword - this keyword is when you want to stop the loop entirely! if this keyword is hit.
# then we stop executing the loops code block whether or not it's finished its execution expression

# and definining iterables!
# iterable really is any collection of "stuff" - lists are iterable, however, so are strings for example!
# so when I casted to a list in the last program like list("string") - that was a bit inefficient.
# I could have just iterated over the string

#ARGH, A SNAKE WITH ASTHMA! CATCH IT WHEN IT STOPS FOR BREATH
check_for_a = "SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSaSSSSSSSSSSSSSSSSSSSSSSS"

i = 0
for character in check_for_a:
    i += 1
    if character == "a":
        print(f"GOT THE BUGGER, IT TOOK US {i} CHARACTERS")

# It would have taken more S's if our brave dogs didn't steal some for their names
# lets pet any dog with an S!
dogs = ["biscuit", "fox", "stella"]

for dog in dogs:
    if "s" not in dog:
        #what should go here? continue or break?
    print(f"Good work on stealing that S {dog}! *pat pat*")

#DAMN Gizmo escaped, he's always doing that!
dogs = ["stella", "biscuit", "gizmo", "fox"] #we'll redefine the list with the lost dog!

#let's write some code so we can always make sure he's there! this loop can finish once he is found

i = 0;
for dog in dogs:
    i+=1
    if dog == "gizmo":
        #what should go here? continue or break?
print(f"Found Gizmo! The list is {len(dogs)} long but we found him in {i} iterations!")