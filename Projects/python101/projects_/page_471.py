
footnote = {
    "footnote1": ["Foolish Fire. Will of the wisp(1608)"]
}

def time_passes():
    read_or_no = input('''


“I have nothing left. No more food. No more water.”


“I have film but the flash is dead.”


“I’m so cold. My feet hurt”



Time passes. You realize "I’m no longer sitting on anything. The slab, whatever it was, is gone. I’m floating or falling or I don’t know what.”


Not even the growl accompanies you.


"I have no sense of anything other than myself" you mutter.



“I know I’m falling and will soon slam into the bottom. I feel it rushing up at me.”



"I won’t even know when I finally do hit. I’ll be dead before I can realize anything’s happened. So there is no bottom. It does not exist for me. Only my end exists.” 



“Maybe that is the something here. The only thing here. My end”



''')

    if read_or_no == "":
            
        time_pass = input('''
        
…


Time passes. You sob. You groan with slight delirium. You still have a bit of humor left in you when you announce to the camera: "It’s not fair in a way. I’ve been falling down so long it feels like floating up to me.”


''')
        if time_pass == "":
            more_time = input('''

    
…

Time passes. The rest of the delirium sets in. All you can do is ramble. Ramble about Tom (“Tom...Tom, is this where you went? Don’t look down, eh?”). Ramble about Delial, your kids, your wife (“I’ve you. I’ve lost you”).

Your words become unintelligible.

“Catch me I’m falling, I’m flying”

“Now I will walk-sleep"


''')

            if more_time == "":
                most_time = input('''
Time passes.

“You become almost light hearted, losing sight of questions of your end, your past, all derailed by some tune lodged in your head, drifting up out of the blue.

“Something like..I think,hmmm…Kinda like (You cough)..Now I find i changed my mind and opened up the door..”


…

“Daisy. Daisy. Daisy. Daisy. Daisy, give me your answer do. I’m half crazy over the love of you. That’s not right.”


…

“Don’t be scared”

“Don’t be”

“I am”
''')
                if most_time == "":
                    input('''



Time passes. All your words and ramblings and murmurs trail into just a painful rasp. Your voice will never heat this world. No voice will.

Memories cease to surface
Sorrow threatens to no longer matter


You are forgetting.
You are dying





Very 
soon you 
will vanish 
completely in the wings 
of your own 
wordless 
stanza




Except
this stanza
does not remain
entirely 
empty 

“Light”



''')
                while(True):
                    footnoting = input('''


Can’t. Be. I see light. Care-”*

''')
                    if footnoting == "": 
                        print('''









Light, a tiny fleck of blue, in the upper right hand corner of your vision








                End
                Yale Film Processing Lab













You close the book

                        
''')
                        break
                    elif footnoting == "footnote":
                        print(footnote["footnote1"])
