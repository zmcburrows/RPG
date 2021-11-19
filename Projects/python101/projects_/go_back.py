from page433 import you_get_an_idea
def you_dont_know():
    next_choice = input('''

You don’t know which direction is back, but you take a guess and continue.

''')
    if next_choice == "":
        you_get_an_idea()