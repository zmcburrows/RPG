from page_424 import into_the_house
from navidson_character import character_information



# House of leaves pages 424-489
#Navidson entering the hallway for the last time
#have to be different choices no matter which way the story goes
#like when he continues down the hall, give the option to stop or to keep going
#theres no getting out if he goes back
#if he goes back, he can either just keep going forever(purposeful infinite loop??)
#or he starves
#if he stays there he will get eaten

#I could either only do the Navidson part or I can add a Johnny part(I don't know which part would work)

#funny endings??


def exploration5():
    while (True):
        menu = input('''
        
        Type yes to start this section of the film. 
        
        Type no to move on

        ''')
        if menu == "yes":
            start = input('''

        Exploration #5
    
        Part 15/16 of the Navidson Record

        Do you want to learn about your character?

        ''')

            if start == "yes":
                character_information()
            elif start == "no":
                real_start = input("Starting Exploration #5")
                if real_start == "":
                    into_the_house()
                    break
            else:
                break
        elif menu == "no":
                johnny_boy = input('''

            Do you want to stop reading, Johnny? 
            
            ''')
                if johnny_boy == "yes":
                    print('''
            You close the book

            ''')
                break
        else:
            break
exploration5()
