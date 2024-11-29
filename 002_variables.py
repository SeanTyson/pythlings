# Welcome to the Dog Playdate Program!
# In this program, we're going to learn about variables, printing, and sharing toys between dogs.

# First, let's introduce our two dogs, Biscuit and Stella, and their toys.



biscuit_toys = 5  # Biscuit starts with 5 toys
stella_toys = 4   # Stella starts with 4 toys

# We'll use the `print()` function to display information. Don't worry about functions yet
# For now all you need to know is that using print() like this will output text to the terminal.
# Here, we're showing how many toys each dog has before sharing.
print(f"Stella and Biscuit are going on a playdate. Biscuit has {biscuit_toys} toys and Stella has {stella_toys} toys.")

# Now, let's have the dogs share one toy.
biscuit_toys -= 1  # Biscuit gives one toy to Stella
stella_toys += 1  # Stella receives one toy from Biscuit

# After sharing, let's print how many toys each dog has.
print(f"After sharing, Biscuit now has {biscuit_toys} toys and Stella has {stella_toys} toys.")

# ---------- Your Task ----------
# The dogs didn't quite end up with an equal number of toys. Can you modify the program to ensure that
# Biscuit and Stella have the same number of toys after sharing? You can do this however you like.