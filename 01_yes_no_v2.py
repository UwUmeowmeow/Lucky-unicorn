"""LU Yes/ No
Puts The code created in v2 into a loop to make testing easier and more efficient.
"""

show_instructions = ""
while show_instructions != "x":

    # Ask the user if they have played before
    show_instructions = input("Have you played this game before?:").lower()

    # if they say yes, 'out put Continues'
    if show_instructions == "yes" or show_instructions == "y":
        print("program continues")


    # if they say no, 'Display instructions'
    elif show_instructions == "no" or show_instructions == "n":
        print("Display instructions")


    # Otherwise - show error
    else:
        print("please enter 'yes' or 'no'")

    print(f"You entered '{show_instructions}'")
    print("You entered {}".format(show_instructions))
