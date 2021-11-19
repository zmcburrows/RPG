from continue_1 import continue_2
from go_home import go_home1

def into_the_house():
    while(True):
        print('''
                        
        You are back.
                        
        ''')
        date = input("The timestamp on the camera reads ‘April 1, 1991’. You point the camera towards your supplies(type supplies to see list, press enter to bypass) ")
        if date == "supplies":
                print('''
                - 1963 H16 hand crank Bolex 16mm camera -rated sleeping bag
                    -16mm, 25mm, and 75mm Kern
                    -Paillard lenses		        -one man tent
                -Bogen tripod						-rations for two weeks
                -Sony microcassette recorder		-2 five gallon containers of water
                -Panasonic Hi 8						-chemical heat packs
                -batteries							-flares
                -a dozen or more 120 minute Metal Evaporated (DLC) tapes   -fishing line
                -35mm Nikon					         -high intensity and regular intensity lightsticks
                    -flashes				           -plenty of neon markers
                    -USA Bobby Lee camera straps	-three flashlights
                -3000 feet of 7298 16mm Kodak (in 100 ft loads)	-one small pumper light
                -20 rolls of 35mm 				        -extra batteries
                -some 36 frame Konica 3200 speed		-carbide lamp
                -10 rolls of assorted black and white film	-matches
                -thermal video camera (you mentally scratched this off, it fell through last minute)
                                        -toothbrush
                                        -stove
                                        -change of clothes
                                        -extra sweater
                                        -extra socks
                                        -toilet paper
                                        -small medical kit
                                        -one book
        ''')
        elif date == "":
                input("You loaded all of this onto a trailer hooked up to a mountain bike" )

                print("You are back" )

                start = input("The next shot you get from the camera you hooked up to the bike is of you are inside,  bypassing the Spiral Staircase. You aren’t going back down there." )
                if start == "":

                    continue1 = input("Instead you head down one of the corridors in Great Hall" )
                    if continue1 == "": 

                        print('''
The weight of your supplies limits your mobility, so you bike along slowly
                    ''')

                        print('''
"I am in no hurry" you note to the cassette player
                    ''')

                        print('''
You stop every once and a while to get stills and shots. After two hours, you have only managed to go 7 miles, so says the numbers written on the screen of the odometer.
                        ''')
                        print('''

You stop for a moment to take a drink of water and lay out a neon marker. As you start pedaling, you notice something and remark “It seems to be getting easier.”

Soon, there is less resistance when you pedal. The hallway is sloping downward. After a while, all you need to do is brake.

When you finally stop, your odometer reads 163 miles.

As you set up camp in a small room, you know you need to make a decision when you wake up: turn back and go home or continue down 
                        ''')
                        choice_1 = input('''
Go home or continue 

''')
                        if choice_1 == "go home":
                            go_home1()
                            break      
                        elif choice_1 == "continue":
                            continue_2()
                            break
                        else: 
                            break   
                    else:
                        break
                else:
                    break                         
        else:
            break



