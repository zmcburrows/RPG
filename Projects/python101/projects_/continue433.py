from page433 import you_get_an_idea
def you_continue():
    next_choice = input('''
    
You continue forward

''')
    if next_choice == "":
        you_get_an_idea()
