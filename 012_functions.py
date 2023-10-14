import math
import random #ooh a new import statement! Remember we learnt about modules?

# In this lesson we're gonna talk about functions
# We've been using functions this whole time!
# print() len() int() ceil() floor() - etc etc. they're all functions!
# some functions take arguments like
print("hello!")
# some functions return things like ceil 
three = math.ceil(2.9)
print(three)

# Functions are useful because they allow us to do things we might need to do LOADS
# for example from the random module.

# We could write code to introduce a bit of random choice ourselves easy!
# but if we use it a lot we could end up repeating ourselves which is a snoozefest
# worse! if we ever wanna change the way random choices work we would have to change it more than once!
# solution, use the choice function from the random module.

my_list = [1, 2, 3, 4, 5]
random_item = random.choice(my_list)
print(random_item)

# But we aren't stuck to using the standard library or other peopels functions! We can MAKE THEM
# and it's super easy! We only need to use the def keyword (define)
# then name it def function_name
# then say what parameters it will take def function_name(params):
# then after the colon, indent so we give it a code block to run whenever it is called!
# that function now has access to the arguments it will eventually be sent.
# we can take as many arguments as we want, no one can stop us!

def return_woofs(doggy):
    woofs = 1 # all dogs have at least one woof.

     # OOP! In this block is the first time we've seen the elif keyword.
     # don't panic it just means "else if" - we can chain our if statements with more ifs
     # when the if isn't true, it'll check the next elif if there is one, then the else if there is one
     # you can use as many elifs as you like, they'll just cascade until one is true or none are!

    if doggy == "Biscuit":
        woofs += 2
    elif doggy == "Stella":
        woofs += 3 # We all know Stella has more woofs!
    return woofs # we use the return keyword to give back the value to whatever "called" this function
 
# woops, i've forgotten something while trying to make the print_woofs function!
# what is missing? it's also missing two arguments that the code block tries to use?
# give print_woofs its arguments back based on what we're trying to use in the function body!

print_woofs(???, ???):
    print(f" {woofs} {mood} woofs") 

dogs = ["Stella", "Biscuit", "Fox"]
actions = ['poke', 'pet', "dance with"]


# have a look at this code, it doesn't need fixing once you've sorted the function out
# but working out what it does and how will be an interesting insight into how programs are wrote
# it might just be silly but this is a real program still! it's almost like a random little adventure game
# an adventure game the program plays for you without input... but we can maybe improve that sometime!

for dog in dogs:
    doggies_woofage = return_woofs(dog)
    random_action = random.choice(actions)
    reaction = "happy" #set initial mood of dogs

    if random_action == "poke":
        reaction = "annoyed"
    elif random_action == "dance with":
        reaction = "confused"
    print(f"you randomly {random_action} {dog}, lets see how they react:")

    # we're telling how print_woofs how many woofs that dog likes to do and their current reaction
    # to your randomness, in the function we call reaction "mood" - you don't have to persist names
    # functions get their own copy of variable values to work with that they can rename

    print_woofs(doggies_woofage, reaction)