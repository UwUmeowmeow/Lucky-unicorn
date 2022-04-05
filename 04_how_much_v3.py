"""Component 2 (how much) v2
use try/accept and pull error message out of the loop
"""

error = "That was not valid input\n"
user_balance = 0

# Keep asking until a valid amount (1.10) is entered
while not 1 <= user_balance <= 10:
    try:
        user_balance = int(input("Please enter a whole number between 1 and 10""\nhow much would you like to play with $"))

        print()

    except ValueError:
        print(error)

print(f"You are playing with ${user_balance}")