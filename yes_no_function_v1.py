"""Yes/No checking function
based on test 3.py
"""


# Function go here...
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


# Main routine go here...
show_instructions = yes_no("Have you played this game before? ")
print(f"You entered '{show_instructions}'")
print()
having_fun = yes_no("Are you having fun? ")
print(f"You entered '{having_fun}'")
