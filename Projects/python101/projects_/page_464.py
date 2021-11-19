from read import you_occupy
from wait import cover_to_cover

def this_isnt_unexpected():
    print('''
    
“Well this isn’t unexpected." you chuckle to yourself, but when you turn around.

The window has vanished, along with the room. All that remains is the ashen slab where you are standing, supported by nothing. Darkness below, above, and beyond.




It’s only a matter of time before your batteries run out and your flashlights die.

You lost the hand crank flashlight with the rest of your bike.

The three remaining flares you have you begun to use when you can’t resist the urge for warmth, light, and retinal activity.

''')
    flares = input('''

You don’t know how long each flare has burned for. Hours. Days. Your watch broke a long time ago, but you no longer care about the meaning of a minute or even a day.

Since the batteries for the Hi 8 are dead, you can only use your cassette and Bolex to capture your thoughts and sputtering of light from the flares.

You drop one off of the ledge, recording it.

It drops straight down, light reaching nothing around it as it falls. It never reaches the bottom, just winks out into the darkness.
    
''')
    if flares == "":
        print('''

The second flare, however, floats.

You use it as a lamp, taking a bit to read the book you brought along.


The third flare flies straight up, it too vanishes into darkness.

You continue to record. When the three flares all finally vanish, you keep recording, capturing the darkness filling in their absence.

''')

        choice = input(''' "I’ve been feeling surges of nausea, like I’ve got a bad case of the spins." you comment into the cassette.


Are you floating? Falling? Rising? Right side up, upside down, or on your side?


As the nausea stops, you accept that these questions are irrelevant.

Read or wait it out?

''')
        if choice == "read":
            you_occupy()
        elif choice == "wait":
            cover_to_cover