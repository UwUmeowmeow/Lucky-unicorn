# Ask the user if they have played before
show_instructions = input("Have you played this game before?:")

# if they say yes, 'out put Continues'
if show_instructions == "yes":
    print("program continues")


# if they say no, 'Display instructions'
elif show_instructions == "no":
    print("Display instructions")


# Otherwise - show error
else:
    print("please enter 'yes' or 'no'")




