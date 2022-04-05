"""Component 2 (how much) v2
use try/accept and pull error message out of the loop
"""

error = "Please enter a whole number between 1 and 10\n"
valid = False

# Keep asking until a valid amount (1.10) is entered
while not valid:
    try:
        user_balance = int(input("How much would you like to play with? $"))

        if 0 < user_balance <= 10:
            print(f"You are playing with ${user_balance}")
        else:
            print(error)
    except ValueError:
        print(error)


