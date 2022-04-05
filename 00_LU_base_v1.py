"""LU base component
Components added after they have been created and Tested"""


# Yes/no checking function
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # if they say yes, 'out put Continues'
        if answer == "yes" or answer == "y":
            answer = "yes"
            return answer

        # if they say no, 'Display instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("please enter 'yes' or 'no'")


# Functions to display instructions
def instructions():
    print("**** How to play *****")
    print()
    print("The rules of the game will go here")
    print()



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


# Main routine go here...
plated_before = yes_no("Have you played this game before? ")

if plated_before == "No":
    instructions()

# Ask the number how much to play with
user_balance = num_check("How much would you like to play with?$", 1, 10)
print(f"You are playing with ${user_balance}")
