from page_464 import this_isnt_unexpected

footnotes  = {
    "footnote1": ['''Erich Kastner in Olberge Weinberge (Frankfurt, 1960, p.95) comments on the force of vertical meanings: The climbing of a mountain reflects redemption. That is due to the force of the word "above" and the power of the word "up". Even those who have long ceased to believe in Heaven or Hell, cannot exchange the words "above" and "below."''']
}

def when_you_grab():
        sleep = input('''
When you grab your things and turn to look at the edge once more, it has disappeared.

In its place stands a bartizan, blocking you from the emptiness. There is only one door.

You go inside.

There is a staircase.

Instead of leading up or down somewhere, it lies on its side, sticking into the wall that leads to the abyss.

You don’t want to investigate it.

So you stay in the room, deciding to spend whatever is left of the day or night (the time stamp on your camera has stopped working) in the only solid place of rest you have found in hours.*

''')
        if sleep == "":
            print('''
When you wake up, you notice the door has vanished.

In its absence, the staircase has righted itself, starting directly above you, rising into the ceiling of the \033[34mHouse\033[0m            
''')
            you_change = input('''
You change the bandages on your leg, eat a small snack, and collect your remaining supplies (your Hi 8, film, video tapes, your cassette, two containers of water, three flares, chemical heaters, and PowerBars) into your pack. You toss it up into the hole.”

You manage to push your flashlight, batteries, and your book onto a step and hoist yourself up.
         
''')
            if you_change == "":
                print('''
As soon as you get on the first step, the floor beneath you has vanished. Your bike, trailer, and additional food and water fall with it

You grab your things in a panic, sprinting up the stairs, trying to distance yourself from the now open pit below you.
                
''')
            while(True):
                staircase = input('''
The staircase seems to have no end. No landings or exits. You keep on moving.

After many hours, you reach the last step. You exit into a small circular chamber with no doorways or passages. Only a narrow vertical shaft and what appears to be a ladder.

Slowly you start climbing, pulling yourself up.

Hours pass, you are still going, only stopping to take brief gulps of water or eat small bites of food.

Stopping, you comment how you will probably have to tie yourself to a rung if you want to try to sleep.

Even the idea of it is unappealing, so you don’t stop. You continue forward, pushing on for a little bit longer.


''')
                if staircase == "":
                    footnote_room = input('''
Finally you reach the last rung. You climb out and standing up, you find yourself inside a very*

                    small 	    room 		with
                    one 	door 		    which
                    you 	cautiously 	    open

''')
                    if footnote_room == "":
                        print('''

''')

                        labryinth = input('''
                    These walls
                    are actually
                    a relief" You 
                    comment 
                    into the cam
                    era (you’ve 
                    left it going
                    the whole time. 
                    You need to 
                    get everything.)
                    “I never tho-
                    ught this 
                    labyrinth
                    would be a
                    pleasant 
                    thing to 
                    return to.”
                    ''')
                    if labryinth == "":
                        print('''
                    Except
                    the furth-
                    er you go,
                    the smaller
                    the hallway
                    gets until
                    you have
                    to remove
                    your pack
                    and crouch.

                        ''')
                        crouch = input('''
                    Except
                    the furth-
                    er you go,
                    the smaller
                    the hallway
                    gets until
                    you have
                    to remove
                    your pack
                    and crouch.



                    Soon
                    you a-
                    re on
                    all 
                    fours, 
                    pushing 
                    your 
                    pack 
                    ahead 
                    of you.
                        
                        
''')
                        if crouch == "":
                            print('''

                    Ano-
                    ther hu-
                    ndred 
                    yards
                    and 
                    you 
                    have 
                    to 
                    crawl
                    on your belly.

''')

                            print('''
                            
                    Your injured leg screams.


                    As you continue forward. At this point,
                    however the pain is excruciating.


                    You keep going.

''')
                            pass_out = input('''

                    At one point, you are unable to move another inch.

                    You pass out

''')
                            if pass_out == "":
                                print('''

                    When you wake, you continue

                    The pain hasn’t gone away. But eventually.

                    You emerge into a very large room.

                    Then everything about the \033[34mHouse\033[0m suddenly changes
                                
''')
                                weird = input('''
                    [XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX]
                    [XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX]
                    [XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX]
                    [XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX]
                    [XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX]
                    [XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX]
                    [XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX]
                    [XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX]
                    [XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX]
                    [XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX]
                    [XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX]                
                                
''')
                                if weird == "":
                                    window = input('''

You stop

“I’m afraid it’ll vanish if I move closer." You whisper "It’s almost worth spending an hour just basking in the sight. I must be nuts to enjoy this so much.”

You step forward. Nothing changes. You continue


[                                                                                         ]
[                                                                                         ]
[                                                                                         ]
[                                    XXXXXX                                               ]
[                                    XXXXXX                                               ]
[                                    XXXXXX                                               ]
[                                    XXXXXX                                               ]
[                                    XXXXXX                                               ]
[                                                                                         ]
[                                                                                         ]
[                                                                                         ]
‘’’
As you move forward, step by step, you realize what you are looking at in front of you. A window.

When you reach it, you climb onto the narrow terrace outside, and for a second time, you are confronted with the absolute absence of anything but darkness.

''')
                                if window == "":
                                    this_isnt_unexpected()
                                    break
                    elif footnote_room == "footnote":
                        print(footnotes["footnote1"])
        elif sleep == "footnote":
            print('''
        
While it would have offered Navidson some comfort, these walls still find Hermann broch's inscription insupportable: "In the middle of all distance stands this \033[34mHouse\033[0m, therefore be fond of it."
        
''')
