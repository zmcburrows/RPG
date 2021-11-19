from rest import you_wake_up
from page_437 import when_you_grab
footnotes = {
    "Footnote1": ['''Navidson is not the only one to have intuitively sense the abyss. During the tragic May assault on Everest where eleven people died, Neal Biedelman, lost at night in a blinding blizzard, described how he stumbled to the edge of the 7,000 foot Kangshung face: "Finally, probably around ten o'clock, I walked over this little rise, and it felt like I was standing on the edge of the earth. I could sense a huge void just beyond." See Jon Krakauer's "Into Thin Air" in Outside v. xxi, n. 9 September 1996 p.64.'''],
}

def you_get_an_idea():
        print('''
You get an idea. You stop and light some magnesium flares, which you throw off to the right and left.

After a hundred yards, you stop and light four more.

You stop for a third time and throw the remaining flares.

You take a step back, take out your camera, and start taking pictures.

''')
        first_image = input('''

In the first image, you can see all twelve flares

''')
        if first_image == "":
            second_image = input('''

In the second image, however, the flares seem further away

''')
            if second_image == "":
                    print('''

By the third image, they are only streaks in the distance.

“I put the camera onto my tripod, we stayed in the same place" you noted on your cassette.

You continue on
''')
            while (True):
                    water = input(''' 
You try and conserve water, drinking as little as you can. Even though your odometer breaks halfway through, you no longer care about the thousands of miles you have traveled.

You are often lost in a trance, as the lamp on your bike illuminates as much as it can (not enough), only darkness ahead and darkness behind you, monotonous. 
However, at one point you notice something and stop.

Something's different.

“It’s as if all along, during the last week, I had sensed something out there" you comment into your camera an hour later. “And then all at once it was gone, replaced by-"*

''')
                    if water == "":
                        print('''

You see it.



The edge.
''')
                        fall = input('''

You panic, trying to stop the bike, but the brakes don’t catch, squealing and shrieking as it threatens to take you over the ledge, so you yank the bike to the ground.

“My leg is pretty torn up, still bleeding a little" you say into the cassette later, still sitting on the ground where you’d crashed. "The trailer’s wreaked too. I think that’s what finally stopped me. I slid right to the edge. My legs were hanging over. And I could feel it too. I don’t know how. There was no wind, no sound, no change of temperature. There was just this terrible emptiness reaching up for me.”

You bandage your wounds.

Stay (and rest) or continue?

''')
                        if fall == "continue":
                                when_you_grab()
                                break
                        elif fall == "stay":
                                you_wake_up()
                                break

                    elif water == "footnote":
                        print(footnotes["Footnote1"])
