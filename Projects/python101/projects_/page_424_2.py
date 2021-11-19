from continue433 import you_continue
from go_back import you_dont_know
def soonhowever():
    while (True):
        print('''
Soon, however, you are clipping along at almost 30 miles per hour
                    ''')
        print('''
        For the next 
	five days you
	cover 240-300
	miles a day, o-
	ne day cover-
	ing 428 miles.

''')
        forward_2 = input('''
The long corridors don’t keep the same form either.	

''')
        if forward_2 == "":
            print('''
______________________________


Sometimes the ceilings drops in on you


_______________________________



______________________________

Getting progressively lower

_______________________________



______________________________

And lower
_______________________________



__________________________________
Until it begins to graze the top of your head
__________________________________



____________________________

Only to shift a few minutes later
____________________________



_____________________________


Rising higher

______________________________



_____________________________



And higher



____________________________



__________________________




Until




_______________________________


''')
        disappears = input('''
        



It disappears all together




''')
        if disappears == "":
            print('''
                 Sometimes 			the hallway
         widens, 					as it continues
    you comment into 						the camera
“This has to 									be some kind 
of enormous										plateau”

“Or an infinitely billiard table”, you continue later as you make a meal. “Or the smooth face of some incredible mountain. One time I stopped and set out to the right on what I thought would be a traverse. Within seconds I was heading downhill again.

''')
            when_you_start = input('''
When you start biking again, the walls reappear, along with ceilings and doorways, shifts in terrain and surroundings marked by a familiar growl.

Days pass. You are running low on food and water.

Your fear of inevitable and immediate doom both compound on you. "I can’t help thinking I’m going to reach an edge to this thing. 
I’ll be going too fast to stop and just fly off into the darkness" you mutter into the cassette.

''')
            if when_you_start == "":
                print('''
Which almost happens.

You can’t tell what day it is (maybe the 12th or 13th day).

After sleeping for what you estimate has to be over 18 hours, you start biking down the hall.

Soon, the halls and 							         doorways recede and
				v a           n          i                          s       h 
then                                                                             of sight
    the                                                                out 
        ceiling
                                                        completely 
		                         is
                       lifts
                                       too 
                                    
                                   it

		   until 
“Direction no longer matters”
''')
                continue_or_back = input('''
                
Do you continue or go back

''')
                if continue_or_back == "continue":
                    you_continue()
                    break
                elif continue_or_back == "go back":
                    you_dont_know()
                    break
                else:
                    break
            else:
                break
        else:
            break
        