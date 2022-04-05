"""Component 2 (how much) v2
use try/accept and pull error message out of the loop
"""


def num_check(question, low, high):
    error = "That was not valid input\n" \
            "Please enter a number between {} and {}\n".format(low, high)

    while True:
        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main routine
user_balance = num_check("How much would you like to play with?$", 1, 10)
print(f"You are playing with ${user_balance}")


